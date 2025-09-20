import streamlit as st
import os

def render_geojson_overlay_selector(geojson_metadata):
    """
    UI for selecting GeoJSON overlays and showing metadata/images.
    Returns the list of selected files.
    """
    selected_geojson_files = st.multiselect(
        "Select Primary GeoJSON Overlays:",
        list(geojson_metadata.keys()),
        default=[],
        key="primary_geojson_overlays"
    )

    for geojson_file in selected_geojson_files:
        show_metadata_and_image(geojson_file, geojson_metadata)

    return selected_geojson_files


def show_metadata_and_image(geojson_file, geojson_metadata):
    """Display metadata, description, source link, image, and downloads for a GeoJSON file."""
    meta = geojson_metadata.get(geojson_file, {})
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(f"#### ℹ️ Metadata for {geojson_file}")
        st.markdown(f"**Description:** {meta.get('description', 'N/A')}")
        st.markdown(f"**Source_link:** [Visit site]({meta.get('external_link', '#')})")
        st.markdown(f"**Recorded Time:** {meta.get('recorded_time', 'Unknown')}")
        st.markdown(f"**Source:** {meta.get('source', 'Unknown')}")

        # Download original
        original_file = meta.get("original", geojson_file.replace("enhanced_", ""))
        if os.path.exists(original_file):
            with open(original_file, "r") as f:
                geojson_text = f.read()
            st.download_button(
                f"⬇️ Download Original {original_file}",
                geojson_text,
                file_name=original_file,
                mime="application/json"
            )

        # Download enhanced
        if os.path.exists(geojson_file):
            with open(geojson_file, "r") as f:
                enhanced_text = f.read()
            st.download_button(
                f"⬇️ Download Enhanced {geojson_file}",
                enhanced_text,
                file_name=geojson_file,
                mime="application/json"
            )

    with col2:
        # Construct the full path to the image in assets/images folder
        image_filename = meta.get("image_path", "")
        if image_filename:
            full_image_path = os.path.join("assets", "images", image_filename)
            if os.path.exists(full_image_path):
                st.image(full_image_path, caption="Source Reference Map", width=300)
            else:
                st.warning(f"Image not found: {full_image_path}")
        else:
            st.info("No image available for this overlay")
