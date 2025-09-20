import pandas as pd

# Check steel plants data columns
try:
    df_steel = pd.read_excel("data/raw/steel_plant_data.xlsx")
    print("Steel Plants columns:")
    print(df_steel.columns.tolist())
    print(f"Shape: {df_steel.shape}")
    print("\nFirst few rows:")
    print(df_steel.head())
except Exception as e:
    print(f"Error loading steel plants: {e}")

print("\n" + "="*50 + "\n")

# Check steel plants with BF data columns
try:
    df_bf = pd.read_excel("data/raw/steel_plant_bf.xlsx")
    print("Steel Plants with BF columns:")
    print(df_bf.columns.tolist())
    print(f"Shape: {df_bf.shape}")
    print("\nFirst few rows:")
    print(df_bf.head())
except Exception as e:
    print(f"Error loading steel plants with BF: {e}")

print("\n" + "="*50 + "\n")

# Check ricemills data columns
try:
    df_rice = pd.read_csv("data/raw/ricemills.csv")
    print("Rice Mills columns:")
    print(df_rice.columns.tolist())
    print(f"Shape: {df_rice.shape}")
    print("\nFirst few rows:")
    print(df_rice.head())
except Exception as e:
    print(f"Error loading ricemills: {e}")
