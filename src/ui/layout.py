import streamlit as st
import pandas as pd

# Data + preprocessing
from src.data.loader import load_steel_plants, load_ricemill_data, load_geocoded_companies
from src.data.preprocessing import optimize_dataframe_memory
from src.data.filters import apply_all_filters
from src.data.data_manager import load_and_merge_data, render_memory_info, render_debug_info
from src.data.metadata_loader import load_geojson_metadata

# UI
from src.ui.filters import render_filters
from src.ui.geojson_ui import render_geojson_overlay_selector
from src.ui.map_plot import render_interactive_map
from src.ui.crop_specific_data import render_crop_specific_data
from src.ui.details import render_detailed_results
from src.ui.summary import generate_data_summary, render_summary_panel

# Utils
from src.utils.memory_utils import get_memory_usage_info, cleanup_session_state

# Pagination utilities
from src.ui.pagination_utils import (
    get_source_data_by_type,
    get_or_init_session_state,
    calculate_pagination_info,
    get_optimized_page_data,
    create_plant_cards_vectorized
)


def _get_important_columns(data_source: str, all_columns: list) -> list:
    """Determine important columns to show by default for each data source"""
    important_cols = []
    
    if data_source in ["Steel Plants", "Steel Plants with BF"]:
        # Steel plants - show only essential details
        steel_plant_cols = [
            "Plant Name", "State", "District", "Capacity", "Operational"
        ]
        important_cols = [col for col in steel_plant_cols if col in all_columns]
        
        # If essential columns not found, try alternatives
        if not important_cols:
            steel_plant_alternatives = [
                "Plant", "Name", "State", "District", "Capacity", 
                "Operational Status", "Status"
            ]
            important_cols = [col for col in steel_plant_alternatives if col in all_columns]
        
    elif data_source == "Rice Mills":
        # Rice mills - show only essential details
        rice_mills_cols = [
            "Name", "State", "District", "Company"
        ]
        important_cols = [col for col in rice_mills_cols if col in all_columns]
        
        # If essential columns not found, try alternatives
        if not important_cols:
            rice_mills_alternatives = [
                "Company", "Location", "Type"
            ]
            important_cols = [col for col in rice_mills_alternatives if col in all_columns]
        
    elif data_source == "Geocoded Companies":
        # Geocoded companies - show only essential details
        geocoded_cols = [
            "Company", "State", "District", "City"
        ]
        important_cols = [col for col in geocoded_cols if col in all_columns]
        
        # If essential columns not found, try alternatives
        if not important_cols:
            geocoded_alternatives = [
                "Name", "latitude", "longitude"
            ]
            important_cols = [col for col in geocoded_alternatives if col in all_columns]
    
    # If no important columns found, show first 4 columns (more focused)
    if not important_cols:
        important_cols = all_columns[:4]
    
    return important_cols



def render_sidebar():
    st.sidebar.header("Navigation")
    section = st.sidebar.radio(
        "Choose Section",
        ["Dashboard", "Crop-Specific Data", "GeoJSON Map"]
    )
    
    # Data source selection - now multi-select
    data_sources = st.sidebar.multiselect(
        "Select Data Sources",
        ["Steel Plants", "Steel Plants with BF", "Geocoded Companies", "Rice Mills"],
        default=["Steel Plants"]
    )
    
    plant_type = st.sidebar.selectbox("Select Plant Type", ["Steel", "Rice"])
    min_capacity = st.sidebar.slider("Minimum Capacity", 0, 5000, 1000)
    show_map = st.sidebar.checkbox("Show Map", True)
    return section, data_sources, plant_type, min_capacity, show_map


