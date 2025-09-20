import pandas as pd
import re
import streamlit as st
from src.data.preprocessing import memory_efficient_filter, optimize_dataframe_memory, convert_to_native_types

def apply_all_filters(plants, filters):
    """Apply all filters in order and return filtered DataFrame."""

    filtered = plants.copy()
    # Convert to native types to ensure JSON serialization compatibility
    filtered = convert_to_native_types(filtered)

    # State/district filter
    col_filters = {}
    if filters["state"]:
        col_filters["state"] = filters["state"]
    if filters["district"]:
        col_filters["district"] = filters["district"]

    if col_filters:
        filtered = memory_efficient_filter(filtered, col_filters)

    # Name filter
    if filters["name"]:
        name_mask = pd.Series([False] * len(filtered), index=filtered.index)
        if "Plant Name" in filtered.columns:
            name_mask |= filtered["Plant Name"].str.contains(filters["name"], case=False, na=False)
        if "Plant" in filtered.columns:
            name_mask |= filtered["Plant"].str.contains(filters["name"], case=False, na=False)
        filtered = filtered[name_mask]

    # Operational status
    if filters["operational"] and filters["operational_col"]:
        filtered = filtered[filtered[filters["operational_col"]].isin(filters["operational"])]

    # Furnace type
    if filters["furnace"] and filters["furnace_col"]:
        mask = pd.Series([False] * len(filtered), index=filtered.index)
        for ftype in filters["furnace"]:
            mask |= filtered[filters["furnace_col"]].astype(str).str.contains(
                rf"\b{re.escape(ftype)}\b", case=False, na=False
            )
        filtered = filtered[mask]

    # Optimize memory
    if not filtered.empty:
        filtered = optimize_dataframe_memory(filtered)

    return filtered


@st.cache_data
def get_source_data_by_type(filtered_plants, data_sources):
    """Get filtered data for each source type efficiently"""
    source_data_dict = {}
    for source in data_sources:
        source_data = filtered_plants[filtered_plants['source_type'] == source]
        if not source_data.empty:
            source_data_dict[source] = source_data
    return source_data_dict



@st.cache_data
def filter_plants_data(plants, data_sources, state_filter, district_filter, name_filter):
    """Filter plants data based on selected criteria"""
    filtered_plants = plants[plants['source_type'].isin(data_sources)].copy()
    
    # Apply state filter
    if state_filter:
        filtered_plants = filtered_plants[filtered_plants['state'].isin(state_filter)]
    
    # Apply district filter
    if district_filter:
        filtered_plants = filtered_plants[filtered_plants['district'].isin(district_filter)]
    
    # Apply name filter
    if name_filter:
        name_cols = [col for col in ["Plant Name", "Plant", "name", "Company_Name"] if col in filtered_plants.columns]
        if name_cols:
            mask = pd.Series([False]*len(filtered_plants))
            for col in name_cols:
                mask |= filtered_plants[col].str.contains(name_filter, case=False, na=False)
            filtered_plants = filtered_plants[mask]
    
    return filtered_plants
