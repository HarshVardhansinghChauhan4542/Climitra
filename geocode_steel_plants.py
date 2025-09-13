
import pandas as pd

INPUT_FILE = 'STEEL PLANTS BF CAPACITY DATA.xlsx'
OUTPUT_FILE = 'steel_plants_with_city.xlsx'
SHEET_NAME = 0  # Change if your data is not in the first sheet

# Read the Excel file
df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)

# Extract Plant name (column A) and State (column H)
df_city = df[[df.columns[0], df.columns[7]]].copy()
df_city.columns = ['Plant_Name', 'State']

# Function to extract city (word before 'plant' or 'Plant')
def extract_city(plant_name):
    tokens = str(plant_name).split()
    for i, token in enumerate(tokens):
        if token.lower() == 'plant' and i > 0:
            return tokens[i-1]
    return ''

df_city['City'] = df_city['Plant_Name'].apply(extract_city)

# Save output
df_city.to_excel(OUTPUT_FILE, index=False)
print(f"City extraction complete. Results saved to {OUTPUT_FILE}")
