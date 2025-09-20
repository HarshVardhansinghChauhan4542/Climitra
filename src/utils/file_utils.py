# src/utils/file_utils.py
import pandas as pd
import json
import streamlit as st

@st.cache_data
def get_data_info(file_path):
    """Get basic information about data file without loading full data"""
    try:
        if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            with pd.ExcelFile(file_path) as excel_file:
                # read just first row
                sample_df = pd.read_excel(file_path, nrows=1)
                return {
                    'columns': list(sample_df.columns),
                    'sheet_count': len(excel_file.sheet_names),
                    'file_type': 'excel'
                }
        elif file_path.endswith('.csv'):
            sample_df = pd.read_csv(file_path, nrows=1)
            return {
                'columns': list(sample_df.columns),
                'file_type': 'csv'
            }
        elif file_path.endswith('.geojson'):
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
