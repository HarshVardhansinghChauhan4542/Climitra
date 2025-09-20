import math
import pandas as pd
import streamlit as st

def convert_to_native_types(df):
    """Convert numpy types to native Python types for JSON serialization"""
    df = df.copy()
    for col in df.select_dtypes(include=['float64', 'float32', 'int64', 'int32']).columns:
        df[col] = df[col].astype(float)
    return df

def optimize_dataframe_memory(df):
    """Optimize DataFrame memory usage by converting to appropriate dtypes"""
    optimized_df = df.copy()
    
    # Convert object columns to categorical if they have low cardinality and safe values
    for col in optimized_df.select_dtypes(include=['object']).columns:
        unique_count = optimized_df[col].nunique()
        total_count = len(optimized_df[col])
        
        # Skip if total_count is 0 to avoid division by zero
        if total_count == 0:
            continue
            
        # Skip columns that might contain problematic values for pyarrow
        # Check if column contains values that look like they should remain as strings
        sample_values = optimized_df[col].dropna().head(10)
        if any(isinstance(val, str) and (val.startswith('#') or val.startswith('$') or not val.replace('.', '').replace('-', '').isdigit()) for val in sample_values):
            continue
            
        # Convert to categorical if unique values are less than 50% of total
        if unique_count / total_count < 0.5:
            try:
                optimized_df[col] = optimized_df[col].astype('category')
            except:
                # If conversion fails, keep as object
                pass
    
    # Convert numeric columns to smallest possible dtype
    for col in optimized_df.select_dtypes(include=['int64']).columns:
        col_min = optimized_df[col].min()
        col_max = optimized_df[col].max()
        
        if col_min >= 0:
            if col_max < 255:
                optimized_df[col] = optimized_df[col].astype('uint8')
            elif col_max < 65535:
                optimized_df[col] = optimized_df[col].astype('uint16')
            elif col_max < 4294967295:
                optimized_df[col] = optimized_df[col].astype('uint32')
        else:
            if col_min > -128 and col_max < 127:
                optimized_df[col] = optimized_df[col].astype('int8')
            elif col_min > -32768 and col_max < 32767:
                optimized_df[col] = optimized_df[col].astype('int16')
            elif col_min > -2147483648 and col_max < 2147483647:
                optimized_df[col] = optimized_df[col].astype('int32')
    
    # Keep float64 as is to avoid JSON serialization issues with float32
    # No conversion of float64 to float32
    
    return optimized_df



@st.cache_data
def memory_efficient_filter(data, filters):
    """Apply filters in a memory-efficient way"""
    filtered_data = data.copy()
    
    for filter_key, filter_values in filters.items():
        if filter_values:
            # Check for exact column name match first
            if filter_key in filtered_data.columns:
                column_to_use = filter_key
            else:
                # Try case-insensitive match
                matching_cols = [col for col in filtered_data.columns if col.lower() == filter_key.lower()]
                column_to_use = matching_cols[0] if matching_cols else None
            
            if column_to_use:
                # Use isin() for efficient filtering
                if isinstance(filter_values, list):
                    filtered_data = filtered_data[filtered_data[column_to_use].isin(filter_values)]
                else:
                    # Single value filter
                    filtered_data = filtered_data[filtered_data[column_to_use] == filter_values]
    
    return filtered_data



@st.cache_data
def get_paginated_data(data, page, page_size):
    """Get paginated data slice efficiently"""
    start_idx = (page - 1) * page_size
    end_idx = min(start_idx + page_size, len(data))
    return data.iloc[start_idx:end_idx], start_idx + 1, end_idx



@st.cache_data
def calculate_pagination_info(total_items, page_size):
    """Calculate pagination information"""
    total_pages = math.ceil(total_items / page_size)
    return total_pages


@st.cache_data
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize state, district, plant names, latitude/longitude columns."""
    # State
    if "state" not in df.columns:
        if "State" in df.columns:
            df["state"] = df["State"]
        elif "detailed_state" in df.columns:
            df["state"] = df["detailed_state"]
        else:
            df["state"] = "Unknown"

    if "State" not in df.columns:
        df["State"] = df["state"]

    # District
    if "district" not in df.columns:
        if "District" in df.columns:
            df["district"] = df["District"]
        elif "detailed_district" in df.columns:
            df["district"] = df["detailed_district"]
        elif "address" in df.columns:
            df["district"] = df["address"].apply(
                lambda x: x.split(",")[-2].strip() if isinstance(x, str) and "," in x else "Unknown"
            )
        else:
            df["district"] = "Unknown"

    if "District" not in df.columns:
        df["District"] = df["district"]

    # Plant name
    if "Plant Name" in df.columns and "Plant" not in df.columns:
        df["Plant"] = df["Plant Name"]
    if "Plant" in df.columns and "Plant Name" not in df.columns:
        df["Plant Name"] = df["Plant"]

    # Latitude/Longitude
    if "Latitude" in df.columns and "latitude" not in df.columns:
        df["latitude"] = df["Latitude"]
    if "latitude" in df.columns and "Latitude" not in df.columns:
        df["Latitude"] = df["latitude"]

    if "Longitude" in df.columns and "longitude" not in df.columns:
        df["longitude"] = df["Longitude"]
    if "longitude" in df.columns and "Longitude" not in df.columns:
        df["Longitude"] = df["longitude"]

    return df
