import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.utils.geojson_utils import load_geojson_chunked, generate_hover_texts
from src.data.preprocessing import convert_to_native_types

def render_interactive_map(filtered_plants, data_sources, selected_geojson_files):
    """
    Renders the interactive map with plant points and selected GeoJSON overlays.
    """
    if filtered_plants.empty:
        st.info("No data available for map visualization.")
        return
    
    # Convert all numpy types to native Python types for JSON serialization
    filtered_plants = convert_to_native_types(filtered_plants)

    # Enhanced color map with vibrant colors
    color_map = {
        "Steel Plants": "#8B5CF6",  # Vibrant purple
        "Steel Plants with BF": "#EF4444",  # Bright red
        "Geocoded Companies": "#10B981",  # Emerald green
        "Rice Mills": "#F59E0B"  # Amber orange
    }

    fig = go.Figure()

    # Add plant datasets
    for source in data_sources:
        # Check if source_type column exists, if not use all data
        if 'source_type' in filtered_plants.columns:
            df = filtered_plants[filtered_plants['source_type'] == source]
        else:
            # If no source_type column, use all data for the first source
            df = filtered_plants.copy()
            if data_sources.index(source) > 0:  # Skip subsequent sources
                continue
        if df.empty:
            continue

        # All data sources now use standardized coordinate columns
        lat_col, lon_col = "latitude", "longitude"
        
        if source in ["Steel Plants", "Steel Plants with BF"]:
            hover_name_col = "Plant Name" if "Plant Name" in df.columns else "Plant"
        elif source == "Rice Mills":
            hover_name_col = "name"
        else:  # Geocoded Companies - flexible name column detection
            name_cols = [col for col in df.columns if any(name_term in col.lower() for name_term in ['company', 'name', 'firm', 'business'])]
            hover_name_col = name_cols[0] if name_cols else df.columns[0]  # Use first name-like column or first column

        if lat_col not in df.columns or lon_col not in df.columns:
            continue

        # Ensure numeric and convert to native Python floats
        df = df.copy()
        df[lat_col] = pd.to_numeric(df[lat_col], errors="coerce").astype(float)
        df[lon_col] = pd.to_numeric(df[lon_col], errors="coerce").astype(float)

        hover_texts = generate_hover_texts(df, source, hover_name_col)

        fig.add_trace(go.Scattermapbox(
            lat=df[lat_col],
            lon=df[lon_col],
            mode="markers",
            marker=dict(
                size=10,  # Larger markers for better visibility
                color=color_map.get(source, "#6B7280"),  # Default gray
                opacity=0.8  # Slight transparency for overlapping points
            ),
            name=source,
            text=hover_texts,
            hoverinfo="text",
            showlegend=True  # Ensure legend is shown
        ))

    # Add GeoJSON overlays
    overlay_colors = assign_overlay_colors(selected_geojson_files)

    for geojson_file in selected_geojson_files:
        geojson_data, is_chunked = load_geojson_chunked(geojson_file)
        if geojson_data is None:
            continue

        if is_chunked:
            st.warning(f"Large GeoJSON file detected: {geojson_file}. Showing first 5000 features.")

        add_geojson_overlays(fig, geojson_data, geojson_file, overlay_colors[geojson_file])

    # Enhanced layout with legend and better styling
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_center={"lat": 20.5937, "lon": 78.9629},
        mapbox_zoom=4,
        height=600,  # Taller map for better visibility
        margin={"r":0,"t":30,"l":0,"b":0},  # Top margin for legend
        showlegend=True,  # Ensure legend is shown
        legend=dict(
            title="Data Sources",
            orientation="h",  # Horizontal legend
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        title=dict(
            text="Interactive Map - Multi-Source Data Visualization",
            x=0.5,
            xanchor="center",
            font=dict(size=16)
        )
    )

    st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})