# ----------------------------
# Dashboard Rendering
# ----------------------------
def render_main_dashboard(data_sources, min_capacity, show_map):
    st.title("Climitra Steel Plant Dashboard")
    
    if not data_sources:
        st.warning("Please select at least one data source.")
        return

    # First, load a sample dataset to determine available filters
    sample_df = None
    for data_source in data_sources:
        if data_source == "Steel Plants":
            sample_df = load_steel_plants()
        elif data_source == "Steel Plants with BF":
            from assets.pdfs.steel_plant_bf_loader import load_steel_plants_bf
            sample_df = load_steel_plants_bf()
        elif data_source == "Geocoded Companies":
            sample_df = load_geocoded_companies()
        elif data_source == "Rice Mills":
            sample_df = load_ricemill_data()
        
        if not sample_df.empty:
            break
    
    if sample_df is None or sample_df.empty:
        st.warning("No data available for any selected data source.")
        return
    
    # Render filter UI once (using sample data to determine available filters)
    filters = render_filters(sample_df)
    
    all_filtered_data = {}
    all_data_for_map = []
    
    # Load and process each selected data source separately
    for data_source in data_sources:
        # Load base dataset based on selected data source
        if data_source == "Steel Plants":
            df = load_steel_plants()
        elif data_source == "Steel Plants with BF":
            from assets.pdfs.steel_plant_bf_loader import load_steel_plants_bf
            df = load_steel_plants_bf()
        elif data_source == "Geocoded Companies":
            df = load_geocoded_companies()
        elif data_source == "Rice Mills":
            df = load_ricemill_data()
        else:
            df = load_steel_plants()  # default fallback
        
        if df.empty:
            st.warning(f"No data available for {data_source}")
            continue
            
        df = optimize_dataframe_memory(df)
        # Add source_type column for compatibility with map plotting
        df["source_type"] = data_source

        # Apply capacity filter
        if "Capacity" in df.columns:
            df = df[df["Capacity"] >= min_capacity]

        # Apply the same filters to all data sources
        filtered_plants = apply_all_filters(df, filters)
        
        all_filtered_data[data_source] = filtered_plants
        
        # Add to combined data for map visualization
        if not filtered_plants.empty:
            # Standardize coordinate column names for map visualization
            map_df = filtered_plants.copy()
            if data_source == "Rice Mills":
                # Convert rice mills 'lat', 'lng' to 'latitude', 'longitude'
                if "lat" in map_df.columns and "lng" in map_df.columns:
                    map_df["latitude"] = map_df["lat"]
                    map_df["longitude"] = map_df["lng"]
            elif data_source == "Geocoded Companies":
                # Convert geocoded companies 'Latitude', 'Longitude' to lowercase
                if "Latitude" in map_df.columns and "Longitude" in map_df.columns:
                    map_df["latitude"] = map_df["Latitude"]
                    map_df["longitude"] = map_df["Longitude"]
            # Steel plants already use 'latitude', 'longitude'
            
            all_data_for_map.append(map_df)
    
    # Generate data summaries
    summaries = generate_data_summary(all_filtered_data, data_sources)
    
    # Combined map visualization - MOVED ABOVE TABLES
    if show_map and all_data_for_map:
        combined_df = pd.concat(all_data_for_map, ignore_index=True)
        if "latitude" in combined_df.columns and "longitude" in combined_df.columns:
            map_data = combined_df[["latitude", "longitude", "source_type"]].dropna()
            if not map_data.empty:
                st.subheader("🗺️ Combined Map View")
                # Use the interactive map with color coding for different data sources
                render_interactive_map(combined_df, data_sources, [])
                st.caption(f"Showing {len(map_data)} locations from {len(data_sources)} data sources")
    
    st.markdown("---")
    
    # Two-column layout: Detailed Data (Left) and Summary (Right)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Combine all filtered data for pagination
        combined_filtered_data = pd.concat(all_filtered_data.values(), ignore_index=True)
        
        if not combined_filtered_data.empty:
            st.markdown("---")
            st.markdown(f"#### 📋 Filtered Plant List ({len(combined_filtered_data)} plants)")
            
            # Use cached function to get source data efficiently
            source_data_dict = get_source_data_by_type(combined_filtered_data, data_sources)
            
            # Show separate tables for each data source
            for source, source_data in source_data_dict.items():
                # Create a section for each data source
                st.markdown(f"**{source}** ({len(source_data)} items)")
                
                # Use optimized session state function
                page_key, size_key = get_or_init_session_state(source)
                
                # Use cached function for pagination calculations
                total_pages = calculate_pagination_info(len(source_data), st.session_state[size_key])
                
                # Reset to page 1 if current page is out of bounds
                if st.session_state[page_key] > total_pages:
                    st.session_state[page_key] = 1
                
                # Use optimized page data function for memory-efficient pagination
                paginated_data, start_idx, end_idx = get_optimized_page_data(
                    source_data, st.session_state[page_key], st.session_state[size_key], source
                )
                
                # Create columns for pagination controls and page size selection
                pagination_col1, pagination_col2, pagination_col3 = st.columns([2, 1, 2])
                
                with pagination_col1:
                    # Previous button
                    if st.session_state[page_key] > 1:
                        if st.button("⬅️ Previous", key=f"prev_{page_key}"):
                            st.session_state[page_key] -= 1
                            st.rerun()
                    else:
                        st.button("⬅️ Previous", key=f"prev_{page_key}", disabled=True)
                
                with pagination_col2:
                    # Page size selector
                    page_size = st.selectbox(
                        "Items per page:",
                        [5, 10, 20, 50],
                        index=1,  # Default to 10
                        key=size_key
                    )
                    if page_size != st.session_state[size_key]:
                        st.session_state[size_key] = page_size
                        st.session_state[page_key] = 1
                        st.rerun()
                
                with pagination_col3:
                    # Next button
                    if st.session_state[page_key] < total_pages:
                        if st.button("Next ➡️", key=f"next_{page_key}"):
                            st.session_state[page_key] += 1
                            st.rerun()
                    else:
                        st.button("Next ➡️", key=f"next_{page_key}", disabled=True)
                
                # Page info
                st.markdown(f"**Page {st.session_state[page_key]} of {total_pages}** (Showing items {start_idx}-{end_idx} of {len(source_data)})")
                
                # Create a container for the paginated plant list
                with st.container():
                    # Display data as a simple table with specific columns
                    if not paginated_data.empty:
                        # Define columns based on data source type
                        if source == 'Steel Plants' or source == 'Steel Plants with BF':
                            desired_columns = ['Plant Name', 'Capacity', 'Furnace Type', 'Status', 'State', 'District']
                        elif source == 'Rice Mills':
                            desired_columns = ['detailed_district', 'Name', 'Rice mill name', 'state', 'address']
                        elif source == 'Geocoded Companies':
                            desired_columns = ['Company', 'State', 'District', 'City', 'Name']
                        else:
                            # Default fallback
                            desired_columns = ['Name', 'State', 'District']
                        
                        # Define alternative column names based on data source type
                        if source == 'Steel Plants' or source == 'Steel Plants with BF':
                            alt_columns = {
                                'Plant Name': ['Plant', 'Name', 'Company'],
                                'Capacity': ['Capacity'],
                                'Furnace Type': ['Furnace Type', 'Furnace_Type', 'Furnance'],
                                'Status': ['Operational', 'Operational Status'],
                                'State': ['State'],
                                'District': ['District']
                            }
                        elif source == 'Rice Mills':
                            alt_columns = {
                                'detailed_district': ['detailed_district', 'District', 'district'],
                                'Name': ['Name', 'Company'],
                                'Rice mill name': ['Rice mill name', 'Rice Mill Name', 'Mill Name', 'Mill name'],
                                'state': ['state', 'State'],
                                'address': ['address', 'Address', 'Location', 'location']
                            }
                        elif source == 'Geocoded Companies':
                            alt_columns = {
                                'Company': ['Name', 'Plant', 'Plant Name'],
                                'State': ['State'],
                                'District': ['District'],
                                'City': ['City', 'Location'],
                                'Name': ['Company', 'Plant']
                            }
                        else:
                            # Default fallback
                            alt_columns = {
                                'Name': ['Company', 'Plant', 'Plant Name'],
                                'State': ['State'],
                                'District': ['District']
                            }
                        
                        # Find which columns actually exist in the data
                        available_columns = []
                        used_columns = set()  # Track which actual columns have been used
                        
                        for desired_col in desired_columns:
                            # First try exact match
                            if desired_col in paginated_data.columns and desired_col not in used_columns:
                                available_columns.append(desired_col)
                                used_columns.add(desired_col)
                            else:
                                # Try alternative names
                                for alt_name in alt_columns.get(desired_col, []):
                                    if alt_name in paginated_data.columns and alt_name not in used_columns:
                                        available_columns.append(alt_name)
                                        used_columns.add(alt_name)
                                        break
                        
                        # Display the table with available columns
                        if available_columns:
                            display_data = paginated_data[available_columns]
                            st.dataframe(display_data, use_container_width=True)
                        else:
                            # Fallback: show first 6 columns if no desired columns found
                            st.dataframe(paginated_data.iloc[:, :6], use_container_width=True)
                
                # Add separator between data sources
                st.markdown("---")
        else:
            st.info("No data matches the current filters.")
    
    with col2:
        # Summary statistics
        st.markdown("#### 📊 Summary")
        st.write(f"**Total Plants:** {len(combined_filtered_data)}")
        
        # Show counts by source type
        for source in data_sources:
            count = len(combined_filtered_data[combined_filtered_data['source_type'] == source])
            if count > 0:
                st.write(f"**{source}:** {count}")
        
        # Show counts by state if state filter is applied
        # Note: state_filter would need to be passed to this function or retrieved from session state
        
        # Show counts by operational status if available
        if 'Operational' in combined_filtered_data.columns:
            st.markdown("---")
            
            # Get status counts
            status_counts = combined_filtered_data['Operational'].value_counts()
            total_count = len(combined_filtered_data[combined_filtered_data['Operational'].notna()])
            
            if total_count > 0:
                # Define main statuses and special cases
                main_statuses = ['Active', 'NP', 'A']
                special_cases = []
                
                # Separate main statuses from special cases
                for status in status_counts.index:
                    if pd.notna(status):
                        # Normalize status for comparison (strip whitespace, case-insensitive)
                        normalized_status = str(status).strip().lower()
                        is_main_status = False
                        for main_status in main_statuses:
                            if normalized_status == main_status.strip().lower():
                                is_main_status = True
                                break
                        
                        if is_main_status:
                            continue  # Will handle main statuses separately
                        else:
                            special_cases.append(status)
                
                # Display total count
                st.markdown(f"**Statuses (Total: {total_count})**")
                
                # Display main statuses
                for main_status in main_statuses:
                    # Find matching status in data (case-insensitive, whitespace-insensitive)
                    found_status = None
                    for status in status_counts.index:
                        if pd.notna(status) and str(status).strip().lower() == main_status.strip().lower():
                            found_status = status
                            break
                    
                    if found_status is not None:
                        count = status_counts[found_status]
                        st.write(f"  • {found_status}: {count}")
                
                # Display special cases in expandable section if any exist
                if special_cases:
                    with st.expander("Special Cases (expand ▼)"):
                        for status in special_cases:
                            count = status_counts[status]
                            st.write(f"       - {status}: {count}")
        
        # Show counts by furnace type if available
        furnace_col = None
        for col in ['Furnance', 'Furnace Type', 'Furnace_Type']:
            if col in combined_filtered_data.columns:
                furnace_col = col
                break
        
        if furnace_col:
            st.markdown("---")
            
            # Get furnace type counts
            furnace_counts = combined_filtered_data[furnace_col].value_counts()
            total_count = len(combined_filtered_data[combined_filtered_data[furnace_col].notna()])
            
            # Define main furnace categories and their subtypes
            main_furnace_types = ['IF', 'RM', 'EAF', 'BF', 'DRI']
            furnace_categories = {}
            
            # Categorize furnace types
            for furnace_type in furnace_counts.index:
                if pd.notna(furnace_type):
                    furnace_str = str(furnace_type).strip()
                    
                    # Determine primary category
                    primary_category = None
                    for main_type in main_furnace_types:
                        if main_type in furnace_str:
                            primary_category = main_type
                            break
                    
                    if primary_category is None:
                        primary_category = 'Other'
                    
                    # Add to category
                    if primary_category not in furnace_categories:
                        furnace_categories[primary_category] = {}
                    furnace_categories[primary_category][furnace_type] = furnace_counts[furnace_type]
            
            # Display total count
            st.markdown(f"**Furnace Types (Total: {total_count})**")
            
            # Display main furnace categories
            for main_type in main_furnace_types:
                if main_type in furnace_categories:
                    category_total = sum(furnace_categories[main_type].values())
                    
                    # Check if this category has multiple subtypes
                    subtypes = furnace_categories[main_type]
                    
                    if len(subtypes) == 1 and list(subtypes.keys())[0] == main_type:
                        # Single subtype that matches the main type
                        furnace_subtype = list(subtypes.keys())[0]
                        count = subtypes[furnace_subtype]
                        st.write(f"  • {main_type}: {count}")
                    else:
                        # Multiple subtypes or complex combinations
                        with st.expander(f"▶ {main_type} ({category_total})"):
                            for furnace_subtype, count in subtypes.items():
                                st.write(f"   • {furnace_subtype}: {count}")
            
            # Display Other category if it exists
            if 'Other' in furnace_categories:
                with st.expander(f"▶ Other ({sum(furnace_categories['Other'].values())})"):
                    for furnace_subtype, count in furnace_categories['Other'].items():
                        st.write(f"   • {furnace_subtype}: {count}")




