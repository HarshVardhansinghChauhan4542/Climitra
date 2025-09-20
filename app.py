import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os

# Configure Streamlit to prevent file watcher threading errors
if "_STREAMLIT_WATCHER_DISABLED" not in os.environ:
    os.environ["_STREAMLIT_WATCHER_DISABLED"] = "true"

# Main layout router
from src.ui.layout import render_main_layout


# ----------------------------
# Global Page Config + Styling
# ----------------------------
st.set_page_config(page_title="Biochar Dashboard", layout="wide")

# Custom CSS for compact layout
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-size: 13px !important;
    }
    .block-container {
        padding: 0.5rem 1rem 0.5rem 1rem;
    }
    .stSidebar {
        width: 220px !important;
    }
    .stDataFrame {
        font-size: 12px !important;
    }
    h1, h2, h3 {
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


# ----------------------------
# Sidebar Toggle (Show/Hide)
# ----------------------------
if "show_sidebar" not in st.session_state:
    st.session_state["show_sidebar"] = True

if st.button("👈 Toggle Sidebar"):
    st.session_state["show_sidebar"] = not st.session_state["show_sidebar"]

# ----------------------------
# Main Entry Point
# ----------------------------
if st.session_state["show_sidebar"]:
    # Sidebar is managed inside layout
    render_main_layout(pdf_viewer=pdf_viewer)
else:
    # If sidebar hidden → still show layout (default Dashboard)
    render_main_layout(pdf_viewer=pdf_viewer)
