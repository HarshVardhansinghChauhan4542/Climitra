import pandas as pd

# Read the Excel file
INPUT_FILE = 'Untitled spreadsheet (1).xlsx'
OUTPUT_FILE = 'coordinates_separated.xlsx'

df = pd.read_excel(INPUT_FILE)

# Print original columns and data
print("Original columns:", df.columns.tolist())
print("\nFirst few rows of original data:")
print(df.head())

# Function to extract coordinates
def extract_coordinates(row):
    try:
        # Convert to string and clean up
        coords = str(row).strip()
        # Split by comma and clean each part
        parts = [p.strip() for p in coords.split(',')]
        
        if len(parts) >= 2:
            # Take first two parts as lat and lon
            lat = float(parts[0])
            lon = float(parts[1])
            return pd.Series({'Latitude': lat, 'Longitude': lon})
        else:
            return pd.Series({'Latitude': None, 'Longitude': None})
    except Exception as e:
        print(f"Error processing coordinates: {row} - {str(e)}")
        return pd.Series({'Latitude': None, 'Longitude': None})

# Find columns containing coordinates
coord_cols = [col for col in df.columns if any(x in col.lower() for x in ['lat', 'lon', 'coordinate'])]

if coord_cols:
    print(f"\nFound coordinate columns: {coord_cols}")
    # Create new columns for separated coordinates
    for col in coord_cols:
        print(f"\nProcessing column: {col}")
        print("Sample values:")
        print(df[col].head())
        
        # Extract coordinates
        new_coords = df[col].apply(extract_coordinates)
        df[f'Clean_Lat_{col}'] = new_coords['Latitude']
        df[f'Clean_Lon_{col}'] = new_coords['Longitude']

# Save to new file
df.to_excel(OUTPUT_FILE, index=False)
print(f"\nSaved cleaned coordinates to {OUTPUT_FILE}")
print("\nNew columns added:")
print([col for col in df.columns if 'Clean_' in col])
