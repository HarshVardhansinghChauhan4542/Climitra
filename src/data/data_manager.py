import pandas as pd
import streamlit as st
from src.data.loader import (
    load_steel_plants,
    load_geocoded_companies,
    load_ricemill_data,
)
from src.data.preprocessing import optimize_dataframe_memory, normalize_columns
from src.utils.memory_utils import get_memory_usage_info, cleanup_session_state
from src.data.validation import validate_coordinates

def load_and_merge_data(data_sources):
    """Load, normalize, and merge multiple selected data sources."""
    all_dfs = []

    for source in data_sources:
        if source == "Steel Plants":
            df = load_steel_plants()
        elif source == "Steel Plants with BF":
            from assets.pdfs.steel_plant_bf_loader import load_steel_plants_bf
            df = load_steel_plants_bf()
        elif source == "Geocoded Companies":
            df = load_geocoded_companies()
        elif source == "Rice Mills":
            df = load_ricemill_data()
        else:
            continue

        df["source_type"] = source
        df = optimize_dataframe_memory(df)
        df = normalize_columns(df)
        all_dfs.append(df)

    if not all_dfs:
        return pd.DataFrame()

    plants = pd.concat(all_dfs, ignore_index=True)
    plants = optimize_dataframe_memory(plants)
    return plants


def render_memory_info():
    """Sidebar/expander showing memory usage + cleanup button."""
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
            import gc
            gc.collect()
            st.rerun()


def render_debug_info(plants, data_sources):
    """Expander showing loaded records and validation issues."""
    with st.expander("Data Debug Info"):
        st.write(f"Loaded {len(plants)} records from {', '.join(data_sources)}")

        # Fix category columns that might cause pyarrow issues
        for col in plants.select_dtypes(include=['category']).columns:
            try:
                pd.to_numeric(plants[col].dropna().head(1), errors="raise")
            except Exception:
                plants[col] = plants[col].astype('object')

        st.dataframe(plants)

        invalid_coords = validate_coordinates(plants, data_sources)
        if not invalid_coords.empty:
            st.warning(f"⚠️ Found {len(invalid_coords)} records with invalid coordinates:")
            st.dataframe(invalid_coords)
