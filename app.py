import plotly.express as px
import pandas as pd
import math
import streamlit as st
import json
import os
import re
from PIL import Image
import base64
import streamlit.components.v1 as components
from streamlit_pdf_viewer import pdf_viewer

def get_location_info_from_coords(polygon):
    """
    Enhanced function to estimate location based on polygon centroid coordinates
    Maps coordinates to actual Indian states and major districts
    """
    try:
        centroid = polygon.centroid
        lat, lon = centroid.y, centroid.x
        
        # Detailed coordinate-based state and district identification for India
        
        # Rajasthan
        if 24.0 <= lat <= 30.2 and 69.5 <= lon <= 78.2:
            districts = []
            if 26.8 <= lat <= 28.4 and 75.0 <= lon <= 76.8:
                districts = ["Jaipur", "Alwar", "Sikar"]
            elif 24.3 <= lat <= 26.0 and 70.9 <= lon <= 73.8:
                districts = ["Jodhpur", "Barmer", "Jaisalmer"]
            elif 27.0 <= lat <= 28.9 and 73.0 <= lon <= 75.5:
                districts = ["Bikaner", "Ganganagar", "Hanumangarh"]
            elif 24.0 <= lat <= 25.8 and 73.7 <= lon <= 75.8:
                districts = ["Udaipur", "Rajsamand", "Dungarpur"]
            else:
                districts = ["Central Rajasthan"]
            return districts, ["Rajasthan"]
        
        # Gujarat
        elif 20.1 <= lat <= 24.7 and 68.2 <= lon <= 74.5:
            districts = []
            if 22.2 <= lat <= 23.8 and 72.0 <= lon <= 73.2:
                districts = ["Ahmedabad", "Gandhinagar", "Mehsana"]
            elif 21.1 <= lat <= 22.3 and 70.0 <= lon <= 72.1:
                districts = ["Rajkot", "Jamnagar", "Porbandar"]
            elif 20.9 <= lat <= 21.9 and 72.7 <= lon <= 73.2:
                districts = ["Surat", "Navsari", "Valsad"]
            elif 22.7 <= lat <= 24.2 and 68.8 <= lon <= 71.8:
                districts = ["Kutch", "Banaskantha", "Patan"]
            else:
                districts = ["Central Gujarat"]
            return districts, ["Gujarat"]
        
        # Maharashtra
        elif 15.6 <= lat <= 22.0 and 72.6 <= lon <= 80.9:
            districts = []
            if 18.8 <= lat <= 19.3 and 72.7 <= lon <= 73.2:
                districts = ["Mumbai", "Mumbai Suburban", "Thane"]
            elif 18.4 <= lat <= 18.7 and 73.7 <= lon <= 74.0:
                districts = ["Pune", "Pimpri-Chinchwad"]
            elif 19.7 <= lat <= 21.2 and 78.0 <= lon <= 79.3:
                districts = ["Nagpur", "Wardha", "Chandrapur"]
            elif 19.0 <= lat <= 20.3 and 74.7 <= lon <= 76.0:
                districts = ["Aurangabad", "Jalna", "Beed"]
            else:
                districts = ["Central Maharashtra"]
            return districts, ["Maharashtra"]
        
        # Karnataka
        elif 11.5 <= lat <= 18.5 and 74.0 <= lon <= 78.6:
            districts = []
            if 12.8 <= lat <= 13.2 and 77.4 <= lon <= 77.8:
                districts = ["Bangalore Urban", "Bangalore Rural"]
            elif 15.3 <= lat <= 15.9 and 75.0 <= lon <= 75.8:
                districts = ["Belgaum", "Bagalkot", "Bijapur"]
            elif 13.3 <= lat <= 14.5 and 74.8 <= lon <= 75.8:
                districts = ["Mysore", "Mandya", "Hassan"]
            elif 14.4 <= lat <= 15.6 and 76.0 <= lon <= 77.6:
                districts = ["Bellary", "Raichur", "Koppal"]
            else:
                districts = ["Central Karnataka"]
            return districts, ["Karnataka"]
        
        # Tamil Nadu
        elif 8.1 <= lat <= 13.6 and 76.2 <= lon <= 80.3:
            districts = []
            if 12.8 <= lat <= 13.2 and 79.8 <= lon <= 80.3:
                districts = ["Chennai", "Kanchipuram", "Tiruvallur"]
            elif 10.7 <= lat <= 11.1 and 76.9 <= lon <= 77.8:
                districts = ["Coimbatore", "Tirupur", "Erode"]
            elif 9.9 <= lat <= 10.8 and 78.0 <= lon <= 78.8:
                districts = ["Madurai", "Theni", "Dindigul"]
            elif 11.8 <= lat <= 12.5 and 79.0 <= lon <= 79.9:
                districts = ["Vellore", "Tiruvannamalai", "Villupuram"]
            else:
                districts = ["Central Tamil Nadu"]
            return districts, ["Tamil Nadu"]
        
        # Andhra Pradesh & Telangana
        elif 12.6 <= lat <= 19.9 and 76.8 <= lon <= 84.8:
            districts = []
            if 17.2 <= lat <= 17.6 and 78.2 <= lon <= 78.7:
                districts = ["Hyderabad", "Rangareddy", "Medchal"]
                return districts, ["Telangana"]
            elif 15.8 <= lat <= 17.1 and 79.7 <= lon <= 81.8:
                districts = ["Visakhapatnam", "Vizianagaram", "Srikakulam"]
                return districts, ["Andhra Pradesh"]
            elif 14.4 <= lat <= 15.9 and 78.1 <= lon <= 80.0:
                districts = ["Kurnool", "Anantapur", "Kadapa"]
                return districts, ["Andhra Pradesh"]
            elif 16.5 <= lat <= 19.0 and 77.3 <= lon <= 80.5:
                districts = ["Warangal", "Karimnagar", "Nizamabad"]
                return districts, ["Telangana"]
            else:
                districts = ["Central Region"]
                return districts, ["Andhra Pradesh/Telangana"]
        
        # Kerala
        elif 8.2 <= lat <= 12.8 and 74.9 <= lon <= 77.4:
            districts = []
            if 9.9 <= lat <= 10.0 and 76.2 <= lon <= 76.4:
                districts = ["Kochi", "Ernakulam"]
            elif 8.4 <= lat <= 8.9 and 76.8 <= lon <= 77.1:
                districts = ["Thiruvananthapuram", "Kollam"]
            elif 11.2 <= lat <= 11.6 and 75.7 <= lon <= 76.1:
                districts = ["Kozhikode", "Malappuram", "Wayanad"]
            elif 9.5 <= lat <= 10.5 and 76.0 <= lon <= 77.0:
                districts = ["Kottayam", "Idukki", "Alappuzha"]
            else:
                districts = ["Central Kerala"]
            return districts, ["Kerala"]
        
        # West Bengal
        elif 21.5 <= lat <= 27.1 and 85.8 <= lon <= 89.9:
            districts = []
            if 22.4 <= lat <= 22.7 and 88.2 <= lon <= 88.5:
                districts = ["Kolkata", "North 24 Parganas", "South 24 Parganas"]
            elif 23.2 <= lat <= 25.6 and 87.8 <= lon <= 89.3:
                districts = ["Darjeeling", "Jalpaiguri", "Cooch Behar"]
            elif 23.8 <= lat <= 24.6 and 87.0 <= lon <= 88.8:
                districts = ["Malda", "Murshidabad", "Birbhum"]
            else:
                districts = ["Central West Bengal"]
            return districts, ["West Bengal"]
        
        # Odisha
        elif 17.8 <= lat <= 22.6 and 81.4 <= lon <= 87.5:
            districts = []
            if 20.2 <= lat <= 20.4 and 85.7 <= lon <= 86.0:
                districts = ["Bhubaneswar", "Khordha", "Puri"]
            elif 21.4 <= lat <= 22.0 and 84.8 <= lon <= 85.8:
                districts = ["Rourkela", "Sundargarh", "Jharsuguda"]
            elif 19.2 <= lat <= 20.5 and 83.9 <= lon <= 85.2:
                districts = ["Cuttack", "Jagatsinghpur", "Kendrapara"]
            else:
                districts = ["Central Odisha"]
            return districts, ["Odisha"]
        
        # Madhya Pradesh
        elif 21.1 <= lat <= 26.9 and 74.0 <= lon <= 82.8:
            districts = []
            if 23.1 <= lat <= 23.4 and 77.2 <= lon <= 77.6:
                districts = ["Bhopal", "Sehore", "Raisen"]
            elif 22.6 <= lat <= 23.0 and 75.7 <= lon <= 76.1:
                districts = ["Indore", "Dewas", "Ujjain"]
            elif 24.5 <= lat <= 25.9 and 78.0 <= lon <= 80.4:
                districts = ["Jabalpur", "Katni", "Narsinghpur"]
            elif 24.0 <= lat <= 25.4 and 81.2 <= lon <= 82.8:
                districts = ["Rewa", "Satna", "Sidhi"]
            else:
                districts = ["Central Madhya Pradesh"]
            return districts, ["Madhya Pradesh"]
        
        # Uttar Pradesh
        elif 23.9 <= lat <= 30.4 and 77.1 <= lon <= 84.6:
            districts = []
            if 28.4 <= lat <= 28.8 and 77.0 <= lon <= 77.4:
                districts = ["New Delhi", "Ghaziabad", "Gautam Buddha Nagar"]
            elif 26.8 <= lat <= 27.2 and 80.8 <= lon <= 81.0:
                districts = ["Lucknow", "Unnao", "Rae Bareli"]
            elif 25.3 <= lat <= 25.5 and 82.9 <= lon <= 83.1:
                districts = ["Varanasi", "Chandauli", "Jaunpur"]
            elif 27.1 <= lat <= 27.3 and 78.0 <= lon <= 78.2:
                districts = ["Agra", "Mathura", "Firozabad"]
            else:
                districts = ["Central Uttar Pradesh"]
            return districts, ["Uttar Pradesh"]
        
        # Punjab
        elif 29.5 <= lat <= 32.5 and 73.9 <= lon <= 76.9:
            districts = []
            if 31.6 <= lat <= 31.8 and 74.8 <= lon <= 75.0:
                districts = ["Amritsar", "Tarn Taran", "Gurdaspur"]
            elif 30.3 <= lat <= 30.5 and 75.8 <= lon <= 76.0:
                districts = ["Ludhiana", "Jalandhar", "Kapurthala"]
            elif 30.9 <= lat <= 31.1 and 75.3 <= lon <= 75.5:
                districts = ["Patiala", "Fatehgarh Sahib", "Sangrur"]
            else:
                districts = ["Central Punjab"]
            return districts, ["Punjab"]
        
        # Haryana
        elif 27.7 <= lat <= 30.9 and 74.5 <= lon <= 77.6:
            districts = []
            if 28.4 <= lat <= 28.6 and 76.9 <= lon <= 77.1:
                districts = ["Gurugram", "Faridabad", "Palwal"]
            elif 29.1 <= lat <= 29.3 and 76.0 <= lon <= 76.2:
                districts = ["Hisar", "Fatehabad", "Sirsa"]
            elif 28.8 <= lat <= 29.0 and 76.6 <= lon <= 76.8:
                districts = ["Rohtak", "Jhajjar", "Sonipat"]
            else:
                districts = ["Central Haryana"]
            return districts, ["Haryana"]
        
        # Jharkhand
        elif 21.9 <= lat <= 25.3 and 83.3 <= lon <= 87.6:
            districts = []
            if 23.3 <= lat <= 23.5 and 85.2 <= lon <= 85.4:
                districts = ["Ranchi", "Khunti", "Lohardaga"]
            elif 22.7 <= lat <= 22.9 and 86.1 <= lon <= 86.3:
                districts = ["Jamshedpur", "East Singhbhum", "West Singhbhum"]
            elif 24.6 <= lat <= 24.8 and 85.9 <= lon <= 86.1:
                districts = ["Dhanbad", "Bokaro", "Giridih"]
            else:
                districts = ["Central Jharkhand"]
            return districts, ["Jharkhand"]
        
        # Chhattisgarh
        elif 17.8 <= lat <= 24.1 and 80.2 <= lon <= 84.4:
            districts = []
            if 21.2 <= lat <= 21.4 and 81.5 <= lon <= 81.7:
                districts = ["Raipur", "Durg", "Bilaspur"]
            elif 19.0 <= lat <= 19.2 and 81.9 <= lon <= 82.1:
                districts = ["Jagdalpur", "Bastar", "Kondagaon"]
            else:
                districts = ["Central Chhattisgarh"]
            return districts, ["Chhattisgarh"]
        
        # Bihar
        elif 24.3 <= lat <= 27.5 and 83.3 <= lon <= 88.1:
            districts = []
            if 25.5 <= lat <= 25.7 and 85.0 <= lon <= 85.2:
                districts = ["Patna", "Nalanda", "Jehanabad"]
            elif 26.1 <= lat <= 26.3 and 85.1 <= lon <= 85.3:
                districts = ["Muzaffarpur", "Sitamarhi", "Sheohar"]
            else:
                districts = ["Central Bihar"]
            return districts, ["Bihar"]
        
        # Assam and Northeast
        elif 24.1 <= lat <= 28.2 and 89.7 <= lon <= 97.1:
            districts = []
            if 26.1 <= lat <= 26.3 and 91.7 <= lon <= 91.9:
                districts = ["Guwahati", "Kamrup", "Nalbari"]
                return districts, ["Assam"]
            elif 25.5 <= lat <= 25.7 and 91.8 <= lon <= 92.0:
                districts = ["Shillong", "East Khasi Hills", "West Khasi Hills"]
                return districts, ["Meghalaya"]
            elif 23.7 <= lat <= 24.7 and 91.2 <= lon <= 92.7:
                districts = ["Agartala", "West Tripura", "Sepahijala"]
                return districts, ["Tripura"]
            elif 25.1 <= lat <= 27.7 and 93.2 <= lon <= 97.4:
                districts = ["Itanagar", "Papum Pare", "Lower Subansiri"]
                return districts, ["Arunachal Pradesh"]
            else:
                districts = ["Northeast Region"]
                return districts, ["Northeast States"]
        
        # Himachal Pradesh
        elif 30.2 <= lat <= 33.2 and 75.6 <= lon <= 79.0:
            districts = []
            if 31.1 <= lat <= 31.3 and 77.1 <= lon <= 77.3:
                districts = ["Shimla", "Solan", "Sirmaur"]
            elif 32.2 <= lat <= 32.4 and 76.3 <= lon <= 76.5:
                districts = ["Dharamshala", "Kangra", "Hamirpur"]
            else:
                districts = ["Central Himachal Pradesh"]
            return districts, ["Himachal Pradesh"]
        
        # Uttarakhand
        elif 28.4 <= lat <= 31.5 and 77.6 <= lon <= 81.0:
            districts = []
            if 30.3 <= lat <= 30.5 and 78.0 <= lon <= 78.2:
                districts = ["Dehradun", "Tehri Garhwal", "Pauri Garhwal"]
            elif 29.2 <= lat <= 29.4 and 79.5 <= lon <= 79.7:
                districts = ["Nainital", "Almora", "Pithoragarh"]
            else:
                districts = ["Central Uttarakhand"]
            return districts, ["Uttarakhand"]
        
        # Jammu & Kashmir / Ladakh
        elif 32.3 <= lat <= 37.1 and 73.3 <= lon <= 80.3:
            districts = []
            if 34.0 <= lat <= 34.2 and 74.7 <= lon <= 74.9:
                districts = ["Srinagar", "Budgam", "Ganderbal"]
                return districts, ["Jammu & Kashmir"]
            elif 32.7 <= lat <= 32.9 and 74.8 <= lon <= 75.0:
                districts = ["Jammu", "Samba", "Kathua"]
                return districts, ["Jammu & Kashmir"]
            elif 34.1 <= lat <= 34.3 and 77.5 <= lon <= 77.7:
                districts = ["Leh", "Kargil"]
                return districts, ["Ladakh"]
            else:
                districts = ["Northern Region"]
                return districts, ["Jammu & Kashmir/Ladakh"]
        
        # Goa
        elif 15.0 <= lat <= 15.8 and 73.7 <= lon <= 74.3:
            districts = ["North Goa", "South Goa"]
            return districts, ["Goa"]
        
        # Default case for coordinates not matching any state
        else:
            return ["Region Unknown"], ["State Unknown"]
            
    except Exception as e:
        return ["Region Unknown"], ["State Unknown"]

