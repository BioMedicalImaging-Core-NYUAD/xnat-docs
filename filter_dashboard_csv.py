#!/usr/bin/env python3
"""
Filter the ARI dashboard CSV to show only display-relevant columns.
This script is used by the GitHub Actions workflow to create a clean version
of the dashboard data for documentation display.
"""

import pandas as pd
import sys
import os

def filter_dashboard_csv(input_file, output_file):
    """
    Filter the dashboard CSV to include only the columns needed for display.
    
    Args:
        input_file (str): Path to the full dashboard CSV
        output_file (str): Path to write the filtered CSV
    """
    
    # Define the columns we want to display (in requested order)
    display_columns = [
        'Subject_ID',
        'Overall_Status', 
        'Sbref_Direction',
        'IntendedFor',
        'DWI_Parameters',
        'File_Properties',
        'Missing_Files',
        'Extra_Files',
        'DWI_Version',
        'ASL_Version'
    ]
    
    try:
        # Read the full CSV
        df = pd.read_csv(input_file)
        
        # Check if all required columns exist
        missing_columns = [col for col in display_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing columns in source CSV: {missing_columns}")
            # Use only the columns that exist
            display_columns = [col for col in display_columns if col in df.columns]
        
        # Filter to only the display columns
        filtered_df = df[display_columns]
        
        # Write the filtered CSV
        filtered_df.to_csv(output_file, index=False)
        
        print(f"Successfully filtered CSV:")
        print(f"  Input: {input_file} ({len(df)} rows, {len(df.columns)} columns)")
        print(f"  Output: {output_file} ({len(filtered_df)} rows, {len(filtered_df.columns)} columns)")
        print(f"  Columns included: {', '.join(display_columns)}")
        
        return True
        
    except FileNotFoundError:
        print(f"Error: Input file not found: {input_file}")
        return False
    except pd.errors.EmptyDataError:
        print(f"Error: Input file is empty: {input_file}")
        return False
    except Exception as e:
        print(f"Error processing CSV: {e}")
        return False

def main():
    """Main function to handle command line arguments."""
    
    # Default file paths
    default_input = "xnat_ari_dashboard.csv"
    default_output = "docs/source/_static/xnat_ari_dashboard_display.csv"
    
    # Get input and output files from command line or use defaults
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
    else:
        input_file = default_input
    
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        output_file = default_output
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Filter the CSV
    success = filter_dashboard_csv(input_file, output_file)
    
    if success:
        print("✅ CSV filtering completed successfully")
        sys.exit(0)
    else:
        print("❌ CSV filtering failed")
        sys.exit(1)

if __name__ == "__main__":
    main()