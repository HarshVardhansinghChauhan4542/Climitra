import streamlit as st
import os

def render_crop_specific_data(pdf_viewer):
    """
    Renders the Crop-Specific Data section with PDF download and inline viewing.
    """
    st.title("🌾 Crop-Specific Biochar Resource Information")

    crop_selected = st.selectbox(
        "Choose a Crop", 
        ["Cotton", "Sugarcane", "Maize", "Juliflora", "Lantana", "Bamboo"]
    )

    pdf_map = {
        "Cotton": "assets/pdfs/cotton.pdf",
        "Sugarcane": "assets/pdfs/sugarcane.pdf",
        "Maize": "assets/pdfs/maize.pdf",
        "Juliflora": "assets/pdfs/Juliflora (1).pdf",
        "Lantana": "assets/pdfs/Lantana (1).pdf",
        "Bamboo": "assets/pdfs/bamboo.pdf",
    }

    if crop_selected in pdf_map and os.path.exists(pdf_map[crop_selected]):
        st.markdown(f"#### 📄 {crop_selected} Reference PDF")

        with open(pdf_map[crop_selected], "rb") as f:
            st.download_button(
                label=f"⬇️ Download {crop_selected} PDF", 
                data=f.read(), 
                file_name=os.path.basename(pdf_map[crop_selected]), 
                mime="application/pdf"
            )

        # Render PDF inline if viewer is provided
        if pdf_viewer:
            pdf_viewer(pdf_map[crop_selected])
    else:
        st.warning("No PDF available for this crop.")
