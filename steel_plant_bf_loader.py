import pandas as pd
import streamlit as st

@st.cache_data
def load_steel_plants_bf():
    try:
        # Load the steel plant BF data from the Excel file
        df = pd.read_excel("steel_plant_bf.xlsx")

        # Dynamically handle latitude and longitude column names
        lat_col = next((col for col in df.columns if col.lower() in ["latitude", "lat"]), None)
        lon_col = next((col for col in df.columns if col.lower() in ["longitude", "lon", "lng", "long"]), None)

        if lat_col and lon_col:
            df = df.dropna(subset=[lat_col, lon_col])
            df = df[(df[lat_col].abs() <= 90) & (df[lon_col].abs() <= 180)]

            # Rename columns to standard names for consistency
            df = df.rename(columns={lat_col: "latitude", lon_col: "longitude"})
        else:
            raise ValueError(f"Latitude and/or Longitude columns are missing or improperly named. Found columns: {list(df.columns)}")

        return df
    except Exception as e:
        st.error(f"Error loading steel plant BF data: {str(e)}")
        return pd.DataFrame()
