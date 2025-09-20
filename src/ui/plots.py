import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def plot_capacity_distribution(data):
    if "Capacity" not in data.columns: 
        return
    fig, ax = plt.subplots()
    data["Capacity"].hist(ax=ax)
    st.pyplot(fig)

def plot_plants_map(data, lat_col="latitude", lon_col="longitude"):
    if lat_col not in data.columns or lon_col not in data.columns:
        st.info("Map visualization not available - coordinate data missing.")
        return
    fig = px.scatter_mapbox(
        data, lat=lat_col, lon=lon_col, hover_name=data.columns[0],
        zoom=4, height=500
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)
