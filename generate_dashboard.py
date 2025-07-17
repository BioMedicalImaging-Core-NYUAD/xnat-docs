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
    dwi_v1 = len(df[df['DWI_Version'] == 'VERSION 1 (DEPRECATED)'])
    dwi_v2 = len(df[df['DWI_Version'] == 'VERSION 2 (LATEST)'])
    asl_v1 = len(df[df['ASL_Version'] == 'VERSION 1 (DEPRECATED)'])
    asl_v2 = len(df[df['ASL_Version'] == 'VERSION 2 (LATEST)'])
    
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

def generate_rst_table(df, max_rows=20):
    """Generate RST table from dataframe"""
    # Select key columns for the table
    table_cols = [
        'Subject_ID', 'Overall_Status', 'Missing_Files', 'Extra_Files', 
        'File_Properties', 'DWI_Parameters', 'DWI_Version', 'ASL_Version'
    ]
    
    # Filter dataframe
    table_df = df[table_cols].head(max_rows)
    
    # Calculate column widths
    col_widths = {}
    for col in table_cols:
        max_width = max(len(str(col)), table_df[col].astype(str).str.len().max())
        col_widths[col] = min(max_width, 25)  # Cap width at 25 characters
    
    # Generate RST table
    rst_lines = []
    
    # Header separator
    separator = "+".join(["-" * (col_widths[col] + 2) for col in table_cols])
    rst_lines.append("+" + separator + "+")
    
    # Header row
    header_row = "|".join([f" {col:<{col_widths[col]}} " for col in table_cols])
    rst_lines.append("|" + header_row + "|")
    
    # Header separator
    rst_lines.append("+" + separator + "+")
    
    # Data rows
    for _, row in table_df.iterrows():
        data_row = "|".join([f" {str(row[col]):<{col_widths[col]}} " for col in table_cols])
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

Overall Statistics
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 20px; margin: 20px 0;">
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
       <h4 style="margin: 0 0 10px 0; color: #28a745;">✅ Validation Summary</h4>
       <p style="margin: 5px 0;"><strong>Total Subjects:</strong> {stats['total_subjects']}</p>
       <p style="margin: 5px 0;"><strong>Passed:</strong> {stats['subjects_passed']} ({stats['pass_rate']:.1f}%)</p>
       <p style="margin: 5px 0;"><strong>Issues Found:</strong> {stats['subjects_with_issues']}</p>
     </div>
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #dc3545;">
       <h4 style="margin: 0 0 10px 0; color: #dc3545;">⚠️ Common Issues</h4>
       <p style="margin: 5px 0;"><strong>Missing Files:</strong> {stats['missing_files']} subjects</p>
       <p style="margin: 5px 0;"><strong>Extra Files:</strong> {stats['extra_files']} subjects</p>
       <p style="margin: 5px 0;"><strong>File Properties:</strong> {stats['file_properties']} subjects</p>
       <p style="margin: 5px 0;"><strong>DWI Parameters:</strong> {stats['dwi_params']} subjects</p>
     </div>
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #007bff;">
       <h4 style="margin: 0 0 10px 0; color: #007bff;">📊 Version Distribution</h4>
       <p style="margin: 5px 0;"><strong>DWI Version 1:</strong> {stats['dwi_v1']} subjects</p>
       <p style="margin: 5px 0;"><strong>DWI Version 2:</strong> {stats['dwi_v2']} subjects</p>
       <p style="margin: 5px 0;"><strong>ASL Version 1:</strong> {stats['asl_v1']} subjects</p>
       <p style="margin: 5px 0;"><strong>ASL Version 2:</strong> {stats['asl_v2']} subjects</p>
     </div>
   </div>

Recent Validation Results
~~~~~~~~~~~~~~~~~~~~~~~~~

The table below shows the most recent validation results for all subjects:

{generate_rst_table(df)}

.. note::
   - **Overall Status**: PASSED = No issues found, HAS ISSUES = One or more validation failures
   - **Missing Files**: Files required by BIDS/ARI standards that are absent
   - **Extra Files**: Unexpected files that may indicate processing issues
   - **File Properties**: Issues with image dimensions, TR values, or file sizes
   - **DWI Parameters**: Mismatches between DWI and reverse phase-encode parameters

Detailed Results
~~~~~~~~~~~~~~~~

For complete validation details including specific file names, dimensions, and parameter values, 
download the full dashboard data:

.. raw:: html

   <div style="margin: 20px 0;">
     <a href="../_static/xnat_ari_dashboard.csv" 
        style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; 
               text-decoration: none; border-radius: 5px; margin: 10px 0;">
       📥 Download Complete Dashboard Data (CSV)
     </a>
   </div>

Key Validation Criteria
~~~~~~~~~~~~~~~~~~~~~~~

The ARI validator checks for:

**File Structure Validation:**
- All required BIDS files are present
- No unexpected extra files
- Proper naming conventions

**Data Quality Checks:**
- Correct image dimensions for each modality
- Proper TR (repetition time) values
- File size validation

**ARI-Specific Requirements:**
- Sbref phase encoding directions
- Fieldmap IntendedFor field accuracy
- DWI parameter consistency
- Version compatibility (V1 vs V2)

**Current Standards:**
- DWI Version 2 (latest): 104 x 104 x 75 x 105 dimensions
- ASL Version 2 (latest): 128 x 128 x 48 x 25 dimensions
- M0scan handling: Separate files preferred

Interpreting Results
~~~~~~~~~~~~~~~~~~~~

**PASSED Status:**
All validation checks completed successfully. Data is ready for preprocessing.

**HAS ISSUES Status:**
One or more validation failures detected. Common issues include:

- **Missing Files**: Required BIDS files are absent
- **Extra Files**: Unexpected files that may interfere with processing
- **File Properties**: Incorrect dimensions, TR values, or file sizes
- **DWI Parameters**: Mismatches between DWI and reverse phase-encode parameters

**Version Information:**
- Version 1 (Deprecated): Older acquisition parameters
- Version 2 (Latest): Current recommended parameters

Next Steps for Issues
~~~~~~~~~~~~~~~~~~~~

If your data shows validation issues:

1. **Missing Files**: Check if files were properly converted from DICOM
2. **Extra Files**: Remove or relocate unexpected files
3. **File Properties**: Verify acquisition parameters match protocol
4. **DWI Parameters**: Ensure DWI and fieldmap parameters are consistent
5. **Version Compatibility**: Consider updating to Version 2 parameters

For technical support, see the :doc:`../support/troubleshooting` page.
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