# ----------------------------
# Layout Router
# ----------------------------
def render_main_layout(pdf_viewer=None):
    st.title("Biochar Cluster Map with Industrial Data and GeoJSON Overlays")

    # Load GeoJSON metadata
    geojson_metadata = load_geojson_metadata()

    # Sidebar navigation
    section, data_sources, plant_type, min_capacity, show_map = render_sidebar()

    # Dashboard Section
    if section == "Dashboard":
        render_main_dashboard(data_sources, min_capacity, show_map)

        # Diagnostics block (memory + debug info)
        st.markdown("---")
        st.subheader("⚙️ Diagnostics")
        if data_sources:
            plants = load_and_merge_data(data_sources)  # quick merge for debug
            if not plants.empty:
                render_memory_info()
                render_debug_info(plants, data_sources)

    # Crop-Specific Data Section
    elif section == "Crop-Specific Data":
        render_crop_specific_data(pdf_viewer)

    # GeoJSON Map Section
    elif section == "GeoJSON Map":
        st.title("🗺️ GeoJSON Overlays + Plant Map")

        # Select overlay(s)
        selected_files = render_geojson_overlay_selector(geojson_metadata)

        # Load datasets based on selected data sources
        if not data_sources:
            st.warning("Please select at least one data source to display on the map.")
            return
            
        all_dataframes = []
        
        for data_source in data_sources:
            if data_source == "Steel Plants":
                df = load_steel_plants()
            elif data_source == "Steel Plants with BF":
                from assets.pdfs.steel_plant_bf_loader import load_steel_plants_bf
                df = load_steel_plants_bf()
            elif data_source == "Geocoded Companies":
                df = load_geocoded_companies()
            elif data_source == "Rice Mills":
                df = load_ricemill_data()
            else:
                df = load_steel_plants()  # default fallback
                
            if not df.empty:
                df = optimize_dataframe_memory(df)
                df["source_type"] = data_source  # Add source type for map visualization
                all_dataframes.append(df)
        
        # Combine all dataframes for map visualization
        if all_dataframes:
            combined_df = pd.concat(all_dataframes, ignore_index=True)
            render_interactive_map(combined_df, data_sources, selected_files)
        else:
            st.warning("No data available for the selected data sources.")
