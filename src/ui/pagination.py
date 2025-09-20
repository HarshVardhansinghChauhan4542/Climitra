import streamlit as st
import math

def get_or_init_session_state(source, default_page=1, default_page_size=10):
    page_key = f"{source.replace(' ', '_').lower()}_current_page"
    size_key = f"{source.replace(' ', '_').lower()}_page_size"
    
    if page_key not in st.session_state:
        st.session_state[page_key] = default_page
    if size_key not in st.session_state:
        st.session_state[size_key] = default_page_size
    
    return page_key, size_key

@st.cache_data
def calculate_pagination_info(total_items, page_size):
    """Calculate pagination information"""
    total_pages = math.ceil(total_items / page_size)
    return total_pages
