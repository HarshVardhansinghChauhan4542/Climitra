import pandas as pd
import json
import streamlit as st
import math

from src.utils.coordinate_utils import convert_coordinate
from src.data.metadata_loader import get_data_info

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
