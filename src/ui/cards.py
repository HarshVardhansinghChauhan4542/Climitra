import streamlit as st

def create_plant_cards_vectorized(paginated_data, source):
    """Create plant cards using vectorized operations instead of iterrows"""
    plant_data = paginated_data.to_dict('records')

    for plant in plant_data:
        if source in ["Steel Plants", "Steel Plants with BF"]:
            plant_name = plant.get('Plant Name', plant.get('Plant', 'Unknown'))
            capacity = plant.get('Capacity(MTPA)', 'N/A')
            furnace_type = plant.get('Furnance', plant.get('Furnace Type', 'N/A'))
            operational_status = plant.get('Operational', 'N/A')
            
            with st.expander(f"🏭 {plant_name}"):
                st.write(f"**Capacity:** {capacity} MTPA")
                st.write(f"**Furnace Type:** {furnace_type}")
                st.write(f"**Status:** {operational_status}")
                st.write(f"**State:** {plant.get('state', 'N/A')}")
                st.write(f"**District:** {plant.get('district', 'N/A')}")
                
        elif source == "Geocoded Companies":
            company_name = plant.get('Company_Name', 'Unknown')
            sales_revenue = plant.get('Sales_Revenue', 'N/A')
            city = plant.get('City', 'N/A')
            
            with st.expander(f"🏢 {company_name}"):
                st.write(f"**Sales Revenue:** {sales_revenue}")
                st.write(f"**City:** {city}")
                st.write(f"**State:** {plant.get('State', 'N/A')}")
                
        elif source == "Rice Mills":
            mill_name = plant.get('name', plant.get('Mill Name', 'Unknown'))
            address = plant.get('address', 'N/A')
            
            with st.expander(f"🌾 {mill_name}"):
                st.write(f"**Address:** {address}")
                st.write(f"**State:** {plant.get('state', 'N/A')}")
                st.write(f"**District:** {plant.get('district', 'N/A')}")