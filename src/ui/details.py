import streamlit as st
import pandas as pd

def render_steel_plant_details(row):
    with st.expander(f"{row['Plant Name']}"):
        st.write(f"**Capacity (MTPA):** {row.get('Capacity(MTPA)', 'N/A')}")
        st.write(f"**Furnace Type:** {row.get('Furnance', 'N/A')}")
        st.write(f"**Operational Status:** {row.get('Operational', 'N/A')}")
        source_url = row.get('Source')
        if isinstance(source_url, str) and source_url.startswith('http'):
            st.markdown(f"**Source:** <a href='{source_url}' target='_blank'>Visit Link</a>", unsafe_allow_html=True)
        else:
            st.write(f"**Source:** {source_url if pd.notna(source_url) else 'N/A'}")

def render_steel_bf_details(row):
    plant_name = row.get('Plant') if 'Plant' in row else row.get('Plant Name', 'Unknown Plant')
    with st.expander(f"{plant_name}"):
        st.write(f"**Blast Furnace Capacity:** {row.get('Quantity', 'N/A')} Mtpa")
        st.write(f"**State:** {row.get('State', 'N/A')}")
        st.write(f"**District:** {row.get('District', 'N/A')}")

def render_rice_mill_details(row):
    with st.expander(f"{row['name']}"):
        st.write(f"**Address:** {row.get('address', 'N/A')}")
        st.write(f"**Phone:** {row.get('phone', 'N/A')}")
        st.write(f"**Email:** {row.get('email', 'N/A')}")
        st.write(f"**State:** {row.get('state', 'N/A')}")
        st.write(f"**Country:** {row.get('country', 'N/A')}")
        st.write(f"**ZIP:** {row.get('zip', 'N/A')}")
        st.write(f"**Rating:** {row.get('star_count', 'N/A')} ({row.get('rating_count', 'N/A')} reviews)")
        st.write(f"**Category:** {row.get('primary_category_name', 'N/A')}")
        
        website_url = row.get('url')
        if isinstance(website_url, str) and website_url.startswith('http'):
            st.markdown(f"**Website:** <a href='{website_url}' target='_blank'>Visit Site</a>", unsafe_allow_html=True)
        else:
            st.write(f"**Website:** {website_url if pd.notna(website_url) else 'N/A'}")

        # Social media links
        render_social_links(row)

def render_geocoded_company_details(row):
    with st.expander(f"{row['Company_Name']}"):
        st.write(f"**Sales Revenue:** {row.get('Sales_Revenue', 'N/A')}")
        st.write(f"**City:** {row.get('City', 'N/A')}")
        st.write(f"**State:** {row.get('State', 'N/A')}")
        st.write(f"**Country:** {row.get('Country', 'N/A')}")
        company_url = row.get('Company_URL')
        if isinstance(company_url, str) and company_url.startswith('http'):
            st.markdown(f"**Website:** <a href='{company_url}' target='_blank'>Visit Site</a>", unsafe_allow_html=True)
        else:
            st.write(f"**Website:** {company_url if pd.notna(company_url) else 'N/A'}")

def render_social_links(row):
    links = []
    platforms = ["facebook", "instagram", "twitter", "linkedin", "youtube", "whatsapp", "tiktok"]
    for platform in platforms:
        col = f"{platform}_link"
        if col in row and pd.notna(row[col]) and str(row[col]).startswith("http"):
            links.append(f"<a href='{row[col]}' target='_blank'>{platform.capitalize()}</a>")
    if links:
        st.markdown(f"**Social Media:** {' | '.join(links)}", unsafe_allow_html=True)


def render_detailed_results(filtered_plants, data_sources, name_filter):
    if name_filter and not filtered_plants.empty:
        st.markdown("---")
        st.markdown("#### ℹ️ Details for Found Results")

        for source in data_sources:
            df = filtered_plants[filtered_plants['source_type'] == source]
            if df.empty:
                continue

            for _, row in df.iterrows():
                if source == "Steel Plants":
                    render_steel_plant_details(row)
                elif source == "Steel Plants with BF":
                    render_steel_bf_details(row)
                elif source == "Rice Mills":
                    render_rice_mill_details(row)
                elif source == "Geocoded Companies":
                    render_geocoded_company_details(row)

        st.markdown("---")
