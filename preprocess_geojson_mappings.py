#!/usr/bin/env python3
"""
Pre-process GeoJSON files to map polygons to districts and states.
This script calculates all spatial intersections beforehand and saves the results
so the Streamlit app can load them quickly without real-time calculations.
"""

import json
import os
import geopandas as gpd
from shapely.geometry import shape
import pandas as pd
from tqdm import tqdm

def load_boundaries():
    """Load India administrative boundaries"""
    try:
        states_file = "india_states.geojson"
        districts_file = "india_districts.geojson"
        
        if not os.path.exists(states_file) or not os.path.exists(districts_file):
            print("❌ Boundary files not found. Please ensure india_states.geojson and india_districts.geojson exist.")
            return gpd.GeoDataFrame()
            
        # Load boundaries
        states_gdf = gpd.read_file(states_file)
        districts_gdf = gpd.read_file(districts_file)
        
        # Combine and standardize
        states_gdf['boundary_type'] = 'state'
        districts_gdf['boundary_type'] = 'district'
        
        # Standardize column names
        if 'NAME_1' in states_gdf.columns:
            states_gdf['name'] = states_gdf['NAME_1']
        elif 'ST_NM' in states_gdf.columns:
            states_gdf['name'] = states_gdf['ST_NM']
        elif 'state' in states_gdf.columns:
            states_gdf['name'] = states_gdf['state']
            
        if 'NAME_2' in districts_gdf.columns:
            districts_gdf['name'] = districts_gdf['NAME_2']
        elif 'DISTRICT' in districts_gdf.columns:
            districts_gdf['name'] = districts_gdf['DISTRICT']
        elif 'district' in districts_gdf.columns:
            districts_gdf['name'] = districts_gdf['district']
            
        # Add state info to districts
        if 'NAME_1' in districts_gdf.columns:
            districts_gdf['state_name'] = districts_gdf['NAME_1']
        elif 'ST_NM' in districts_gdf.columns:
            districts_gdf['state_name'] = districts_gdf['ST_NM']
            
        # Select needed columns and combine
        states_clean = states_gdf[['name', 'boundary_type', 'geometry']].copy()
        districts_clean = districts_gdf[['name', 'boundary_type', 'geometry']].copy()
        if 'state_name' in districts_gdf.columns:
            districts_clean['state_name'] = districts_gdf['state_name']
        
        # Combine both GeoDataFrames
        combined_boundaries = pd.concat([states_clean, districts_clean], ignore_index=True)
        combined_gdf = gpd.GeoDataFrame(combined_boundaries)
        
        print(f"✅ Loaded {len(states_gdf)} states and {len(districts_gdf)} districts")
        return combined_gdf
        
    except Exception as e:
        print(f"❌ Error loading boundaries: {e}")
        return gpd.GeoDataFrame()

def get_intersected_regions(polygon, boundaries):
    """Get districts and states that intersect with polygon"""
    try:
        if boundaries.empty:
            return [], []
            
        # Ensure polygon is GeoDataFrame with correct CRS
        polygon_gdf = gpd.GeoDataFrame(geometry=[polygon], crs="EPSG:4326")
        
        # Ensure boundaries have same CRS
        if boundaries.crs != "EPSG:4326":
            boundaries = boundaries.to_crs("EPSG:4326")
        
        # Perform spatial intersection
        intersection = gpd.overlay(boundaries, polygon_gdf, how='intersection')
        
        districts = []
        states = []
        
        if not intersection.empty:
            # Get districts
            district_rows = intersection[intersection['boundary_type'] == 'district']
            if not district_rows.empty and 'name' in district_rows.columns:
                districts = district_rows['name'].dropna().unique().tolist()
            
            # Get states
            state_rows = intersection[intersection['boundary_type'] == 'state']
            if not state_rows.empty and 'name' in state_rows.columns:
                states = state_rows['name'].dropna().unique().tolist()
            
            # If no states found directly, try from district's state_name
            if not states and not district_rows.empty and 'state_name' in district_rows.columns:
                states = district_rows['state_name'].dropna().unique().tolist()
        
        return districts, states
        
    except Exception as e:
        print(f"⚠️ Spatial intersection failed: {e}")
        return [], []

