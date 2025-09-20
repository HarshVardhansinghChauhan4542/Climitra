import streamlit as st
import pandas as pd
from src.data.preprocessing import calculate_pagination_info, get_paginated_data
from src.utils.session import get_or_init_session_state

# Stub for plant card rendering (replace with your existing one)
def create_plant_cards_vectorized(data, source):
    for _, row in data.iterrows():
        st.write(f"Plant: {row.to_dict()}")

def render_paginated_table(filtered_plants, data_sources, get_source_data_by_type):
    source_data_dict = get_source_data_by_type(filtered_plants, data_sources)

    for source, source_data in source_data_dict.items():
        st.markdown(f"**{source}** ({len(source_data)} items)")

        page_key, size_key = get_or_init_session_state(source)
        total_pages = calculate_pagination_info(len(source_data), st.session_state[size_key])

        if st.session_state[page_key] > total_pages:
            st.session_state[page_key] = 1

        paginated_data, start_idx, end_idx = get_paginated_data(
            source_data, st.session_state[page_key], st.session_state[size_key]
        )

        # Pagination controls
        col1, col2, col3 = st.columns([2, 1, 2])

        with col1:
            if st.session_state[page_key] > 1:
                if st.button("⬅️ Previous", key=f"prev_{page_key}"):
                    st.session_state[page_key] -= 1
                    st.rerun()
            else:
                st.button("⬅️ Previous", key=f"prev_{page_key}", disabled=True)

        with col2:
            page_size = st.selectbox("Items per page:", [5, 10, 20, 50], index=1, key=size_key)
            if page_size != st.session_state[size_key]:
                st.session_state[size_key] = page_size
                st.session_state[page_key] = 1
                st.rerun()

        with col3:
            if st.session_state[page_key] < total_pages:
                if st.button("Next ➡️", key=f"next_{page_key}"):
                    st.session_state[page_key] += 1
                    st.rerun()
            else:
                st.button("Next ➡️", key=f"next_{page_key}", disabled=True)

        st.markdown(
            f"**Page {st.session_state[page_key]} of {total_pages}** "
            f"(Showing items {start_idx}-{end_idx} of {len(source_data)})"
        )

        with st.container():
            create_plant_cards_vectorized(paginated_data, source)

        st.markdown("---")

def render_summary_statistics(filtered_plants, data_sources, state_filter):
    st.markdown("#### 📊 Summary")
    st.write(f"**Total Plants:** {len(filtered_plants)}")

    # Counts by source
    for source in data_sources:
        count = len(filtered_plants[filtered_plants['source_type'] == source])
        if count > 0:
            st.write(f"**{source}:** {count}")

    # Counts by state
    if state_filter:
        st.markdown("---")
        st.markdown("**By State:**")
        for state in state_filter:
            state_count = len(filtered_plants[filtered_plants['state'] == state])
            if state_count > 0:
                st.write(f"**{state}:** {state_count}")

    # Operational status
    if 'Operational' in filtered_plants.columns:
        st.markdown("---")
        status_counts = filtered_plants['Operational'].value_counts()
        st.markdown(f"**Statuses (Total: {len(status_counts)})**")
        for status, count in status_counts.items():
            st.write(f"  • {status}: {count}")

    # Furnace type
    for col in ['Furnance', 'Furnace Type', 'Furnace_Type']:
        if col in filtered_plants.columns:
            st.markdown("---")
            furnace_counts = filtered_plants[col].value_counts()
            st.markdown(f"**Furnace Types (Total: {len(furnace_counts)})**")
            for furnace, count in furnace_counts.items():
                st.write(f"  • {furnace}: {count}")
