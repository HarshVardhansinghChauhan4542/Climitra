import streamlit as st
import pandas as pd
from typing import Dict, List

def generate_data_summary(filtered_data: Dict[str, pd.DataFrame], data_sources: List[str]) -> Dict[str, Dict]:
    """Generate summary statistics for each data source"""
    summaries = {}
    
    for data_source in data_sources:
        if data_source in filtered_data and not filtered_data[data_source].empty:
            df = filtered_data[data_source]
            summary = {
                "total_records": len(df),
                "columns": list(df.columns),
                "numeric_columns": [],
                "categorical_columns": []
            }
            
            # Identify numeric and categorical columns
            for col in df.columns:
                if pd.api.types.is_numeric_dtype(df[col]):
                    summary["numeric_columns"].append(col)
                else:
                    summary["categorical_columns"].append(col)
            
            # Generate specific insights based on data source type
            if data_source in ["Steel Plants", "Steel Plants with BF"]:
                summary.update(_generate_steel_plant_summary(df))
            elif data_source == "Rice Mills":
                summary.update(_generate_rice_mills_summary(df))
            elif data_source == "Geocoded Companies":
                summary.update(_generate_geocoded_companies_summary(df))
            
            summaries[data_source] = summary
    
    return summaries

def _generate_steel_plant_summary(df: pd.DataFrame) -> Dict:
    """Generate summary specific to steel plants data"""
    summary = {}
    
    # Capacity statistics
    if "Capacity" in df.columns:
        capacity_data = pd.to_numeric(df["Capacity"], errors="coerce").dropna()
        if not capacity_data.empty:
            summary["capacity_stats"] = {
                "total_capacity": capacity_data.sum(),
                "avg_capacity": capacity_data.mean(),
                "min_capacity": capacity_data.min(),
                "max_capacity": capacity_data.max()
            }
    
    # Operational status
    op_cols = ["Operational", "Operational Status", "Status"]
    op_col = next((col for col in op_cols if col in df.columns), None)
    if op_col:
        summary["operational_status"] = df[op_col].value_counts().to_dict()
    
    # State distribution
    state_col = next((col for col in df.columns if col.lower() == "state"), None)
    if state_col:
        summary["state_distribution"] = df[state_col].value_counts().head(10).to_dict()
    
    # District distribution
    district_col = next((col for col in df.columns if col.lower() == "district"), None)
    if district_col:
        summary["district_distribution"] = df[district_col].value_counts().head(10).to_dict()
    
    return summary

def _generate_rice_mills_summary(df: pd.DataFrame) -> Dict:
    """Generate summary specific to rice mills data"""
    summary = {}
    
    # State distribution
    state_col = next((col for col in df.columns if col.lower() == "state"), None)
    if state_col:
        summary["state_distribution"] = df[state_col].value_counts().head(10).to_dict()
    
    # District distribution  
    district_col = next((col for col in df.columns if col.lower() == "district"), None)
    if district_col:
        summary["district_distribution"] = df[district_col].value_counts().head(10).to_dict()
    
    # Name patterns
    name_col = next((col for col in df.columns if "name" in col.lower()), None)
    if name_col:
        summary["name_patterns"] = {
            "unique_names": df[name_col].nunique(),
            "sample_names": df[name_col].head(10).tolist()
        }
    
    return summary

def _generate_geocoded_companies_summary(df: pd.DataFrame) -> Dict:
    """Generate summary specific to geocoded companies data"""
    summary = {}
    
    # Company name patterns
    name_cols = [col for col in df.columns if any(term in col.lower() for term in ['company', 'name', 'firm', 'business'])]
    if name_cols:
        name_col = name_cols[0]
        summary["company_patterns"] = {
            "unique_companies": df[name_col].nunique(),
            "sample_companies": df[name_col].head(10).tolist()
        }
    
    # State distribution
    state_col = next((col for col in df.columns if col.lower() == "state"), None)
    if state_col:
        summary["state_distribution"] = df[state_col].value_counts().head(10).to_dict()
    
    # District distribution
    district_col = next((col for col in df.columns if col.lower() == "district"), None)
    if district_col:
        summary["district_distribution"] = df[district_col].value_counts().head(10).to_dict()
    
    # Source file distribution
    if "Source_File" in df.columns:
        summary["source_files"] = df["Source_File"].value_counts().to_dict()
    
    return summary

def render_summary_panel(summaries: Dict[str, Dict], data_sources: List[str]):
    """Render the summary panel with statistics and insights"""
    st.subheader("📈 Data Summary & Insights")
    
    # Overall summary
    total_records = sum(summary.get("total_records", 0) for summary in summaries.values())
    st.metric("Total Records Across All Sources", total_records)
    
    st.markdown("---")
    
    # Individual data source summaries
    for data_source in data_sources:
        if data_source in summaries:
            summary = summaries[data_source]
            
            with st.expander(f"📊 {data_source} Summary", expanded=True):
                # Basic stats
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Records", summary["total_records"])
                with col2:
                    st.metric("Columns", len(summary["columns"]))
                
                st.markdown("**Column Overview:**")
                st.write(f"Numeric columns: {len(summary['numeric_columns'])}")
                st.write(f"Categorical columns: {len(summary['categorical_columns'])}")
                
                # Data source specific insights
                if "capacity_stats" in summary:
                    st.markdown("**🏭 Capacity Statistics:**")
                    cap_stats = summary["capacity_stats"]
                    st.write(f"Total Capacity: {cap_stats['total_capacity']:,.0f}")
                    st.write(f"Average Capacity: {cap_stats['avg_capacity']:,.0f}")
                    st.write(f"Min Capacity: {cap_stats['min_capacity']:,.0f}")
                    st.write(f"Max Capacity: {cap_stats['max_capacity']:,.0f}")
                
                if "operational_status" in summary:
                    st.markdown("**⚡ Operational Status:**")
                    for status, count in summary["operational_status"].items():
                        st.write(f"{status}: {count}")
                
                if "state_distribution" in summary:
                    st.markdown("**📍 Top States:**")
                    for state, count in list(summary["state_distribution"].items())[:5]:
                        st.write(f"{state}: {count}")
                
                if "district_distribution" in summary:
                    st.markdown("**🏘️ Top Districts:**")
                    for district, count in list(summary["district_distribution"].items())[:5]:
                        st.write(f"{district}: {count}")
                
                if "company_patterns" in summary:
                    st.markdown("**🏢 Company Insights:**")
                    st.write(f"Unique Companies: {summary['company_patterns']['unique_companies']}")
                    st.write("Sample Companies:")
                    for company in summary["company_patterns"]["sample_companies"][:3]:
                        st.write(f"- {company}")
                
                if "source_files" in summary:
                    st.markdown("**📁 Source Files:**")
                    for source_file, count in summary["source_files"].items():
                        st.write(f"{source_file}: {count}")
                
                if "name_patterns" in summary:
                    st.markdown("**🏷️ Name Patterns:**")
                    st.write(f"Unique Names: {summary['name_patterns']['unique_names']}")
                    st.write("Sample Names:")
                    for name in summary["name_patterns"]["sample_names"][:3]:
                        st.write(f"- {name}")
