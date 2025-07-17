#!/usr/bin/env python3
"""
Generate ARI Dashboard for ReadTheDocs documentation
Processes CSV data and creates RST format dashboard content
"""

import pandas as pd
import os
from datetime import datetime
from pathlib import Path

def generate_summary_stats(df):
    """Generate summary statistics from the dashboard data"""
    total_subjects = len(df)
    subjects_with_issues = len(df[df['Overall_Status'] == 'HAS ISSUES'])
    subjects_passed = len(df[df['Overall_Status'] == 'PASSED'])
    
    # Calculate percentages
    pass_rate = (subjects_passed / total_subjects * 100) if total_subjects > 0 else 0
    
    # Count specific issues
    missing_files = len(df[df['Missing_Files'] == 'INCORRECT'])
    extra_files = len(df[df['Extra_Files'] == 'INCORRECT'])
    file_properties = len(df[df['File_Properties'] == 'INCORRECT'])
    dwi_params = len(df[df['DWI_Parameters'] == 'INCORRECT'])
    
    # Version statistics
    dwi_v1 = len(df[df['DWI_Version'].str.contains('VERSION 1', na=False)])
    dwi_v2 = len(df[df['DWI_Version'].str.contains('VERSION 2', na=False)])
    asl_v1 = len(df[df['ASL_Version'].str.contains('VERSION 1', na=False)])
    asl_v2 = len(df[df['ASL_Version'].str.contains('VERSION 2', na=False)])
    
    return {
        'total_subjects': total_subjects,
        'subjects_passed': subjects_passed,
        'subjects_with_issues': subjects_with_issues,
        'pass_rate': pass_rate,
        'missing_files': missing_files,
        'extra_files': extra_files,
        'file_properties': file_properties,
        'dwi_params': dwi_params,
        'dwi_v1': dwi_v1,
        'dwi_v2': dwi_v2,
        'asl_v1': asl_v1,
        'asl_v2': asl_v2
    }

def generate_rst_table(df, max_rows=50):
    """Generate RST table from dataframe"""
    # Select only the specified columns for the table
    table_cols = [
        'Subject_ID', 'Overall_Status', 'Missing_Files', 'Extra_Files', 
        'File_Properties', 'Sbref_Direction', 'IntendedFor', 'DWI_Parameters', 
        'DWI_Version', 'ASL_Version'
    ]
    
    # Filter dataframe to only include existing columns
    available_cols = [col for col in table_cols if col in df.columns]
    table_df = df[available_cols].head(max_rows)
    
    # Clean up column names for display
    clean_headers = {
        'Subject_ID': 'Subject ID',
        'Overall_Status': 'Status',
        'Missing_Files': 'Missing Files',
        'Extra_Files': 'Extra Files',
        'File_Properties': 'File Properties',
        'Sbref_Direction': 'Sbref Direction',
        'IntendedFor': 'IntendedFor',
        'DWI_Parameters': 'DWI Parameters',
        'DWI_Version': 'DWI Version',
        'ASL_Version': 'ASL Version'
    }
    
    # Calculate column widths
    col_widths = {}
    for col in available_cols:
        header_width = len(clean_headers.get(col, col))
        data_width = table_df[col].astype(str).str.len().max() if not table_df.empty else 0
        col_widths[col] = min(max(header_width, data_width), 22)  # Cap width at 22 characters
    
    # Generate RST table
    rst_lines = []
    
    # Header separator
    separator = "+".join(["-" * (col_widths[col] + 2) for col in available_cols])
    rst_lines.append("+" + separator + "+")
    
    # Header row
    header_row = "|".join([f" {clean_headers.get(col, col):<{col_widths[col]}} " for col in available_cols])
    rst_lines.append("|" + header_row + "|")
    
    # Header separator
    rst_lines.append("+" + "=".join(["=" * (col_widths[col] + 2) for col in available_cols]) + "+")
    
    # Data rows
    for _, row in table_df.iterrows():
        data_row = "|".join([f" {str(row[col])[:col_widths[col]-1]:<{col_widths[col]}} " for col in available_cols])
        rst_lines.append("|" + data_row + "|")
    
    # Footer separator
    rst_lines.append("+" + separator + "+")
    
    return "\n".join(rst_lines)

def generate_dashboard_content(csv_file):
    """Generate the full dashboard content in RST format"""
    # Load data
    df = pd.read_csv(csv_file)
    
    # Generate statistics
    stats = generate_summary_stats(df)
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Generate dashboard content
    dashboard_content = f"""
Data Validation Dashboard
-------------------------

.. note::
   This dashboard is automatically updated when the ARI validation pipeline runs.
   Last updated: {timestamp}

Quick Summary
~~~~~~~~~~~~~

* **Total Subjects:** {stats['total_subjects']}
* **Passed:** {stats['subjects_passed']} ({stats['pass_rate']:.1f}%)
* **Issues Found:** {stats['subjects_with_issues']}

Validation Results Table
~~~~~~~~~~~~~~~~~~~~~~~~

{generate_rst_table(df)}

.. note::
   - **Status**: PASSED = No issues found, HAS ISSUES = One or more validation failures
   - **Missing Files/Extra Files/File Properties**: CORRECT = No issues, INCORRECT = Issues found
   - **DWI Parameters**: CORRECT = Parameters match between DWI and reverse phase-encode
   - **Version**: Version 1 (Deprecated) or Version 2 (Latest)

Download Complete Data
~~~~~~~~~~~~~~~~~~~~~~

For detailed validation information including specific file names and parameters:

.. raw:: html

   <div style="margin: 20px 0;">
     <a href="../_static/xnat_ari_dashboard.csv" 
        style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; 
               text-decoration: none; border-radius: 5px;">
       📥 Download Complete Dashboard Data (CSV)
     </a>
   </div>
"""
    
    return dashboard_content

def main():
    """Main function to generate dashboard"""
    csv_file = "xnat_ari_dashboard.csv"
    
    if not os.path.exists(csv_file):
        print(f"Error: CSV file {csv_file} not found")
        return 1
    
    print(f"Generating dashboard from {csv_file}")
    
    # Generate dashboard content
    dashboard_content = generate_dashboard_content(csv_file)
    
    # Save to file
    with open("dashboard_content.rst", "w") as f:
        f.write(dashboard_content)
    
    print("Dashboard content generated successfully")
    print("Files created:")
    print("- dashboard_content.rst")
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())