import pandas as pd
import streamlit as st
import json
from src.utils.coordinates import convert_coordinate
from src.data.preprocessing import convert_to_native_types

@st.cache_data
def load_steel_plants():
    try:
        df = pd.read_excel("data/raw/steel_plant_data.xlsx")

        df["latitude"] = df["Latitude"].apply(convert_coordinate)
        df["longitude"] = df["Longitude"].apply(convert_coordinate)

        df = df.dropna(subset=["latitude", "longitude"])
        # Convert all numpy types to native Python types for JSON serialization
        df = convert_to_native_types(df)
        return df
    except Exception as e:
        st.error(f"Error loading steel plants data: {str(e)}")
        return pd.DataFrame()



@st.cache_data
def load_geocoded_companies():
    try:
        # Load the geocoded companies data from the external folder
        df = pd.read_excel("data/external/geocoded_combined_companies.xlsx")
        
        # Check what coordinate columns are available
        lat_cols = [col for col in df.columns if 'lat' in col.lower()]
        lon_cols = [col for col in df.columns if 'lon' in col.lower() or 'lng' in col.lower()]
        
        # Use the first available coordinate columns
        lat_col = lat_cols[0] if lat_cols else None
        lon_col = lon_cols[0] if lon_cols else None
        
        if lat_col and lon_col:
            # Clean up any invalid coordinates
            df = df.dropna(subset=[lat_col, lon_col])
            df = df[(df[lat_col].abs() <= 90) & (df[lon_col].abs() <= 180)]
            
            # Create standardized coordinate columns for compatibility with map plotting
            df['latitude'] = df[lat_col]
            df['longitude'] = df[lon_col]
        else:
            st.warning("No coordinate columns found in geocoded companies data")
            
        # Convert all numpy types to native Python types for JSON serialization
        df = convert_to_native_types(df)
        
        # Debug info removed
        
        return df
    except Exception as e:
        st.error(f"Error loading geocoded companies data: {str(e)}")
        return pd.DataFrame()



@st.cache_data
def load_ricemill_data():
    try:
        df = pd.read_csv("data/raw/ricemills.csv")
        
        # Clean up any invalid coordinates
        if "lat" in df.columns and "lng" in df.columns:
            df = df.dropna(subset=["lat", "lng"])
            df = df[(df["lat"].abs() <= 90) & (df["lng"].abs() <= 180)]
            # Convert all numpy types to native Python types for JSON serialization
            df = convert_to_native_types(df)

        return df
    except Exception as e:
        st.error(f"Error loading ricemill data: {str(e)}")
        return pd.DataFrame()


@st.cache_data
def load_geojson_data(geojson_file):
    """Load and cache GeoJSON data"""
    try:
        with open(geojson_file) as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading GeoJSON file {geojson_file}: {str(e)}")
        return None