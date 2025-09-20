def get_memory_usage_info():
    try:
        import psutil
        process = psutil.Process()
        memory_info = process.memory_info()
        system_memory = psutil.virtual_memory()
        
        return {
            'process_rss_mb': memory_info.rss / 1024 / 1024,
            'process_vms_mb': memory_info.vms / 1024 / 1024,
            'system_total_mb': system_memory.total / 1024 / 1024,
            'system_available_mb': system_memory.available / 1024 / 1024,
            'system_percent_used': system_memory.percent
        }
    except ImportError:
        return {
            'process_rss_mb': 0,
            'process_vms_mb': 0,
            'system_total_mb': 0,
            'system_available_mb': 0,
            'system_percent_used': 0
        }

def cleanup_session_state():
    """Clean up streamlit session state to free memory"""
    import streamlit as st
    if hasattr(st, 'session_state'):
        initial_count = len(st.session_state)
        # Keep only essential session state variables
        essential_keys = {'show_sidebar'}
        keys_to_remove = [key for key in st.session_state.keys() if key not in essential_keys]
        
        for key in keys_to_remove:
            del st.session_state[key]
        
        return len(keys_to_remove)
    return 0
