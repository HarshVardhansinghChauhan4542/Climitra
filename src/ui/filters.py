import streamlit as st
import pandas as pd

def render_filters(plants):
    """
    Render sidebar filters based on available columns.
    Returns a dictionary of selected filters.
    """
    st.markdown("#### 🔍 Filter Data (applies to all selected sources)")

    filters = {}
    
    # Get data source to determine which filters should be available
    data_source = "Steel Plants"  # Default fallback
    if "source_type" in plants.columns and not plants.empty:
        # Get the first non-null source_type
        source_types = plants["source_type"].dropna().unique()
        if len(source_types) > 0:
            data_source = source_types[0]

    # Name filter
    filters["name"] = st.text_input("Search Name (Plant/Company/Rice Mill)")

    # State filter - always show option
    state_col = next((col for col in plants.columns if col.lower() == "state"), None)
    if state_col:
        filters["state"] = st.multiselect("State", options=plants[state_col].dropna().unique())
    else:
        # Show empty filter when column not present
        filters["state"] = st.multiselect("State", options=[])
        st.caption("No state data available")

    # District filter - always show option
    district_col = next((col for col in plants.columns if col.lower() == "district"), None)
    if district_col:
        filters["district"] = st.multiselect("District", options=plants[district_col].dropna().unique())
    else:
        # Show empty filter when column not present
        filters["district"] = st.multiselect("District", options=[])
        st.caption("No district data available")

    # Operational status - always show option
    op_col = next((col for col in ["Operational", "Operational Status", "Status"] if col in plants.columns), None)
    filters["operational_col"] = op_col
    if op_col:
        values = plants[op_col].dropna().unique()
        filters["operational"] = st.multiselect("Operational Status", options=values)
    else:
        # Show empty filter when column not present
        filters["operational"] = st.multiselect("Operational Status", options=[])
        st.caption("No operational status data available")

    # Furnace type - always show option
    furn_col = next((col for col in ["Furnance", "Furnace Type", "Furnace_Type"] if col in plants.columns), None)
    filters["furnace_col"] = furn_col
    if furn_col:
        unique_types = extract_furnace_types(plants[furn_col])
        filters["furnace"] = st.multiselect("Furnace Type", options=unique_types)
    else:
        # Show empty filter when column not present
        filters["furnace"] = st.multiselect("Furnace Type", options=[])
        st.caption("No furnace type data available")

    return filters


def extract_furnace_types(series):
    """Helper to normalize unique furnace types from a column with combinations."""
    types = set()
    for val in series.dropna():
        for t in str(val).split(","):
            t = t.strip()
            if t:
                types.add(t)
    return sorted(types)


