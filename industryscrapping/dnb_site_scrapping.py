import json
import csv
import pandas as pd
from pathlib import Path
import os
import glob

def read_json_to_csv(json_file_path, csv_output_path=None):
    """
    Read JSON data from file and convert company information to CSV format
    
    Args:
        json_file_path (str): Path to the JSON file
        csv_output_path (str): Path for output CSV file (optional)
    
    Returns:
        pandas.DataFrame: DataFrame containing the company data
    """
    
    # Read JSON data
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None
    
    # Extract company information
    companies = data.get('companyInformationCompany', [])
    
    if not companies:
        print("No company data found in the JSON file.")
        return None
    
    # Prepare data for CSV
    csv_data = []
    
    for company in companies:
        # Extract address information
        address = company.get('primaryAddress', {})
        address_country = address.get('addressCountry', {})
        address_locality = address.get('addressLocality', {})
        address_region = address.get('addressRegion', {})
        street_address = address.get('streetAddress', {})
        
        # Create row data
        row = {
            'DUNS': company.get('duns', ''),
            'Company_Name': company.get('primaryName', ''),
            'Company_URL_Name': company.get('primaryNameForUrl', ''),
            'Sales_Revenue': company.get('salesRevenue', ''),
            'Is_Unincorporated': company.get('isUnincorporatedCompany', ''),
            'Street_Address': street_address.get('line1', ''),
            'City': address_locality.get('name', ''),
            'State_Province': address_region.get('name', ''),
            'State_Abbreviation': address_region.get('abbreviatedName', ''),
            'Postal_Code': address.get('postalCode', ''),
            'Country': address_country.get('countryName', ''),
            'Country_Code': address_country.get('isoAlpha2Code', ''),
            'Formatted_City': company.get('addressLocalityNameFormatted', ''),
            'Formatted_Region': company.get('addressRegionNameFormatted', ''),
            'Company_URL': company.get('companyNameUrl', '')
        }
        
        csv_data.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(csv_data)
    
    # If output path not specified, create one based on input file
    if csv_output_path is None:
        input_path = Path(json_file_path)
        csv_output_path = input_path.with_suffix('.csv')
    
    # Save to CSV
    try:
        df.to_csv(csv_output_path, index=False, encoding='utf-8')
        print(f"CSV file successfully created: {csv_output_path}")
        print(f"Total companies processed: {len(csv_data)}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        return df
    
    return df

def process_all_json_files(input_folder='input', output_csv='combined_companies.csv'):
    """
    Process all JSON files in the input folder and combine into single CSV
    
    Args:
        input_folder (str): Path to folder containing JSON files
        output_csv (str): Path for output CSV file
    
    Returns:
        pandas.DataFrame: Combined DataFrame containing all company data
    """
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' not found.")
        return None
    
    # Find all JSON files in the input folder
    json_files = glob.glob(os.path.join(input_folder, '*.json'))
    
    if not json_files:
        print(f"No JSON files found in '{input_folder}' folder.")
        return None
    
    print(f"Found {len(json_files)} JSON files:")
    for file in json_files:
        print(f"  - {os.path.basename(file)}")
    
    all_companies = []
    file_stats = {}
    
    # Process each JSON file
    for json_file in json_files:
        print(f"\nProcessing: {os.path.basename(json_file)}")
        
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"  Error: Could not read {json_file}")
            continue
        except json.JSONDecodeError:
            print(f"  Error: Invalid JSON format in {json_file}")
            continue
        
        # Extract company information
        companies = data.get('companyInformationCompany', [])
        
        if not companies:
            print(f"  No company data found in {json_file}")
            continue
        
        file_stats[os.path.basename(json_file)] = len(companies)
        print(f"  Found {len(companies)} companies")
        
        # Process companies from this file
        for company in companies:
            # Extract address information
            address = company.get('primaryAddress', {})
            address_country = address.get('addressCountry', {})
            address_locality = address.get('addressLocality', {})
            address_region = address.get('addressRegion', {})
            street_address = address.get('streetAddress', {})
            
            # Create row data with source file info
            row = {
                'Source_File': os.path.basename(json_file),
                'DUNS': company.get('duns', ''),
                'Company_Name': company.get('primaryName', ''),
                'Company_URL_Name': company.get('primaryNameForUrl', ''),
                'Sales_Revenue': company.get('salesRevenue', ''),
                'Is_Unincorporated': company.get('isUnincorporatedCompany', ''),
                'Street_Address': street_address.get('line1', ''),
                'City': address_locality.get('name', ''),
                'State_Province': address_region.get('name', ''),
                'State_Abbreviation': address_region.get('abbreviatedName', ''),
                'Postal_Code': address.get('postalCode', ''),
                'Country': address_country.get('countryName', ''),
                'Country_Code': address_country.get('isoAlpha2Code', ''),
                'Formatted_City': company.get('addressLocalityNameFormatted', ''),
                'Formatted_Region': company.get('addressRegionNameFormatted', ''),
                'Company_URL': company.get('companyNameUrl', '')
            }
            
            all_companies.append(row)
    
    if not all_companies:
        print("No company data found in any files.")
        return None
    
    # Create combined DataFrame
    df = pd.DataFrame(all_companies)
    
    # Save to CSV
    try:
        df.to_csv(output_csv, index=False, encoding='utf-8')
        print(f"\n" + "="*60)
        print("PROCESSING COMPLETE!")
        print("="*60)
        print(f"Combined CSV file created: {output_csv}")
        print(f"Total companies processed: {len(all_companies)}")
        print("\nFile breakdown:")
        for filename, count in file_stats.items():
            print(f"  {filename}: {count} companies")
        
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        return df
    
    return df

def display_summary(df):
    """Display summary information about the processed data"""
    if df is not None:
        print("\n" + "="*50)
        print("DATA SUMMARY")
        print("="*50)
        print(f"Total companies: {len(df)}")
        print(f"Companies with sales revenue: {df['Sales_Revenue'].notna().sum()}")
        print(f"Unique cities: {df['City'].nunique()}")
        print(f"Unique states: {df['State_Province'].nunique()}")
        
        if 'Source_File' in df.columns:
            print(f"Source files: {df['Source_File'].nunique()}")
            print("\nCompanies per source file:")
            print(df['Source_File'].value_counts())
        
        print("\nTop 5 cities by company count:")
        print(df['City'].value_counts().head())
        print("\nFirst 5 rows:")
        print(df.head())

# Example usage
if __name__ == "__main__":
    # Process all JSON files in the 'input' folder and combine into single CSV
    print("Processing all JSON files in 'input' folder...")
    df = process_all_json_files('input', 'combined_companies.csv')
    
    if df is not None:
        display_summary(df)
    
    print("\n" + "="*60)
    print("USAGE INSTRUCTIONS:")
    print("="*60)
    print("1. Create a folder named 'input'")
    print("2. Place all your JSON files (input1.json, input2.json, etc.) in the 'input' folder")
    print("3. Run this script: python script_name.py")
    print("4. The combined output will be saved as 'combined_companies.csv'")
    print("\nAlternative usage:")
    print("- For single file: df = read_json_to_csv('file.json', 'output.csv')")
    print("- For custom folder: df = process_all_json_files('my_folder', 'my_output.csv')")
