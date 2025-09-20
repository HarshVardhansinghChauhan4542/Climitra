import pandas as pd
import sys
import os

# Add the src directory to the path
sys.path.append('src')

# Load the steel plants data
try:
    df = pd.read_excel("data/raw/steel_plant_data.xlsx")
    print("Steel plants data loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Data types:\n{df.dtypes}")
    print("\nFirst few rows:")
    print(df.head())
except Exception as e:
    print(f"Error loading steel plants data: {e}")

print("\n" + "="*50 + "\n")

# Load the ricemills data
try:
    df_rice = pd.read_csv("data/raw/ricemills.csv")
    print("Ricemills data loaded successfully!")
    print(f"Shape: {df_rice.shape}")
    print(f"Columns: {list(df_rice.columns)}")
    print(f"Data types:\n{df_rice.dtypes}")
    print("\nFirst few rows:")
    print(df_rice.head())
except Exception as e:
    print(f"Error loading ricemills data: {e}")