###
st.set_page_config(page_title="Biochar Dashboard")

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-size: 13px !important;
    }
    .block-container {
        padding: 0.5rem 1rem 0.5rem 1rem;
    }
    .stSidebar {
        width: 220px !important;
    }
    .stDataFrame {
        font-size: 12px !important;
    }
    h1, h2, h3 {
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

if "show_sidebar" not in st.session_state:
    st.session_state["show_sidebar"] = True

if st.button("👈 Toggle Sidebar"):
    st.session_state["show_sidebar"] = not st.session_state["show_sidebar"]

section = "Dashboard"
if st.session_state["show_sidebar"]:
    with st.sidebar:
        section = st.radio("Navigate", ["Dashboard", "Crop-Specific Data"])

def circle_coords(lon, lat, radius_km, n_points=100):
    coords = []
    for i in range(n_points):
        angle = 2 * math.pi * i / n_points
        dx = radius_km * math.cos(angle)
        dy = radius_km * math.sin(angle)
        dlon = dx / (111.32 * math.cos(math.radians(lat)))
        dlat = dy / 111.32
        coords.append((lon + dlon, lat + dlat))
    return coords

@st.cache_data
def load_steel_plants():
    try:
        df = pd.read_excel("steel_plant_data.xlsx")

        df["latitude"] = df["Latitude"].apply(convert_coordinate)
        df["longitude"] = df["Longitude"].apply(convert_coordinate)

        df = df.dropna(subset=["latitude", "longitude"])
        return df
    except Exception as e:
        st.error(f"Error loading steel plants data: {str(e)}")
        return pd.DataFrame()

@st.cache_data
def load_geocoded_companies():
    try:
        df = pd.read_excel("geocoded_combined_companies.xlsx")
        # Clean up any invalid coordinates
        df = df.dropna(subset=["Latitude", "Longitude"])
        df = df[(df["Latitude"].abs() <= 90) & (df["Longitude"].abs() <= 180)]
        return df
    except Exception as e:
        st.error(f"Error loading geocoded companies data: {str(e)}")
        return pd.DataFrame()

@st.cache_data
def load_ricemill_data():
    try:
        df = pd.read_csv("ricemills.csv")
        
        # Clean up any invalid coordinates
        if "lat" in df.columns and "lng" in df.columns:
            df = df.dropna(subset=["lat", "lng"])
            df = df[(df["lat"].abs() <= 90) & (df["lng"].abs() <= 180)]

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

@st.cache_data
def convert_coordinate(coord):
    """Convert coordinate string to decimal format"""
    try:
        if isinstance(coord, str) and "°" in coord:
            parts = coord.replace("°", " ").replace("'", " ").replace('"', " ").split()
            deg, min_, sec, direction = int(parts[0]), int(parts[1]), float(parts[2]), parts[3]
            decimal = deg + min_/60 + sec/3600
            return -decimal if direction in ["S", "W"] else decimal
        return float(coord)
    except:
        return None

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

@st.cache_data
def get_paginated_data(data, page, page_size):
    """Get paginated data slice efficiently"""
    start_idx = (page - 1) * page_size
    end_idx = min(start_idx + page_size, len(data))
    return data.iloc[start_idx:end_idx], start_idx + 1, end_idx

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
def calculate_pagination_info(total_items, page_size):
    """Calculate pagination information"""
    total_pages = math.ceil(total_items / page_size)
    return total_pages

def create_plant_cards_vectorized(paginated_data, source):
    """Create plant cards using vectorized operations instead of iterrows"""
    # Convert to list of dictionaries for faster iteration
    plant_data = paginated_data.to_dict('records')
    
    for plant in plant_data:
        if source in ["Steel Plants", "Steel Plants with BF"]:
            plant_name = plant.get('Plant Name', plant.get('Plant', 'Unknown'))
            capacity = plant.get('Capacity(MTPA)', 'N/A')
            furnace_type = plant.get('Furnance', plant.get('Furnace Type', 'N/A'))
            operational_status = plant.get('Operational', 'N/A')
            
            with st.expander(f"🏭 {plant_name}"):
                st.write(f"**Capacity:** {capacity} MTPA")
                st.write(f"**Furnace Type:** {furnace_type}")
                st.write(f"**Status:** {operational_status}")
                st.write(f"**State:** {plant.get('state', 'N/A')}")
                st.write(f"**District:** {plant.get('district', 'N/A')}")
                
        elif source == "Geocoded Companies":
            company_name = plant.get('Company_Name', 'Unknown')
            sales_revenue = plant.get('Sales_Revenue', 'N/A')
            city = plant.get('City', 'N/A')
            
            with st.expander(f"🏢 {company_name}"):
                st.write(f"**Sales Revenue:** {sales_revenue}")
                st.write(f"**City:** {city}")
                st.write(f"**State:** {plant.get('State', 'N/A')}")
                
        elif source == "Rice Mills":
            mill_name = plant.get('name', plant.get('Mill Name', 'Unknown'))
            address = plant.get('address', 'N/A')
            
            with st.expander(f"🌾 {mill_name}"):
                st.write(f"**Address:** {address}")
                st.write(f"**State:** {plant.get('state', 'N/A')}")
                st.write(f"**District:** {plant.get('district', 'N/A')}")

def get_or_init_session_state(source, default_page=1, default_page_size=10):
    """Get or initialize session state for pagination efficiently"""
    page_key = f"{source.replace(' ', '_').lower()}_current_page"
    size_key = f"{source.replace(' ', '_').lower()}_page_size"
    
    if page_key not in st.session_state:
        st.session_state[page_key] = default_page
    if size_key not in st.session_state:
        st.session_state[size_key] = default_page_size
    
    return page_key, size_key

@st.cache_data
def load_steel_plants_chunked(chunk_size=1000):
    """Load steel plants data in chunks for memory efficiency"""
    try:
        # Read entire Excel file first (Excel doesn't support chunksize)
        df = pd.read_excel("steel_plant_data.xlsx")
        
        # Process coordinates
        df["latitude"] = df["Latitude"].apply(convert_coordinate)
        df["longitude"] = df["Longitude"].apply(convert_coordinate)
        df = df.dropna(subset=["latitude", "longitude"])
        
        # Create chunks manually
        chunks = []
        for i in range(0, len(df), chunk_size):
            chunk = df.iloc[i:i + chunk_size].copy()
            chunks.append(chunk)
        
        # Combine all processed chunks
        if chunks:
            return pd.concat(chunks, ignore_index=True)
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading steel plants data in chunks: {str(e)}")
        return pd.DataFrame()

@st.cache_data
def load_geocoded_companies_chunked(chunk_size=1000):
    """Load geocoded companies data in chunks for memory efficiency"""
    try:
        # Read entire Excel file first (Excel doesn't support chunksize)
        df = pd.read_excel("geocoded_combined_companies.xlsx")
        
        # Clean up invalid coordinates
        df = df.dropna(subset=["Latitude", "Longitude"])
        df = df[(df["Latitude"].abs() <= 90) & (df["Longitude"].abs() <= 180)]
        
        # Create chunks manually
        chunks = []
        for i in range(0, len(df), chunk_size):
            chunk = df.iloc[i:i + chunk_size].copy()
            chunks.append(chunk)
        
        # Combine all processed chunks
        if chunks:
            return pd.concat(chunks, ignore_index=True)
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading geocoded companies data in chunks: {str(e)}")
        return pd.DataFrame()

@st.cache_data
def load_ricemill_data_chunked(chunk_size=1000):
    """Load rice mill data in chunks for memory efficiency"""
    try:
        # Read CSV file in chunks
        chunks = []
        for chunk in pd.read_csv("ricemills.csv", chunksize=chunk_size):
            # Clean up invalid coordinates for this chunk
            if "lat" in chunk.columns and "lng" in chunk.columns:
                chunk = chunk.dropna(subset=["lat", "lng"])
                chunk = chunk[(chunk["lat"].abs() <= 90) & (chunk["lng"].abs() <= 180)]
            chunks.append(chunk)
        
        # Combine all processed chunks
        if chunks:
            return pd.concat(chunks, ignore_index=True)
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading ricemill data in chunks: {str(e)}")
        return pd.DataFrame()

@st.cache_data
def load_geojson_chunked(geojson_file, max_features=5000):
    """Load GeoJSON data in chunks for memory efficiency"""
    try:
        with open(geojson_file) as f:
            geojson_data = json.load(f)
        
        # If GeoJSON has features and is too large, process in chunks
        if "features" in geojson_data and len(geojson_data["features"]) > max_features:
            # Create chunked version
            chunked_geojson = {
                "type": geojson_data.get("type", "FeatureCollection"),
                "features": geojson_data["features"][:max_features]  # Load first chunk
            }
            return chunked_geojson, True  # Return data and flag indicating it's chunked
        
        return geojson_data, False  # Return full data and flag indicating it's not chunked
    except Exception as e:
        st.error(f"Error loading GeoJSON file {geojson_file} in chunks: {str(e)}")
        return None, False

def get_data_chunk(data, chunk_number, chunk_size):
    """Get a specific chunk of data for progressive loading"""
    start_idx = chunk_number * chunk_size
    end_idx = start_idx + chunk_size
    return data.iloc[start_idx:end_idx]

@st.cache_data
def get_data_info(file_path):
    """Get basic information about data file without loading full data"""
    try:
        if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            # Get Excel file info
            with pd.ExcelFile(file_path) as excel_file:
                sheet_name = excel_file.sheet_names[0]
                # Read just first few rows to get columns
                sample_df = pd.read_excel(file_path, nrows=1)
                return {
                    'columns': list(sample_df.columns),
                    'sheet_count': len(excel_file.sheet_names),
                    'file_type': 'excel'
                }
        elif file_path.endswith('.csv'):
            # Get CSV file info
            sample_df = pd.read_csv(file_path, nrows=1)
            return {
                'columns': list(sample_df.columns),
                'file_type': 'csv'
            }
        elif file_path.endswith('.geojson'):
            # Get GeoJSON file info
            with open(file_path) as f:
                geojson_data = json.load(f)
            feature_count = len(geojson_data.get('features', []))
            return {
                'feature_count': feature_count,
                'type': geojson_data.get('type', 'FeatureCollection'),
                'file_type': 'geojson'
            }
    except Exception as e:
        return {'error': str(e)}

@st.cache_data
def load_data_progressively(file_path, page=1, page_size=1000):
    """Load data progressively for large datasets"""
    try:
        if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            # Load Excel data progressively
            skip_rows = (page - 1) * page_size
            df = pd.read_excel(file_path, skiprows=skip_rows, nrows=page_size)
            return df, len(df) == page_size  # Return data and has_more flag
        elif file_path.endswith('.csv'):
            # Load CSV data progressively
            skip_rows = (page - 1) * page_size
            df = pd.read_csv(file_path, skiprows=skip_rows, nrows=page_size)
            return df, len(df) == page_size  # Return data and has_more flag
        else:
            return pd.DataFrame(), False
    except Exception as e:
        st.error(f"Error loading data progressively from {file_path}: {str(e)}")
        return pd.DataFrame(), False

def create_lazy_loader(source_type, file_path, total_records=None):
    """Create a lazy loader for large datasets"""
    class LazyDataLoader:
        def __init__(self, source_type, file_path, total_records=None):
            self.source_type = source_type
            self.file_path = file_path
            self.total_records = total_records
            self.current_page = 1
            self.page_size = 1000
            self.cache = {}
            
        def get_page(self, page_number):
            """Get a specific page of data with caching"""
            if page_number in self.cache:
                return self.cache[page_number]
            
            data, has_more = load_data_progressively(
                self.file_path, page_number, self.page_size
            )
            
            # Process the data (add source_type, clean coordinates, etc.)
            if not data.empty:
                data = data.copy()
                data["source_type"] = self.source_type
                
                # Apply coordinate processing based on source type
                if self.source_type in ["Steel Plants", "Steel Plants with BF"]:
                    if "Latitude" in data.columns and "Longitude" in data.columns:
                        data["latitude"] = data["Latitude"].apply(convert_coordinate)
                        data["longitude"] = data["Longitude"].apply(convert_coordinate)
                        data = data.dropna(subset=["latitude", "longitude"])
                elif self.source_type == "Rice Mills":
                    if "lat" in data.columns and "lng" in data.columns:
                        data = data.dropna(subset=["lat", "lng"])
                        data = data[(data["lat"].abs() <= 90) & (data["lng"].abs() <= 180)]
                elif self.source_type == "Geocoded Companies":
                    if "Latitude" in data.columns and "Longitude" in data.columns:
                        data = data.dropna(subset=["Latitude", "Longitude"])
                        data = data[(data["Latitude"].abs() <= 90) & (data["Longitude"].abs() <= 180)]
            
            # Cache the processed data
            self.cache[page_number] = data
            return data
        
        def get_total_pages(self):
            """Estimate total pages based on total records or file info"""
            if self.total_records:
                return math.ceil(self.total_records / self.page_size)
            else:
                # Get file info to estimate size
                file_info = get_data_info(self.file_path)
                if 'error' not in file_info:
                    # Estimate based on typical record sizes
                    if file_info['file_type'] == 'excel':
                        # Excel files typically have 1000-5000 rows per sheet
                        estimated_rows = 2000
                    elif file_info['file_type'] == 'csv':
                        # CSV files can be larger, estimate conservatively
                        estimated_rows = 5000
                    else:
                        estimated_rows = 1000
                    return math.ceil(estimated_rows / self.page_size)
                return 1
    
    return LazyDataLoader(source_type, file_path, total_records)

@st.cache_data
def get_optimized_page_data(data, page, page_size, source_type):
    """Get optimized page data with memory-efficient processing"""
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    # Use iloc for efficient slicing
    page_data = data.iloc[start_idx:end_idx].copy()
    
    # Apply memory-efficient processing
    if source_type in ["Steel Plants", "Steel Plants with BF"]:
        # Only process coordinates for this page
        if "Latitude" in page_data.columns and "Longitude" in page_data.columns:
            page_data["latitude"] = page_data["Latitude"].apply(convert_coordinate)
            page_data["longitude"] = page_data["Longitude"].apply(convert_coordinate)
            page_data = page_data.dropna(subset=["latitude", "longitude"])
    elif source_type == "Rice Mills":
        if "lat" in page_data.columns and "lng" in page_data.columns:
            page_data = page_data.dropna(subset=["lat", "lng"])
            page_data = page_data[(page_data["lat"].abs() <= 90) & (page_data["lng"].abs() <= 180)]
    elif source_type == "Geocoded Companies":
        if "Latitude" in page_data.columns and "Longitude" in page_data.columns:
            page_data = page_data.dropna(subset=["Latitude", "Longitude"])
            page_data = page_data[(page_data["Latitude"].abs() <= 90) & (page_data["Longitude"].abs() <= 180)]
    
    return page_data, start_idx, end_idx

@st.cache_data
def memory_efficient_filter(data, filters):
    """Apply filters in a memory-efficient way"""
    filtered_data = data.copy()
    
    for filter_key, filter_values in filters.items():
        if filter_values and filter_key in filtered_data.columns:
            # Use isin() for efficient filtering
            if isinstance(filter_values, list):
                filtered_data = filtered_data[filtered_data[filter_key].isin(filter_values)]
            else:
                # Single value filter
                filtered_data = filtered_data[filtered_data[filter_key] == filter_values]
    
    return filtered_data

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
    
    # Convert float64 to float32 where precision allows
    for col in optimized_df.select_dtypes(include=['float64']).columns:
        optimized_df[col] = optimized_df[col].astype('float32')
    
    return optimized_df

def create_memory_efficient_chunks(data, chunk_size=1000):
    """Create memory-efficient chunks of data"""
    total_rows = len(data)
    chunks = []
    
    for i in range(0, total_rows, chunk_size):
        chunk = data.iloc[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks

def process_chunk_in_memory(chunk, processing_functions):
    """Process a single chunk with minimal memory overhead"""
    processed_chunk = chunk.copy()
    
    for func_name, func_args in processing_functions.items():
        if func_name == 'convert_coordinates':
            if "Latitude" in processed_chunk.columns and "longitude" not in processed_chunk.columns:
                processed_chunk["longitude"] = processed_chunk["Longitude"]
            if "Latitude" in processed_chunk.columns and "latitude" not in processed_chunk.columns:
                processed_chunk["latitude"] = processed_chunk["Latitude"]
            if "latitude" in processed_chunk.columns and "Longitude" in processed_chunk.columns:
                processed_chunk["latitude"] = processed_chunk["Latitude"].apply(convert_coordinate)
                processed_chunk["longitude"] = processed_chunk["Longitude"].apply(convert_coordinate)
                processed_chunk = processed_chunk.dropna(subset=["latitude", "longitude"])
        elif func_name == 'clean_coordinates':
            if "lat" in processed_chunk.columns and "lng" in processed_chunk.columns:
                processed_chunk = processed_chunk.dropna(subset=["lat", "lng"])
                processed_chunk = processed_chunk[(processed_chunk["lat"].abs() <= 90) & (processed_chunk["lng"].abs() <= 180)]
        elif func_name == 'add_source_type':
            processed_chunk["source_type"] = func_args
        elif func_name == 'normalize_columns':
            # Normalize column names
            for old_col, new_col in func_args.items():
                if old_col in processed_chunk.columns and new_col not in processed_chunk.columns:
                    processed_chunk[new_col] = processed_chunk[old_col]
    
    return processed_chunk

def get_memory_usage_info():
    """Get memory usage information for the app"""
    try:
        import psutil
        import sys
        
        # Get process memory info
        process = psutil.Process()
        memory_info = process.memory_info()
        
        # Get system memory info
        system_memory = psutil.virtual_memory()
        
        return {
            'process_rss_mb': memory_info.rss / 1024 / 1024,
            'process_vms_mb': memory_info.vms / 1024 / 1024,
            'system_total_mb': system_memory.total / 1024 / 1024,
            'system_available_mb': system_memory.available / 1024 / 1024,
            'system_percent_used': system_memory.percent
        }
    except ImportError:
        # psutil not available, return basic info
        return {
            'process_rss_mb': 0,
            'process_vms_mb': 0,
            'system_total_mb': 0,
            'system_available_mb': 0,
            'system_percent_used': 0
        }

def cleanup_session_state():
    """Clean up session state to prevent memory bloat"""
    keys_to_remove = []
    
    for key in st.session_state.keys():
        # Remove large data objects that are no longer needed
        if key.endswith('_data') or key.endswith('_chunk'):
            keys_to_remove.append(key)
        # Remove old pagination state for sources not currently active
        elif key.endswith('_current_page') or key.endswith('_page_size'):
            # Keep only recent pagination state
            if key not in [f"{source.replace(' ', '_').lower()}_current_page" for source in ["Steel Plants", "Steel Plants with BF", "Geocoded Companies", "Rice Mills"]]:
                keys_to_remove.append(key)
    
    for key in keys_to_remove:
        if key in st.session_state:
            del st.session_state[key]
    
    return len(keys_to_remove)

geojson_metadata = {
    "enhanced_lantanapresence.geojson": {
        "source": "Research Paper",
        "external_link": "https://doi.org/10.1016/j.gecco.2020.e01080",
        "recorded_time": "2020",
        "description": "This layer shows Lantana camara presence clusters extracted from satellite NDVI and field survey data in India.",
        "image_path": "lantana.png",
        "original": "lantanapresence.geojson"
    },
    "enhanced_juliflora.geojson": {
        "source": "Manual published by CAZRI, Jodhpur & HDRA, Coventry",
        "external_link": "https://www.researchgate.net/publication/244993994_Managing_Prosopis_juliflora_A_Technical_Manual",
        "recorded_time": "2001",
        "description": "These dots show distribution of juliflora across Indian Map",
        "image_path": "juliflora.png",
        "original": "juliflora.geojson"
    },
    "enhanced_juliflorapdf.geojson": {
        "source": "Manual published by CAZRI, Jodhpur & HDRA, Coventry",
        "external_link": "https://www.researchgate.net/publication/244993994_Managing_Prosopis_juliflora_A_Technical_Manual",
        "recorded_time": "2001",
        "description": "Juliflora distribution extracted from PDF source",
        "image_path": "juliflora.png",
        "original": "juliflorapdf.geojson"
    },
    "enhanced_cottonstalk.geojson": {
        "source": "Bhuvan Jaivoorja (ISRO)",
        "external_link": "https://bhuvan-app1.nrsc.gov.in/bioenergy/index.php",
        "recorded_time": "2016",
        "description": "Surplus Cotton Biomass shown in this layer.",
        "image_path": "Cotton.png",
        "original": "cottonstalk.geojson"
    },
    "enhanced_sugarcane.geojson": {
        "source": "Bhuvan Jaivoorja (ISRO)",
        "external_link": "https://bhuvan-app1.nrsc.gov.in/bioenergy/index.php",
        "recorded_time": "2016",
        "description": "Surplus Sugarcane Biomass shown in this layer.",
        "image_path": "sugarcane.png",
        "original": "sugarcane.geojson"
    },
    "enhanced_maize.geojson": {
        "source": "ICRISAT",
        "external_link": "https://oar.icrisat.org/10759/1/maize%20yield%20India.pdf",
        "recorded_time": "2018",
        "description": "Major districts of maize in India with area sown.",
        "image_path": "Maize.png",
        "original": "maize.geojson"
    },
    "enhanced_bamboo.geojson": {
        "source": "Zenodo Dataset",
        "external_link": "https://doi.org/10.5281/zenodo.14671750",
        "recorded_time": "2025",
        "description": "Shows the Bamboo presence.",
        "image_path": "bamboo.png",
        "original": "bamboo.geojson"
    }
}

if section == "Dashboard":
    st.title("Biochar Cluster Map with Industrial Data and GeoJSON Overlays")
    

    # Multi-select for data sources
    data_sources = st.multiselect(
        "Select Data Sources:",
        ["Steel Plants", "Steel Plants with BF", "Geocoded Companies", "Rice Mills"],
        default=["Steel Plants"],
        help="Choose one or more data sources to visualize together."
    )

    # Load and tag all selected data sources with memory efficiency
    all_dfs = []
    for source in data_sources:
        if source == "Steel Plants":
            df = load_steel_plants_chunked()
            df["source_type"] = "Steel Plants"
        elif source == "Steel Plants with BF":
            from steel_plant_bf_loader import load_steel_plants_bf
            df = load_steel_plants_bf()
            df["source_type"] = "Steel Plants with BF"
        elif source == "Geocoded Companies":
            df = load_geocoded_companies_chunked()
            df["source_type"] = "Geocoded Companies"
        elif source == "Rice Mills":
            df = load_ricemill_data_chunked()
            df["source_type"] = "Rice Mills"
        else:
            continue
        
        # Apply memory optimization to the loaded data
        df = optimize_dataframe_memory(df)
        
        # Normalize columns for each df
        # Create state column if it doesn't exist
        if "state" not in df.columns:
            if "State" in df.columns:
                df["state"] = df["State"]
            elif "detailed_state" in df.columns:
                df["state"] = df["detailed_state"]
            elif "State" in df.columns:
                df["state"] = df["State"]
            else:
                # Create empty state column if none exists
                df["state"] = "Unknown"
        
        # Create district column if it doesn't exist
        if "district" not in df.columns:
            if "District" in df.columns:
                df["district"] = df["District"]
            elif "detailed_district" in df.columns:
                df["district"] = df["detailed_district"]
            elif "address" in df.columns:
                df["district"] = df["address"].apply(lambda x: x.split(",")[-2].strip() if isinstance(x, str) and "," in x else "Unknown")
            else:
                # Create empty district column if none exists
                df["district"] = "Unknown"
        
        # Create uppercase versions for backward compatibility
        if "State" not in df.columns:
            df["State"] = df["state"]
        if "District" not in df.columns:
            df["District"] = df["district"]
        
        # Normalize plant name columns
        if "Plant Name" in df.columns and "Plant" not in df.columns:
            df["Plant"] = df["Plant Name"]
        if "Plant" in df.columns and "Plant Name" not in df.columns:
            df["Plant Name"] = df["Plant"]
        
        # Ensure latitude/longitude are numeric
        if "Latitude" in df.columns and "latitude" not in df.columns:
            df["latitude"] = df["Latitude"]
        if "latitude" in df.columns and "Latitude" not in df.columns:
            df["Latitude"] = df["latitude"]
        if "Longitude" in df.columns and "longitude" not in df.columns:
            df["longitude"] = df["Longitude"]
        if "longitude" in df.columns and "Longitude" not in df.columns:
            df["Longitude"] = df["longitude"]
        all_dfs.append(df)

    if not all_dfs:
        st.warning("No data sources selected.")
        st.stop()

    # Concatenate all selected data with memory optimization
    plants = pd.concat(all_dfs, ignore_index=True)
    plants = optimize_dataframe_memory(plants)
    
    # Add memory monitoring
    with st.expander("💾 Memory Usage Info"):
        memory_info = get_memory_usage_info()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Process Memory", f"{memory_info['process_rss_mb']:.1f} MB")
        with col2:
            st.metric("System Memory Used", f"{memory_info['system_percent_used']:.1f}%")
        with col3:
            st.metric("System Available", f"{memory_info['system_available_mb']:.1f} MB")
        
        if st.button("🧹 Clean Up Memory"):
            cleaned_count = cleanup_session_state()
            st.success(f"Cleaned up {cleaned_count} session state items")
            # Force garbage collection
            import gc
            gc.collect()
            st.rerun()

    with st.expander("Data Debug Info"):
        st.write(f"Loaded {len(plants)} records from {', '.join(data_sources)}")
        
        # Fix categorical columns that might cause pyarrow issues
        if 'zip' in plants.columns and plants['zip'].dtype.name == 'category':
            plants['zip'] = plants['zip'].astype('object')
        
        # Also fix any other categorical columns that might contain problematic values
        for col in plants.select_dtypes(include=['category']).columns:
            # Check if column contains values that might cause issues
            try:
                # Try to convert a sample to see if it causes issues
                sample = plants[col].dropna().head(1)
                if len(sample) > 0:
                    # If conversion fails, convert back to object
                    pd.to_numeric(sample, errors='raise')
            except:
                plants[col] = plants[col].astype('object')
        
        st.dataframe(plants)
        invalid_coords = pd.DataFrame()
        for source in data_sources:
            if source in ["Steel Plants", "Steel Plants with BF"]:
                # Ensure latitude/longitude are numeric
                lat = pd.to_numeric(plants["latitude"], errors="coerce") if "latitude" in plants.columns else pd.Series(dtype=float)
                lon = pd.to_numeric(plants["longitude"], errors="coerce") if "longitude" in plants.columns else pd.Series(dtype=float)
                mask = (plants["source_type"] == source)
                invalid_coords = pd.concat([
                    invalid_coords,
                    plants[mask & ((lat.abs() > 90) | (lon.abs() > 180))]
                ])
            elif source == "Rice Mills":
                if "lat" in plants.columns and "lng" in plants.columns:
                    lat = pd.to_numeric(plants["lat"], errors="coerce")
                    lng = pd.to_numeric(plants["lng"], errors="coerce")
                    mask = (plants["source_type"] == source)
                    invalid_coords = pd.concat([
                        invalid_coords,
                        plants[mask & ((lat.abs() > 90) | (lng.abs() > 180))]
                    ])
            elif source == "Geocoded Companies":
                # Ensure Latitude/Longitude are numeric
                lat = pd.to_numeric(plants["Latitude"], errors="coerce") if "Latitude" in plants.columns else pd.Series(dtype=float)
                lon = pd.to_numeric(plants["Longitude"], errors="coerce") if "Longitude" in plants.columns else pd.Series(dtype=float)
                mask = (plants["source_type"] == source)
                invalid_coords = pd.concat([
                    invalid_coords,
                    plants[mask & ((lat.abs() > 90) | (lon.abs() > 180))]
                ])
        if not invalid_coords.empty:
            st.warning(f"Found {len(invalid_coords)} records with invalid coordinates:")
            st.dataframe(invalid_coords)

    # --- FILTER WIDGETS ---
    st.markdown(f"#### 🔍 Filter Data (applies to all selected sources)")
    name_filter = st.text_input("Search Name (Plant/Company/Rice Mill)")
    
    # State filter - only show if state column exists
    if "state" in plants.columns:
        state_filter = st.multiselect("State", options=plants["state"].dropna().unique())
    else:
        state_filter = []
        st.warning("State column not found in data")
    
    # District filter - only show if district column exists
    if "district" in plants.columns:
        district_filter = st.multiselect("District", options=plants["district"].dropna().unique())
    else:
        district_filter = []
        st.warning("District column not found in data")
    
    # Operational Status Filter - only show if data contains operational status
    operational_status_col = None
    for col in ["Operational", "Operational Status", "Status"]:
        if col in plants.columns:
            operational_status_col = col
            break
    
    if operational_status_col:
        # Get unique operational status values, excluding NaN
        operational_statuses = plants[operational_status_col].dropna().unique()
        if len(operational_statuses) > 0:
            operational_status_filter = st.multiselect(
                "Operational Status", 
                options=operational_statuses,
                help="Filter by operational status (e.g., Active, Not in production)"
            )
        else:
            operational_status_filter = []
    else:
        operational_status_filter = []
    
    # Furnace Type Filter - only show if data contains furnace type
    furnace_type_col = None
    for col in ["Furnance", "Furnace Type", "Furnace_Type"]:
        if col in plants.columns:
            furnace_type_col = col
            break
    
    if furnace_type_col:
        # Extract unique furnace types from combinations
        unique_furnace_types = set()
        furnace_types_raw = plants[furnace_type_col].dropna()
        
        for furnace_combo in furnace_types_raw:
            if pd.notna(furnace_combo):
                # Split by comma and clean each type
                types = [str(t).strip() for t in str(furnace_combo).split(',')]
                unique_furnace_types.update(types)
        
        # Remove empty strings and sort
        unique_furnace_types = [t for t in sorted(unique_furnace_types) if t]
        
        if len(unique_furnace_types) > 0:
            furnace_type_filter = st.multiselect(
                "Furnace Type", 
                options=unique_furnace_types,
                help="Select furnace types (e.g., BF, IF, DRI, etc.)"
            )
        else:
            furnace_type_filter = []
    else:
        furnace_type_filter = []

    # Apply filters using memory-efficient filtering
    filters = {}
    if state_filter:
        filters['state'] = state_filter
    if district_filter:
        filters['district'] = district_filter
    if name_filter:
        # Apply name filter separately as it requires string matching
        name_mask = plants['Plant Name'].str.contains(name_filter, case=False, na=False) | \
                   plants['Plant'].str.contains(name_filter, case=False, na=False)
        filtered_plants = plants[name_mask]
    else:
        filtered_plants = plants
    
    # Apply other filters using memory-efficient function
    if filters:
        filtered_plants = memory_efficient_filter(filtered_plants, filters)
    
    # Apply additional filters (operational status and furnace type)
    if operational_status_filter and operational_status_col:
        filtered_plants = filtered_plants[filtered_plants[operational_status_col].isin(operational_status_filter)]
    if furnace_type_filter and furnace_type_col:
        # Create mask for plants that have any of the selected furnace types
        furnace_mask = pd.Series([False]*len(filtered_plants))
        for selected_type in furnace_type_filter:
            # Check if selected type is present in the furnace combination
            furnace_mask = furnace_mask | filtered_plants[furnace_type_col].astype(str).str.contains(
                f'\b{re.escape(selected_type)}\b', case=False, na=False
            )
        filtered_plants = filtered_plants[furnace_mask]
    
    # Optimize memory for filtered data
    if not filtered_plants.empty:
        filtered_plants = optimize_dataframe_memory(filtered_plants)

    # --- DISPLAY SEARCH RESULTS ---
    if name_filter and not filtered_plants.empty:
        st.markdown("---")
        st.markdown(f"#### ℹ️ Details for Found Results")
        for source in data_sources:
            df = filtered_plants[filtered_plants['source_type'] == source]
            if df.empty:
                continue
            for index, row in df.iterrows():
                if source == "Steel Plants":
                    with st.expander(f"{row['Plant Name']}"):
                        st.write(f"**Capacity (MTPA):** {row.get('Capacity(MTPA)', 'N/A')}")
                        st.write(f"**Furnace Type:** {row.get('Furnance', 'N/A')}")
                        st.write(f"**Operational Status:** {row.get('Operational', 'N/A')}")
                        source_url = row.get('Source')
                        if isinstance(source_url, str) and source_url.startswith('http'):
                            st.markdown(f"**Source:** <a href='{source_url}' target='_blank'>Visit Link</a>", unsafe_allow_html=True)
                        else:
                            st.write(f"**Source:** {source_url if pd.notna(source_url) else 'N/A'}")
                elif source == "Steel Plants with BF":
                    plant_name = row.get('Plant') if 'Plant' in row else row.get('Plant Name', 'Unknown Plant')
                    with st.expander(f"{plant_name}"):
                        st.write(f"**Blast Furnace Capacity:** {row.get('Quantity', 'N/A')} Mtpa")
                        st.write(f"**State:** {row.get('State', 'N/A')}")
                        st.write(f"**District:** {row.get('District', 'N/A')}")
                elif source == "Rice Mills":
                    with st.expander(f"{row['name']}"):
                        st.write(f"**Address:** {row.get('address', 'N/A')}")
                        st.write(f"**Phone:** {row.get('phone', 'N/A')}")
                        st.write(f"**Email:** {row.get('email', 'N/A')}")
                        st.write(f"**State:** {row.get('state', 'N/A')}")
                        st.write(f"**Country:** {row.get('country', 'N/A')}")
                        st.write(f"**ZIP:** {row.get('zip', 'N/A')}")
                        st.write(f"**Rating:** {row.get('star_count', 'N/A')} ({row.get('rating_count', 'N/A')} reviews)")
                        st.write(f"**Category:** {row.get('primary_category_name', 'N/A')}")
                        website_url = row.get('url')
                        if isinstance(website_url, str) and website_url.startswith('http'):
                            st.markdown(f"**Website:** <a href='{website_url}' target='_blank'>Visit Site</a>", unsafe_allow_html=True)
                        else:
                            st.write(f"**Website:** {website_url if pd.notna(website_url) else 'N/A'}")
                        social_links = []
                        if pd.notna(row.get('facebook_link')) and row.get('facebook_link').startswith('http'):
                            social_links.append(f"<a href='{row['facebook_link']}' target='_blank'>Facebook</a>")
                        if pd.notna(row.get('instagram_link')) and row.get('instagram_link').startswith('http'):
                            social_links.append(f"<a href='{row['instagram_link']}' target='_blank'>Instagram</a>")
                        if pd.notna(row.get('twitter_link')) and row.get('twitter_link').startswith('http'):
                            social_links.append(f"<a href='{row['twitter_link']}' target='_blank'>Twitter</a>")
                        if pd.notna(row.get('linkedin_link')) and row.get('linkedin_link').startswith('http'):
                            social_links.append(f"<a href='{row['linkedin_link']}' target='_blank'>LinkedIn</a>")
                        if pd.notna(row.get('youtube_link')) and row.get('youtube_link').startswith('http'):
                            social_links.append(f"<a href='{row['youtube_link']}' target='_blank'>YouTube</a>")
                        if pd.notna(row.get('whatsapp_link')) and row.get('whatsapp_link').startswith('http'):
                            social_links.append(f"<a href='{row['whatsapp_link']}' target='_blank'>WhatsApp</a>")
                        if pd.notna(row.get('tiktok_link')) and row.get('tiktok_link').startswith('http'):
                            social_links.append(f"<a href='{row['tiktok_link']}' target='_blank'>TikTok</a>")
                        if social_links:
                            st.markdown(f"**Social Media:** {' | '.join(social_links)}", unsafe_allow_html=True)
                elif source == "Geocoded Companies":
                    with st.expander(f"{row['Company_Name']}"):
                        st.write(f"**Sales Revenue:** {row.get('Sales_Revenue', 'N/A')}")
                        st.write(f"**City:** {row.get('City', 'N/A')}")
                        st.write(f"**State:** {row.get('State', 'N/A')}")
                        st.write(f"**Country:** {row.get('Country', 'N/A')}")
                        company_url = row.get('Company_URL')
                        if isinstance(company_url, str) and company_url.startswith('http'):
                            st.markdown(f"**Website:** <a href='{company_url}' target='_blank'>Visit Site</a>", unsafe_allow_html=True)
                        else:
                            st.write(f"**Website:** {company_url if pd.notna(company_url) else 'N/A'}")
        st.markdown("---")

    # Multiple selection for primary GeoJSON overlays
    selected_geojson_files = st.multiselect(
        "Select Primary GeoJSON Overlays:", 
        list(geojson_metadata.keys()),
        default=[],
        key="primary_geojson_overlays"
    )

    def show_metadata_and_image(geojson_file):
        meta = geojson_metadata.get(geojson_file, {})
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"#### ℹ️ Metadata for {geojson_file}")
            st.markdown(f"**Description:** {meta.get('description', 'N/A')}")
            st.markdown(f"**Source_link:** [Visit site]({meta.get('external_link', '#')})")
            st.markdown(f"**Recorded Time:** {meta.get('recorded_time', 'Unknown')}")
            st.markdown(f"**Source:** {meta.get('source', 'Unknown')}")
            
            # Offer download of the original GeoJSON file (without precomputed data)
            original_file = meta.get("original", geojson_file.replace("enhanced_", ""))
            if os.path.exists(original_file):
                with open(original_file, "r") as f:
                    geojson_text = f.read()
                st.download_button(f"Download Original {original_file}", geojson_text, file_name=original_file, mime="application/json")
            
            # Also offer the enhanced version for advanced users
            if os.path.exists(geojson_file):
                with open(geojson_file, "r") as f:
                    enhanced_text = f.read()
                st.download_button(f"Download Enhanced {geojson_file}", enhanced_text, file_name=geojson_file, mime="application/json")
                
        with col2:
            if os.path.exists(meta.get("image_path", "")):
                st.image(meta["image_path"], caption="Source Reference Map", use_column_width=True)

    # Show metadata for all selected GeoJSON files
    for geojson_file in selected_geojson_files:
        show_metadata_and_image(geojson_file)

    if not filtered_plants.empty:
        # Show count summary for all selected sources
        filter_info = ""
        if district_filter:
            if len(district_filter) == 1:
                filter_info = f" in {district_filter[0]} district"
            else:
                filter_info = f" in {len(district_filter)} districts"
        elif state_filter:
            if len(state_filter) == 1:
                filter_info = f" in {state_filter[0]} state"
            else:
                filter_info = f" in {len(state_filter)} states"
        if not filter_info:
            filter_info = " matching your criteria"
        st.info(f"Showing {len(filtered_plants)} records from {', '.join(data_sources)}{filter_info}.")

        # Show total capacity for Steel Plants with BF if present
        if "Steel Plants with BF" in data_sources and "Quantity" in filtered_plants.columns:
            total_capacity = filtered_plants[filtered_plants["source_type"] == "Steel Plants with BF"]["Quantity"].sum()
            st.markdown(f"<div style='background-color: #e6f3ff; padding: 10px; border-radius: 5px; margin-bottom: 10px;'><b>Total Blast Furnace Capacity (Steel Plants with BF):</b> {total_capacity:.2f} Mtpa</div>", unsafe_allow_html=True)

        # Plot all selected sources together, color by source_type
        color_map = {
            "Steel Plants": "purple",
            "Steel Plants with BF": "red",
            "Geocoded Companies": "green",
            "Rice Mills": "orange"
        }
        import plotly.graph_objects as go
        fig = go.Figure()
        for source in data_sources:
            df = filtered_plants[filtered_plants["source_type"] == source]
            if df.empty:
                continue
            if source in ["Steel Plants", "Steel Plants with BF"]:
                lat_col, lon_col = "latitude", "longitude"
                hover_name_col = "Plant Name" if "Plant Name" in df.columns else "Plant"
            elif source == "Rice Mills":
                lat_col, lon_col = "lat", "lng"
                hover_name_col = "name"
            else:  # Geocoded Companies
                lat_col, lon_col = "Latitude", "Longitude"
                hover_name_col = "Company_Name"
            if lat_col not in df.columns or lon_col not in df.columns:
                continue
            # Ensure lat/lon columns are float for Arrow compatibility
            df = df.copy()
            df[lat_col] = pd.to_numeric(df[lat_col], errors="coerce")
            df[lon_col] = pd.to_numeric(df[lon_col], errors="coerce")
            # Generate hover texts using cached function
            hover_texts = generate_hover_texts(df, source, hover_name_col)
            fig.add_trace(go.Scattermapbox(
                lat=df[lat_col],
                lon=df[lon_col],
                mode="markers",
                marker=dict(size=8, color=color_map.get(source, "gray")),
                name=source,
                text=hover_texts,
                hoverinfo="text"
            ))

        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_center={"lat": 20.5937, "lon": 78.9629},
            mapbox_zoom=4,
            height=500,
            margin={"r":0,"t":0,"l":0,"b":0}
        )

        # Define colors for multiple overlays
        base_colors = [
            "rgba(255, 165, 0, 0.5)",  # Orange
            "rgba(0, 128, 255, 0.5)",   # Blue
            "rgba(255, 0, 128, 0.5)",   # Pink
            "rgba(0, 255, 128, 0.5)",   # Green
            "rgba(128, 0, 255, 0.5)",   # Purple
            "rgba(255, 128, 0, 0.5)",   # Dark Orange
        ]
        
        # Create overlay colors dictionary for selected files
        overlay_colors = {}
        for i, geojson_file in enumerate(selected_geojson_files):
            overlay_colors[geojson_file] = base_colors[i % len(base_colors)]

        # Add polygons/overlays for all selected GeoJSON files
        for geojson_file in selected_geojson_files:
            if os.path.exists(geojson_file):
                # Use chunked GeoJSON loading
                geojson_data, is_chunked = load_geojson_chunked(geojson_file)
                if geojson_data is None:
                    continue
                
                # Show warning if data was chunked
                if is_chunked:
                    st.warning(f"Large GeoJSON file detected: {geojson_file}. Loading first 5000 features for performance.")
                
                overlay_color = overlay_colors.get(geojson_file, "rgba(0,0,0,0.5)")
                fill_color = overlay_color.replace("0.5", "0.2")
                line_color = overlay_color.replace("0.5", "0.8")
                for feature in geojson_data["features"]:
                    geom_type = feature["geometry"]["type"]
                    coords = feature["geometry"]["coordinates"]
                    if not coords or (isinstance(coords, list) and len(coords) == 0):
                        continue
                    try:
                        if geom_type == "Polygon":
                            polygon_coords = coords[0]
                            if not polygon_coords:
                                continue
                            lons, lats = zip(*polygon_coords)
                            tooltip_text = f"<b>Polygon Information</b><br>"
                            feature_props = feature.get("properties", {})
                            districts = feature_props.get("districts", [])
                            states = feature_props.get("states", [])
                            if districts:
                                tooltip_text += f"Districts: {', '.join(districts)}<br>"
                            if states:
                                tooltip_text += f"States: {', '.join(states)}"
                            if not districts and not states:
                                tooltip_text = "Polygon area (location data unavailable)"
                            fig.add_trace(go.Scattermapbox(
                                lat=list(lats),
                                lon=list(lons),
                                fill="toself",
                                fillcolor=fill_color,
                                line=dict(color=line_color, width=2),
                                mode="lines",
                                name=f"Polygon ({geojson_file})",
                                hovertext=tooltip_text,
                                hoverinfo="text",
                                showlegend=False
                            ))
                        elif geom_type == "Point":
                            lon, lat = coords
                            feature_props = feature.get("properties", {})
                            districts = feature_props.get("districts", [])
                            states = feature_props.get("states", [])
                            tooltip_text = ""
                            if districts:
                                tooltip_text += f"Districts: {', '.join(districts)}<br>"
                            if states:
                                tooltip_text += f"States: {', '.join(states)}"
                            if not tooltip_text:
                                tooltip_text = "Location data unavailable"
                            fig.add_trace(go.Scattermapbox(
                                lat=[lat],
                                lon=[lon],
                                mode="markers",
                                marker=dict(size=8, color=overlay_color),
                                name="GeoJSON Point",
                                hovertext=tooltip_text,
                                hoverinfo="text"
                            ))
                        elif geom_type == "MultiPolygon":
                            for i, poly_coords in enumerate(coords):
                                if not poly_coords or not poly_coords[0]:
                                    continue
                                lons, lats = zip(*poly_coords[0])
                                feature_props = feature.get("properties", {})
                                districts = feature_props.get("districts", [])
                                states = feature_props.get("states", [])
                                tooltip_text = f"<b>MultiPolygon Part {i+1}</b><br>"
                                if districts:
                                    tooltip_text += f"Districts: {', '.join(districts)}<br>"
                                if states:
                                    tooltip_text += f"States: {', '.join(states)}"
                                if not districts and not states:
                                    tooltip_text += "Location data unavailable"
                                fig.add_trace(go.Scattermapbox(
                                    lat=list(lats),
                                    lon=list(lons),
                                    fill="toself",
                                    fillcolor=fill_color,
                                    line=dict(color=line_color, width=2),
                                    mode="lines",
                                    name=f"MultiPolygon ({geojson_file})",
                                    hovertext=tooltip_text,
                                    hoverinfo="text",
                                    showlegend=False
                                ))
                    except Exception as e:
                        st.warning(f"⚠️ Skipped polygon: {e}")
        # Display the map
        st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})
        
        # --- SIDE PANEL: FILTERED PLANT LIST ---
        if not filtered_plants.empty:
            st.markdown("---")
            st.markdown(f"#### 📋 Filtered Plant List ({len(filtered_plants)} plants)")
            
            # Create columns for better layout
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # Use cached function to get source data efficiently
                source_data_dict = get_source_data_by_type(filtered_plants, data_sources)
                
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
                        # Use optimized vectorized function instead of iterrows
                        create_plant_cards_vectorized(paginated_data, source)
                    
                    # Add separator between data sources
                    st.markdown("---")
            
            with col2:
                # Summary statistics
                st.markdown("#### 📊 Summary")
                st.write(f"**Total Plants:** {len(filtered_plants)}")
                
                # Show counts by source type
                for source in data_sources:
                    count = len(filtered_plants[filtered_plants['source_type'] == source])
                    if count > 0:
                        st.write(f"**{source}:** {count}")
                
                # Show counts by state if state filter is applied
                if state_filter:
                    st.markdown("---")
                    st.markdown("**By State:**")
                    for state in state_filter:
                        state_count = len(filtered_plants[filtered_plants['state'] == state])
                        if state_count > 0:
                            st.write(f"**{state}:** {state_count}")
                
                # Show counts by operational status if available
                if 'Operational' in filtered_plants.columns:
                    st.markdown("---")
                    
                    # Get status counts
                    status_counts = filtered_plants['Operational'].value_counts()
                    total_count = len(filtered_plants[filtered_plants['Operational'].notna()])
                    
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
                    if col in filtered_plants.columns:
                        furnace_col = col
                        break
                
                if furnace_col:
                    st.markdown("---")
                    
                    # Get furnace type counts
                    furnace_counts = filtered_plants[furnace_col].value_counts()
                    total_count = len(filtered_plants[filtered_plants[furnace_col].notna()])
                    
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
    else:
        st.info("Map visualization not available - coordinate data missing.")

elif section == "Crop-Specific Data":
    st.title("🌾 Crop-Specific Biochar Resource Information")
    crop_selected = st.selectbox("Choose a Crop", ["Cotton", "Sugarcane", "Maize", "Juliflora", "Lantana","Bamboo"])

    pdf_map = {
        "Cotton": "cotton.pdf",
        "Sugarcane": "sugarcane.pdf",
        "Maize": "maize.pdf",
        "Juliflora": "Juliflora (1).pdf",
        "Lantana": "Lantana (1).pdf",
        "Bamboo": "bamboo.pdf",
    }

    if crop_selected in pdf_map and os.path.exists(pdf_map[crop_selected]):
        st.markdown(f"#### 📄 {crop_selected} Reference PDF")
        with open(pdf_map[crop_selected], "rb") as f:
            st.download_button(label=f"⬇️ Download {crop_selected} PDF", data=f.read(), file_name=pdf_map[crop_selected], mime="application/pdf")
        pdf_viewer(pdf_map[crop_selected])
    else:
        st.warning("No PDF available for this crop.")

######26Aug#####
