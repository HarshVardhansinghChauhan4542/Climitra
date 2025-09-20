import geopandas as gpd
import shapely.geometry as geom
import pandas as pd
import os


def get_location_info_from_coords(polygon):
    """
    Enhanced function to estimate location based on polygon centroid coordinates
    Maps coordinates to actual Indian states and major districts
    """
    try:
        centroid = polygon.centroid
        lat, lon = centroid.y, centroid.x
        
        # Detailed coordinate-based state and district identification for India
        
        # Rajasthan
        if 24.0 <= lat <= 30.2 and 69.5 <= lon <= 78.2:
            districts = []
            if 26.8 <= lat <= 28.4 and 75.0 <= lon <= 76.8:
                districts = ["Jaipur", "Alwar", "Sikar"]
            elif 24.3 <= lat <= 26.0 and 70.9 <= lon <= 73.8:
                districts = ["Jodhpur", "Barmer", "Jaisalmer"]
            elif 27.0 <= lat <= 28.9 and 73.0 <= lon <= 75.5:
                districts = ["Bikaner", "Ganganagar", "Hanumangarh"]
            elif 24.0 <= lat <= 25.8 and 73.7 <= lon <= 75.8:
                districts = ["Udaipur", "Rajsamand", "Dungarpur"]
            else:
                districts = ["Central Rajasthan"]
            return districts, ["Rajasthan"]
        
        # Gujarat
        elif 20.1 <= lat <= 24.7 and 68.2 <= lon <= 74.5:
            districts = []
            if 22.2 <= lat <= 23.8 and 72.0 <= lon <= 73.2:
                districts = ["Ahmedabad", "Gandhinagar", "Mehsana"]
            elif 21.1 <= lat <= 22.3 and 70.0 <= lon <= 72.1:
                districts = ["Rajkot", "Jamnagar", "Porbandar"]
            elif 20.9 <= lat <= 21.9 and 72.7 <= lon <= 73.2:
                districts = ["Surat", "Navsari", "Valsad"]
            elif 22.7 <= lat <= 24.2 and 68.8 <= lon <= 71.8:
                districts = ["Kutch", "Banaskantha", "Patan"]
            else:
                districts = ["Central Gujarat"]
            return districts, ["Gujarat"]
        
        # Maharashtra
        elif 15.6 <= lat <= 22.0 and 72.6 <= lon <= 80.9:
            districts = []
            if 18.8 <= lat <= 19.3 and 72.7 <= lon <= 73.2:
                districts = ["Mumbai", "Mumbai Suburban", "Thane"]
            elif 18.4 <= lat <= 18.7 and 73.7 <= lon <= 74.0:
                districts = ["Pune", "Pimpri-Chinchwad"]
            elif 19.7 <= lat <= 21.2 and 78.0 <= lon <= 79.3:
                districts = ["Nagpur", "Wardha", "Chandrapur"]
            elif 19.0 <= lat <= 20.3 and 74.7 <= lon <= 76.0:
                districts = ["Aurangabad", "Jalna", "Beed"]
            else:
                districts = ["Central Maharashtra"]
            return districts, ["Maharashtra"]
        
        # Karnataka
        elif 11.5 <= lat <= 18.5 and 74.0 <= lon <= 78.6:
            districts = []
            if 12.8 <= lat <= 13.2 and 77.4 <= lon <= 77.8:
                districts = ["Bangalore Urban", "Bangalore Rural"]
            elif 15.3 <= lat <= 15.9 and 75.0 <= lon <= 75.8:
                districts = ["Belgaum", "Bagalkot", "Bijapur"]
            elif 13.3 <= lat <= 14.5 and 74.8 <= lon <= 75.8:
                districts = ["Mysore", "Mandya", "Hassan"]
            elif 14.4 <= lat <= 15.6 and 76.0 <= lon <= 77.6:
                districts = ["Bellary", "Raichur", "Koppal"]
            else:
                districts = ["Central Karnataka"]
            return districts, ["Karnataka"]
        
        # Tamil Nadu
        elif 8.1 <= lat <= 13.6 and 76.2 <= lon <= 80.3:
            districts = []
            if 12.8 <= lat <= 13.2 and 79.8 <= lon <= 80.3:
                districts = ["Chennai", "Kanchipuram", "Tiruvallur"]
            elif 10.7 <= lat <= 11.1 and 76.9 <= lon <= 77.8:
                districts = ["Coimbatore", "Tirupur", "Erode"]
            elif 9.9 <= lat <= 10.8 and 78.0 <= lon <= 78.8:
                districts = ["Madurai", "Theni", "Dindigul"]
            elif 11.8 <= lat <= 12.5 and 79.0 <= lon <= 79.9:
                districts = ["Vellore", "Tiruvannamalai", "Villupuram"]
            else:
                districts = ["Central Tamil Nadu"]
            return districts, ["Tamil Nadu"]
        
        # Andhra Pradesh & Telangana
        elif 12.6 <= lat <= 19.9 and 76.8 <= lon <= 84.8:
            districts = []
            if 17.2 <= lat <= 17.6 and 78.2 <= lon <= 78.7:
                districts = ["Hyderabad", "Rangareddy", "Medchal"]
                return districts, ["Telangana"]
            elif 15.8 <= lat <= 17.1 and 79.7 <= lon <= 81.8:
                districts = ["Visakhapatnam", "Vizianagaram", "Srikakulam"]
                return districts, ["Andhra Pradesh"]
            elif 14.4 <= lat <= 15.9 and 78.1 <= lon <= 80.0:
                districts = ["Kurnool", "Anantapur", "Kadapa"]
                return districts, ["Andhra Pradesh"]
            elif 16.5 <= lat <= 19.0 and 77.3 <= lon <= 80.5:
                districts = ["Warangal", "Karimnagar", "Nizamabad"]
                return districts, ["Telangana"]
            else:
                districts = ["Central Region"]
                return districts, ["Andhra Pradesh/Telangana"]
        
        # Kerala
        elif 8.2 <= lat <= 12.8 and 74.9 <= lon <= 77.4:
            districts = []
            if 9.9 <= lat <= 10.0 and 76.2 <= lon <= 76.4:
                districts = ["Kochi", "Ernakulam"]
            elif 8.4 <= lat <= 8.9 and 76.8 <= lon <= 77.1:
                districts = ["Thiruvananthapuram", "Kollam"]
            elif 11.2 <= lat <= 11.6 and 75.7 <= lon <= 76.1:
                districts = ["Kozhikode", "Malappuram", "Wayanad"]
            elif 9.5 <= lat <= 10.5 and 76.0 <= lon <= 77.0:
                districts = ["Kottayam", "Idukki", "Alappuzha"]
            else:
                districts = ["Central Kerala"]
            return districts, ["Kerala"]
        
        # West Bengal
        elif 21.5 <= lat <= 27.1 and 85.8 <= lon <= 89.9:
            districts = []
            if 22.4 <= lat <= 22.7 and 88.2 <= lon <= 88.5:
                districts = ["Kolkata", "North 24 Parganas", "South 24 Parganas"]
            elif 23.2 <= lat <= 25.6 and 87.8 <= lon <= 89.3:
                districts = ["Darjeeling", "Jalpaiguri", "Cooch Behar"]
            elif 23.8 <= lat <= 24.6 and 87.0 <= lon <= 88.8:
                districts = ["Malda", "Murshidabad", "Birbhum"]
            else:
                districts = ["Central West Bengal"]
            return districts, ["West Bengal"]
        
        # Odisha
        elif 17.8 <= lat <= 22.6 and 81.4 <= lon <= 87.5:
            districts = []
            if 20.2 <= lat <= 20.4 and 85.7 <= lon <= 86.0:
                districts = ["Bhubaneswar", "Khordha", "Puri"]
            elif 21.4 <= lat <= 22.0 and 84.8 <= lon <= 85.8:
                districts = ["Rourkela", "Sundargarh", "Jharsuguda"]
            elif 19.2 <= lat <= 20.5 and 83.9 <= lon <= 85.2:
                districts = ["Cuttack", "Jagatsinghpur", "Kendrapara"]
            else:
                districts = ["Central Odisha"]
            return districts, ["Odisha"]
        
        # Madhya Pradesh
        elif 21.1 <= lat <= 26.9 and 74.0 <= lon <= 82.8:
            districts = []
            if 23.1 <= lat <= 23.4 and 77.2 <= lon <= 77.6:
                districts = ["Bhopal", "Sehore", "Raisen"]
            elif 22.6 <= lat <= 23.0 and 75.7 <= lon <= 76.1:
                districts = ["Indore", "Dewas", "Ujjain"]
            elif 24.5 <= lat <= 25.9 and 78.0 <= lon <= 80.4:
                districts = ["Jabalpur", "Katni", "Narsinghpur"]
            elif 24.0 <= lat <= 25.4 and 81.2 <= lon <= 82.8:
                districts = ["Rewa", "Satna", "Sidhi"]
            else:
                districts = ["Central Madhya Pradesh"]
            return districts, ["Madhya Pradesh"]
        
        # Uttar Pradesh
        elif 23.9 <= lat <= 30.4 and 77.1 <= lon <= 84.6:
            districts = []
            if 28.4 <= lat <= 28.8 and 77.0 <= lon <= 77.4:
                districts = ["New Delhi", "Ghaziabad", "Gautam Buddha Nagar"]
            elif 26.8 <= lat <= 27.2 and 80.8 <= lon <= 81.0:
                districts = ["Lucknow", "Unnao", "Rae Bareli"]
            elif 25.3 <= lat <= 25.5 and 82.9 <= lon <= 83.1:
                districts = ["Varanasi", "Chandauli", "Jaunpur"]
            elif 27.1 <= lat <= 27.3 and 78.0 <= lon <= 78.2:
                districts = ["Agra", "Mathura", "Firozabad"]
            else:
                districts = ["Central Uttar Pradesh"]
            return districts, ["Uttar Pradesh"]
        
        # Punjab
        elif 29.5 <= lat <= 32.5 and 73.9 <= lon <= 76.9:
            districts = []
            if 31.6 <= lat <= 31.8 and 74.8 <= lon <= 75.0:
                districts = ["Amritsar", "Tarn Taran", "Gurdaspur"]
            elif 30.3 <= lat <= 30.5 and 75.8 <= lon <= 76.0:
                districts = ["Ludhiana", "Jalandhar", "Kapurthala"]
            elif 30.9 <= lat <= 31.1 and 75.3 <= lon <= 75.5:
                districts = ["Patiala", "Fatehgarh Sahib", "Sangrur"]
            else:
                districts = ["Central Punjab"]
            return districts, ["Punjab"]
        
        # Haryana
        elif 27.7 <= lat <= 30.9 and 74.5 <= lon <= 77.6:
            districts = []
            if 28.4 <= lat <= 28.6 and 76.9 <= lon <= 77.1:
                districts = ["Gurugram", "Faridabad", "Palwal"]
            elif 29.1 <= lat <= 29.3 and 76.0 <= lon <= 76.2:
                districts = ["Hisar", "Fatehabad", "Sirsa"]
            elif 28.8 <= lat <= 29.0 and 76.6 <= lon <= 76.8:
                districts = ["Rohtak", "Jhajjar", "Sonipat"]
            else:
                districts = ["Central Haryana"]
            return districts, ["Haryana"]
        
        # Jharkhand
        elif 21.9 <= lat <= 25.3 and 83.3 <= lon <= 87.6:
            districts = []
            if 23.3 <= lat <= 23.5 and 85.2 <= lon <= 85.4:
                districts = ["Ranchi", "Khunti", "Lohardaga"]
            elif 22.7 <= lat <= 22.9 and 86.1 <= lon <= 86.3:
                districts = ["Jamshedpur", "East Singhbhum", "West Singhbhum"]
            elif 24.6 <= lat <= 24.8 and 85.9 <= lon <= 86.1:
                districts = ["Dhanbad", "Bokaro", "Giridih"]
            else:
                districts = ["Central Jharkhand"]
            return districts, ["Jharkhand"]
        
        # Chhattisgarh
        elif 17.8 <= lat <= 24.1 and 80.2 <= lon <= 84.4:
            districts = []
            if 21.2 <= lat <= 21.4 and 81.5 <= lon <= 81.7:
                districts = ["Raipur", "Durg", "Bilaspur"]
            elif 19.0 <= lat <= 19.2 and 81.9 <= lon <= 82.1:
                districts = ["Jagdalpur", "Bastar", "Kondagaon"]
            else:
                districts = ["Central Chhattisgarh"]
            return districts, ["Chhattisgarh"]
        
        # Bihar
        elif 24.3 <= lat <= 27.5 and 83.3 <= lon <= 88.1:
            districts = []
            if 25.5 <= lat <= 25.7 and 85.0 <= lon <= 85.2:
                districts = ["Patna", "Nalanda", "Jehanabad"]
            elif 26.1 <= lat <= 26.3 and 85.1 <= lon <= 85.3:
                districts = ["Muzaffarpur", "Sitamarhi", "Sheohar"]
            else:
                districts = ["Central Bihar"]
            return districts, ["Bihar"]
        
        # Assam and Northeast
        elif 24.1 <= lat <= 28.2 and 89.7 <= lon <= 97.1:
            districts = []
            if 26.1 <= lat <= 26.3 and 91.7 <= lon <= 91.9:
                districts = ["Guwahati", "Kamrup", "Nalbari"]
                return districts, ["Assam"]
            elif 25.5 <= lat <= 25.7 and 91.8 <= lon <= 92.0:
                districts = ["Shillong", "East Khasi Hills", "West Khasi Hills"]
                return districts, ["Meghalaya"]
            elif 23.7 <= lat <= 24.7 and 91.2 <= lon <= 92.7:
                districts = ["Agartala", "West Tripura", "Sepahijala"]
                return districts, ["Tripura"]
            elif 25.1 <= lat <= 27.7 and 93.2 <= lon <= 97.4:
                districts = ["Itanagar", "Papum Pare", "Lower Subansiri"]
                return districts, ["Arunachal Pradesh"]
            else:
                districts = ["Northeast Region"]
                return districts, ["Northeast States"]
        
        # Himachal Pradesh
        elif 30.2 <= lat <= 33.2 and 75.6 <= lon <= 79.0:
            districts = []
            if 31.1 <= lat <= 31.3 and 77.1 <= lon <= 77.3:
                districts = ["Shimla", "Solan", "Sirmaur"]
            elif 32.2 <= lat <= 32.4 and 76.3 <= lon <= 76.5:
                districts = ["Dharamshala", "Kangra", "Hamirpur"]
            else:
                districts = ["Central Himachal Pradesh"]
            return districts, ["Himachal Pradesh"]
        
        # Uttarakhand
        elif 28.4 <= lat <= 31.5 and 77.6 <= lon <= 81.0:
            districts = []
            if 30.3 <= lat <= 30.5 and 78.0 <= lon <= 78.2:
                districts = ["Dehradun", "Tehri Garhwal", "Pauri Garhwal"]
            elif 29.2 <= lat <= 29.4 and 79.5 <= lon <= 79.7:
                districts = ["Nainital", "Almora", "Pithoragarh"]
            else:
                districts = ["Central Uttarakhand"]
            return districts, ["Uttarakhand"]
        
        # Jammu & Kashmir / Ladakh
        elif 32.3 <= lat <= 37.1 and 73.3 <= lon <= 80.3:
            districts = []
            if 34.0 <= lat <= 34.2 and 74.7 <= lon <= 74.9:
                districts = ["Srinagar", "Budgam", "Ganderbal"]
                return districts, ["Jammu & Kashmir"]
            elif 32.7 <= lat <= 32.9 and 74.8 <= lon <= 75.0:
                districts = ["Jammu", "Samba", "Kathua"]
                return districts, ["Jammu & Kashmir"]
            elif 34.1 <= lat <= 34.3 and 77.5 <= lon <= 77.7:
                districts = ["Leh", "Kargil"]
                return districts, ["Ladakh"]
            else:
                districts = ["Northern Region"]
                return districts, ["Jammu & Kashmir/Ladakh"]
        
        # Goa
        elif 15.0 <= lat <= 15.8 and 73.7 <= lon <= 74.3:
            districts = ["North Goa", "South Goa"]
            return districts, ["Goa"]
        
        # Default case for coordinates not matching any state
        else:
            return ["Region Unknown"], ["State Unknown"]
            
    except Exception as e:
        return ["Region Unknown"], ["State Unknown"]