def assign_overlay_colors(selected_files):
    base_colors = [
        "rgba(255, 165, 0, 0.5)",  
        "rgba(0, 128, 255, 0.5)",   
        "rgba(255, 0, 128, 0.5)",   
        "rgba(0, 255, 128, 0.5)",   
        "rgba(128, 0, 255, 0.5)",   
        "rgba(255, 128, 0, 0.5)",   
    ]
    return {f: base_colors[i % len(base_colors)] for i, f in enumerate(selected_files)}


def add_geojson_overlays(fig, geojson_data, geojson_file, overlay_color):
    """Handles adding Polygon/Point/MultiPolygon overlays from GeoJSON to fig."""
    fill_color = overlay_color.replace("0.5", "0.2")
    line_color = overlay_color.replace("0.5", "0.8")

    for feature in geojson_data["features"]:
        geom_type = feature["geometry"]["type"]
        coords = feature["geometry"]["coordinates"]

        if not coords:
            continue

        try:
            if geom_type == "Polygon":
                add_polygon(fig, coords, feature, geojson_file, fill_color, line_color)
            elif geom_type == "Point":
                add_point(fig, coords, feature, overlay_color)
            elif geom_type == "MultiPolygon":
                for i, poly_coords in enumerate(coords):
                    add_polygon(fig, poly_coords, feature, geojson_file, fill_color, line_color, multi=True, idx=i+1)
        except Exception as e:
            st.warning(f"⚠️ Skipped feature in {geojson_file}: {e}")


def add_polygon(fig, coords, feature, geojson_file, fill_color, line_color, multi=False, idx=1):
    if not coords or not coords[0]:
        return
    lons, lats = zip(*coords[0])
    tooltip = build_tooltip(feature, prefix=("MultiPolygon Part " + str(idx)) if multi else "Polygon")
    fig.add_trace(go.Scattermapbox(
        lat=list(lats),
        lon=list(lons),
        fill="toself",
        fillcolor=fill_color,
        line=dict(color=line_color, width=2),
        mode="lines",
        name=f"{'MultiPolygon' if multi else 'Polygon'} ({geojson_file})",
        hovertext=tooltip,
        hoverinfo="text",
        showlegend=False
    ))


def add_point(fig, coords, feature, overlay_color):
    lon, lat = coords
    tooltip = build_tooltip(feature)
    fig.add_trace(go.Scattermapbox(
        lat=[lat],
        lon=[lon],
        mode="markers",
        marker=dict(size=8, color=overlay_color),
        name="GeoJSON Point",
        hovertext=tooltip,
        hoverinfo="text"
    ))


def build_tooltip(feature, prefix=None):
    props = feature.get("properties", {})
    districts = props.get("districts", [])
    states = props.get("states", [])
    tooltip = f"<b>{prefix}</b><br>" if prefix else ""
    if districts:
        tooltip += f"Districts: {', '.join(districts)}<br>"
    if states:
        tooltip += f"States: {', '.join(states)}"
    if not districts and not states:
        tooltip += "Location data unavailable"
    return tooltip


@st.cache_data
def generate_hover_texts(df, source, hover_name_col):
    """Generate hover texts for map markers"""
    hover_texts = []
    for idx, row in df.iterrows():
        name = row[hover_name_col] if hover_name_col in row and pd.notna(row[hover_name_col]) else "Unknown"
        state = row["state"] if "state" in row and pd.notna(row["state"]) else row["State"] if "State" in row and pd.notna(row["State"]) else "Unknown"
        district = row["district"] if "district" in row and pd.notna(row["district"]) else row["District"] if "District" in row and pd.notna(row["District"]) else "Unknown"
        if source == "Steel Plants with BF":
            capacity = row["Quantity"] if "Quantity" in row and pd.notna(row["Quantity"]) else "N/A"
            hover_text = f"<b>{name}</b><br>Capacity: {capacity} Mtpa<br>District: {district}<br>State: {state}"
        else:
            hover_text = f"<b>{name}</b><br>District: {district}<br>State: {state}"
        hover_texts.append(hover_text)
    return hover_texts