import math
import streamlit as st

@st.cache_data
def convert_coordinate(coord):
    try:
        if isinstance(coord, str) and "°" in coord:
            parts = coord.replace("°"," ").replace("'"," ").replace('"'," ").split()
            deg, min_, sec, direction = int(parts[0]), int(parts[1]), float(parts[2]), parts[3]
            decimal = deg + min_/60 + sec/3600
            return -decimal if direction in ["S","W"] else decimal
        return float(coord)
    except:
        return None

@st.cache_data
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