def get_coordinate_fallback(polygon):
    """Fallback coordinate-based estimation"""
    try:
        centroid = polygon.centroid
        lat, lon = centroid.y, centroid.x
        
        # Simplified coordinate mapping for major states
        if 24.0 <= lat <= 30.2 and 69.5 <= lon <= 78.2:
            return ["Jodhpur", "Jaipur", "Bikaner"], ["Rajasthan"]
        elif 20.1 <= lat <= 24.7 and 68.2 <= lon <= 74.5:
            return ["Ahmedabad", "Rajkot", "Surat"], ["Gujarat"]
        elif 15.6 <= lat <= 22.0 and 72.6 <= lon <= 80.9:
            return ["Mumbai", "Pune", "Nagpur"], ["Maharashtra"]
        elif 11.5 <= lat <= 18.5 and 74.0 <= lon <= 78.6:
            return ["Bangalore", "Mysore", "Belgaum"], ["Karnataka"]
        elif 8.1 <= lat <= 13.6 and 76.2 <= lon <= 80.3:
            return ["Chennai", "Coimbatore", "Madurai"], ["Tamil Nadu"]
        elif 12.6 <= lat <= 19.9 and 76.8 <= lon <= 84.8:
            return ["Hyderabad", "Visakhapatnam"], ["Telangana", "Andhra Pradesh"]
        elif 8.2 <= lat <= 12.8 and 74.9 <= lon <= 77.4:
            return ["Kochi", "Thiruvananthapuram"], ["Kerala"]
        elif 21.5 <= lat <= 27.1 and 85.8 <= lon <= 89.9:
            return ["Kolkata", "Darjeeling"], ["West Bengal"]
        elif 17.8 <= lat <= 22.6 and 81.4 <= lon <= 87.5:
            return ["Bhubaneswar", "Cuttack"], ["Odisha"]
        elif 21.1 <= lat <= 26.9 and 74.0 <= lon <= 82.8:
            return ["Bhopal", "Indore", "Jabalpur"], ["Madhya Pradesh"]
        elif 23.9 <= lat <= 30.4 and 77.1 <= lon <= 84.6:
            return ["Lucknow", "Agra", "Varanasi"], ["Uttar Pradesh"]
        elif 29.5 <= lat <= 32.5 and 73.9 <= lon <= 76.9:
            return ["Amritsar", "Ludhiana"], ["Punjab"]
        elif 27.7 <= lat <= 30.9 and 74.5 <= lon <= 77.6:
            return ["Gurugram", "Faridabad"], ["Haryana"]
        else:
            return ["Unknown District"], ["Unknown State"]
    except:
        return ["Unknown District"], ["Unknown State"]

def process_geojson_file(filename, boundaries):
    """Process a single GeoJSON file and add district/state mappings"""
    try:
        print(f"\n🔄 Processing {filename}...")
        
        if not os.path.exists(filename):
            print(f"❌ File {filename} not found, skipping...")
            return
        
        # Load GeoJSON
        with open(filename, 'r') as f:
            geojson_data = json.load(f)
        
        processed_features = []
        total_features = len(geojson_data['features'])
        
        # Process each feature with progress bar
        for i, feature in enumerate(tqdm(geojson_data['features'], desc=f"Processing {filename}")):
            try:
                geometry = feature.get('geometry', {})
                if not geometry or not geometry.get('coordinates'):
                    continue
                
                # Convert to shapely polygon
                polygon = shape(geometry)
                
                if polygon.is_empty or not polygon.is_valid:
                    continue
                
                # Get districts and states
                districts, states = [], []
                method = "spatial_intersection"
                if not boundaries.empty:
                    districts, states = get_intersected_regions(polygon, boundaries)
                # Fallback if intersection fails (empty)
                if not districts and not states:
                    districts, states = get_coordinate_fallback(polygon)
                    method = "coordinate_estimation"
                
                # Add mapping to feature properties
                if 'properties' not in feature:
                    feature['properties'] = {}
                
                feature['properties']['districts'] = districts
                feature['properties']['states'] = states
                feature['properties']['mapping_method'] = method
                feature['properties']['feature_id'] = i
                
                processed_features.append(feature)
                
            except Exception as e:
                print(f"⚠️ Error processing feature {i} in {filename}: {e}")
                continue
        
        # Save enhanced GeoJSON (overwrite original with enhanced version)
        enhanced_geojson = {
            "type": "FeatureCollection",
            "features": processed_features
        }
        
        with open(filename, 'w') as f:
            json.dump(enhanced_geojson, f, indent=2)
        
        print(f"✅ Enhanced {filename} with {len(processed_features)} features (original file updated)")
        
        # Create summary mapping file
        summary = {}
        for i, feature in enumerate(processed_features):
            props = feature.get('properties', {})
            summary[i] = {
                'districts': props.get('districts', []),
                'states': props.get('states', []),
                'method': props.get('mapping_method', 'unknown')
            }
        
        summary_filename = f"mapping_{filename.replace('.geojson', '.json')}"
        with open(summary_filename, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✅ Saved mapping summary to {summary_filename}")
        
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

def main():
    """Main preprocessing function"""
    print("🚀 Starting GeoJSON preprocessing for fast Streamlit loading...")
    
    # Load boundaries
    print("\n📊 Loading India administrative boundaries...")
    boundaries = load_boundaries()
    
    # List of GeoJSON files to process
    geojson_files = [
        "lantanapresence.geojson",
        "juliflora.geojson", 
        "juliflorapdf.geojson",
        "cottonstalk.geojson",
        "sugarcane.geojson",
        "maize.geojson",
        "bamboo.geojson",
        "enhanced_juliflora.geojson"
    ]
    
    # Process each file
    for filename in geojson_files:
        if os.path.exists(filename):
            process_geojson_file(filename, boundaries)
        else:
            print(f"⚠️ File {filename} not found, skipping...")
    
    print("\n🎉 Preprocessing complete! Original GeoJSON files enhanced with district/state data.")
    print("📝 Files updated:")
    for filename in geojson_files:
        if os.path.exists(filename):
            mapping_file = f"mapping_{filename.replace('.geojson', '.json')}"
            print(f"   ✅ {filename} (enhanced with precomputed data)")
            if os.path.exists(mapping_file):
                print(f"   ✅ {mapping_file}")
    
    print("\n🚀 Now update your Streamlit app to use these enhanced files for instant loading!")

if __name__ == "__main__":
    main()
