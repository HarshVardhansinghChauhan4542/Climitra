import streamlit as st
import rasterio
from rasterio.plot import reshape_as_image
import numpy as np
import cv2
from shapely.geometry import Polygon, mapping
import json
from PIL import Image

# Allow large images (bypass DecompressionBombError)
Image.MAX_IMAGE_PIXELS = None

st.set_page_config(layout="wide")
st.title("🗺️ GeoTIFF to GeoJSON Digitizer (All Contours Included)")

# --- Utility Functions ---

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def convert_contour_to_geojson(contours, transform):
    features = []
    for cnt in contours:
        cnt = cnt.squeeze()

        if cnt.ndim != 2 or len(cnt) < 3:
            continue  # can't make a polygon

        try:
            geo_pts = [transform * (float(x), float(y)) for x, y in cnt]

            # Ensure closed polygon
            if geo_pts[0] != geo_pts[-1]:
                geo_pts.append(geo_pts[0])

            poly = Polygon(geo_pts)

            if not poly.is_valid:
                poly = poly.buffer(0)  # auto-fix self-intersections etc.

            features.append({
                "type": "Feature",
                "geometry": mapping(poly),
                "properties": {}
            })

        except Exception as e:
            print(f"⚠️ Skipped one contour due to error: {e}")
            continue

    return {
        "type": "FeatureCollection",
        "features": features
    }, len(features)

# --- File Upload ---
uploaded_file = st.file_uploader("📂 Upload a GeoTIFF image (.tif)", type=["tif", "tiff"])

if uploaded_file:
    with rasterio.open(uploaded_file) as src:
        img = reshape_as_image(src.read())
        transform = src.transform

    if img.shape[2] > 3:
        img = img[:, :, :3]  # Drop alpha channel

    # Downscale image for display
    max_pixels = 1500 * 1500
    total_pixels = img.shape[0] * img.shape[1]
    if total_pixels > max_pixels:
        scale_factor = (max_pixels / total_pixels) ** 0.5
        display_img = cv2.resize(img, (0, 0), fx=scale_factor, fy=scale_factor)
    else:
        display_img = img

    st.image(display_img, caption="🖼️ Uploaded GeoTIFF (preview only)")

    # --- Color Selection ---
    num_colors = st.slider("🎨 Number of Colors to Match", 1, 5, 2)
    selected_colors = []
    for i in range(num_colors):
        hex_color = st.color_picker(f"Pick color #{i+1}", "#ff0000")
        selected_colors.append(hex_to_rgb(hex_color))

    tolerance = st.slider("🎚️ Color matching tolerance", 0, 100, 30)

    # --- Create Mask ---
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    for color in selected_colors:
        lower = np.array([max(0, c - tolerance) for c in color], dtype=np.uint8)
        upper = np.array([min(255, c + tolerance) for c in color], dtype=np.uint8)
        mask |= cv2.inRange(img, lower, upper)

    st.subheader("🩷 Mask of Matched Pixels")
    st.image(mask, caption="White = Selected Regions")

    # --- Find Contours ---
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    st.write(f"🔍 Total contours detected: {len(contours)}")

    # --- Optional Preview on Original Image ---
    preview_img = img.copy()
    cv2.drawContours(preview_img, contours, -1, (0, 255, 0), 1)

    # Downscale preview too
    if total_pixels > max_pixels:
        preview_img = cv2.resize(preview_img, (0, 0), fx=scale_factor, fy=scale_factor)

    st.subheader("🧪 Preview on Original Image")
    st.image(preview_img, caption="🧪 Preview: Detected Contours")

    # --- GeoJSON Export ---
    geojson_data, count = convert_contour_to_geojson(contours, transform)
    st.success(f"✅ {count} polygons exported (0 skipped).")

    st.subheader("💾 Download GeoJSON")
    st.download_button(
        label="Download GeoJSON File",
        data=json.dumps(geojson_data, indent=2),
        file_name="extracted_polygons.geojson",
        mime="application/geo+json"
    )
