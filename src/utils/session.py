


def cleanup_session_state():
    """Clean up session state to prevent memory bloat"""
    keys_to_remove = []
    
    for key in st.session_state.keys():
        # Remove large data objects that are no longer needed
        if key.endswith('_data') or key.endswith('_chunk'):
            keys_to_remove.append(key)
        # Remove old pagination state for sources not currently active
        elif key.endswith('_current_page') or key.endswith('_page_size'):
            # Keep only recent pagination state
            if key not in [f"{source.replace(' ', '_').lower()}_current_page" for source in ["Steel Plants", "Steel Plants with BF", "Geocoded Companies", "Rice Mills"]]:
                keys_to_remove.append(key)
    
    for key in keys_to_remove:
        if key in st.session_state:
            del st.session_state[key]
    
    return len(keys_to_remove)