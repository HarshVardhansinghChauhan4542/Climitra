"""
Pagination utilities for data display
"""
import pandas as pd
import streamlit as st
from typing import Dict, List, Tuple


def get_source_data_by_type(filtered_data: pd.DataFrame, data_sources: List[str]) -> Dict[str, pd.DataFrame]:
    """
    Separate filtered data by source type
    
    Args:
        filtered_data: Combined filtered data with source_type column
        data_sources: List of data source names
        
    Returns:
        Dictionary with data source names as keys and filtered dataframes as values
    """
    source_data_dict = {}
    
    for source in data_sources:
        if 'source_type' in filtered_data.columns:
            source_data = filtered_data[filtered_data['source_type'] == source].copy()
        else:
            # If no source_type column, assume all data belongs to this source
            source_data = filtered_data.copy()
        
        if not source_data.empty:
            source_data_dict[source] = source_data
    
    return source_data_dict


def get_or_init_session_state(source: str) -> Tuple[str, str]:
    """
    Initialize or get session state keys for pagination
    
    Args:
        source: Data source name
        
    Returns:
        Tuple of (page_key, size_key)
    """
    page_key = f"page_{source}"
    size_key = f"page_size_{source}"
    
    # Initialize session state if not exists
    if page_key not in st.session_state:
        st.session_state[page_key] = 1
    
    if size_key not in st.session_state:
        st.session_state[size_key] = 10
    
    return page_key, size_key


def calculate_pagination_info(total_items: int, page_size: int) -> int:
    """
    Calculate total pages for pagination
    
    Args:
        total_items: Total number of items
        page_size: Items per page
        
    Returns:
        Total number of pages
    """
    if total_items == 0:
        return 1
    return (total_items + page_size - 1) // page_size


def get_optimized_page_data(source_data: pd.DataFrame, current_page: int, page_size: int, source: str) -> Tuple[pd.DataFrame, int, int]:
    """
    Get paginated data with optimized memory usage
    
    Args:
        source_data: Source dataframe
        current_page: Current page number
        page_size: Items per page
        source: Data source name (for error handling)
        
    Returns:
        Tuple of (paginated_data, start_idx, end_idx)
    """
    if source_data.empty:
        return source_data, 0, 0
    
    # Calculate indices
    start_idx = (current_page - 1) * page_size
    end_idx = min(start_idx + page_size, len(source_data))
    
    # Get paginated data
    paginated_data = source_data.iloc[start_idx:end_idx].copy()
    
    return paginated_data, start_idx + 1, end_idx


def create_plant_cards_vectorized(paginated_data: pd.DataFrame, source: str):
    """
    Create plant cards display using vectorized operations
    
    Args:
        paginated_data: Paginated dataframe to display
        source: Data source name
    """
    if paginated_data.empty:
        st.info("No data to display for this page.")
        return
    
    # Define the columns to display based on source type with fallbacks
    display_columns = {
        "Steel Plants": {
            "primary": ["Plant Name", "State", "District", "Capacity", "Operational"],
            "fallbacks": ["Plant", "Name", "State", "District", "Capacity", "Operational Status", "Status"]
        },
        "Steel Plants with BF": {
            "primary": ["Plant Name", "State", "District", "Capacity", "Operational"],
            "fallbacks": ["Plant", "Name", "State", "District", "Capacity", "Operational Status", "Status"]
        },
        "Rice Mills": {
            "primary": ["Name", "State", "District", "Company"],
            "fallbacks": ["Company", "Location", "Type", "State", "District"]
        },
        "Geocoded Companies": {
            "primary": ["Company", "State", "District", "City"],
            "fallbacks": ["Name", "Company Name", "State", "District", "City", "Sales Revenue"]
        }
    }
    
    # Get column configuration for this source type
    column_config = display_columns.get(source, {"primary": ["State", "District"], "fallbacks": []})
    
    # Try to find available columns, starting with primary then fallbacks
    available_columns = []
    all_possible_columns = column_config["primary"] + column_config["fallbacks"]
    
    for col in all_possible_columns:
        if col in paginated_data.columns and col not in available_columns:
            available_columns.append(col)
            # Limit to 4 columns to keep cards clean
            if len(available_columns) >= 4:
                break
    
    if not available_columns:
        # If no specific columns found, use first 4 available columns (excluding coordinates)
        exclude_cols = ['latitude', 'longitude', 'lat', 'lng', 'source_type']
        available_columns = [col for col in paginated_data.columns if col not in exclude_cols][:4]
    
    if not available_columns:
        st.warning(f"No displayable columns found for {source}")
        return
    
    # Create cards for each row
    for idx, row in paginated_data.iterrows():
        with st.container():
            # Create a card-like container with border
            st.markdown("""
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px; background-color: #f9f9f9;">
            """, unsafe_allow_html=True)
            
            # Try to get a title for the card
            title = ""
            if source == "Geocoded Companies":
                # For geocoded companies, try to use company name as title
                for title_col in ["Company", "Name", "Company Name"]:
                    if title_col in paginated_data.columns and pd.notna(row[title_col]):
                        title = str(row[title_col])
                        break
            elif source in ["Steel Plants", "Steel Plants with BF"]:
                # For steel plants, try to use plant name as title
                for title_col in ["Plant Name", "Plant", "Name"]:
                    if title_col in paginated_data.columns and pd.notna(row[title_col]):
                        title = str(row[title_col])
                        break
            elif source == "Rice Mills":
                # For rice mills, try to use name or company as title
                for title_col in ["Name", "Company"]:
                    if title_col in paginated_data.columns and pd.notna(row[title_col]):
                        title = str(row[title_col])
                        break
            
            # Display title with icon
            if title:
                icon = "🏢" if source == "Geocoded Companies" else "🏭" if source in ["Steel Plants", "Steel Plants with BF"] else "🌾"
                st.markdown(f"**{icon} {title}**")
            else:
                st.markdown(f"**{source} #{idx + 1}**")
            
            # Display the available information
            for col in available_columns:
                # Skip the title column if we already used it
                if title and col in ["Company", "Name", "Company Name", "Plant Name", "Plant"]:
                    continue
                    
                value = row[col]
                if pd.isna(value) or value == "":
                    continue
                elif pd.api.types.is_numeric_dtype(paginated_data[col]):
                    # Format numeric values nicely
                    if "Revenue" in col or "Sales" in col or "Capacity" in col:
                        display_value = f"{value:,.0f}"
                    else:
                        display_value = f"{value:,.2f}"
                else:
                    display_value = str(value).strip()
                    if display_value:
                        st.write(f"**{col}:** {display_value}")
            
            st.markdown("</div>", unsafe_allow_html=True)
