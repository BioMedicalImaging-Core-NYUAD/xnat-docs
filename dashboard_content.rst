
Data Validation Dashboard
-------------------------

.. note::
   This dashboard is automatically updated when the ARI validation pipeline runs.
   Last updated: 2025-07-17 16:38:42 UTC

Overall Statistics
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 20px; margin: 20px 0;">
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
       <h4 style="margin: 0 0 10px 0; color: #28a745;">✅ Validation Summary</h4>
       <p style="margin: 5px 0;"><strong>Total Subjects:</strong> 382</p>
       <p style="margin: 5px 0;"><strong>Passed:</strong> 92 (24.1%)</p>
       <p style="margin: 5px 0;"><strong>Issues Found:</strong> 274</p>
     </div>
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #dc3545;">
       <h4 style="margin: 0 0 10px 0; color: #dc3545;">⚠️ Common Issues</h4>
       <p style="margin: 5px 0;"><strong>Missing Files:</strong> 69 subjects</p>
       <p style="margin: 5px 0;"><strong>Extra Files:</strong> 32 subjects</p>
       <p style="margin: 5px 0;"><strong>File Properties:</strong> 71 subjects</p>
       <p style="margin: 5px 0;"><strong>DWI Parameters:</strong> 226 subjects</p>
     </div>
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #007bff;">
       <h4 style="margin: 0 0 10px 0; color: #007bff;">📊 Version Distribution</h4>
       <p style="margin: 5px 0;"><strong>DWI Version 1:</strong> 182 subjects</p>
       <p style="margin: 5px 0;"><strong>DWI Version 2:</strong> 98 subjects</p>
       <p style="margin: 5px 0;"><strong>ASL Version 1:</strong> 135 subjects</p>
       <p style="margin: 5px 0;"><strong>ASL Version 2:</strong> 181 subjects</p>
     </div>
   </div>

Recent Validation Results
~~~~~~~~~~~~~~~~~~~~~~~~~

The table below shows the most recent validation results for all subjects:

+------------+----------------+---------------+-------------+-----------------+----------------+------------------------+------------------------+
| Subject_ID | Overall_Status | Missing_Files | Extra_Files | File_Properties | DWI_Parameters | DWI_Version            | ASL_Version            |
+------------+----------------+---------------+-------------+-----------------+----------------+------------------------+------------------------+
| sub-0017   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0021   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0097   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 2 (LATEST)     |
| sub-0161   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0183   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0200   | Unknown        | CORRECT       | CORRECT     | CORRECT         | CORRECT        | UNKNOWN                | UNKNOWN                |
| sub-0200   | HAS ISSUES     | INCORRECT     | CORRECT     | CORRECT         | INCORRECT      | UNKNOWN                | UNKNOWN                |
| sub-0200   | HAS ISSUES     | INCORRECT     | CORRECT     | CORRECT         | INCORRECT      | UNKNOWN                | UNKNOWN                |
| sub-0200   | HAS ISSUES     | INCORRECT     | CORRECT     | CORRECT         | INCORRECT      | UNKNOWN                | UNKNOWN                |
| sub-0201   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0203   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0204   | HAS ISSUES     | CORRECT       | CORRECT     | INCORRECT       | CORRECT        | UNKNOWN                | VERSION 2 (LATEST)     |
| sub-0213   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0238   | PASSED         | CORRECT       | CORRECT     | CORRECT         | CORRECT        | VERSION 2 (LATEST)     | VERSION 2 (LATEST)     |
| sub-0239   | HAS ISSUES     | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT      | UNKNOWN                | UNKNOWN                |
| sub-0248   | HAS ISSUES     | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT      | UNKNOWN                | UNKNOWN                |
| sub-0250   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 1 (DEPRECATED) |
| sub-0254   | HAS ISSUES     | CORRECT       | CORRECT     | CORRECT         | INCORRECT      | VERSION 1 (DEPRECATED) | VERSION 2 (LATEST)     |
| sub-0255   | HAS ISSUES     | INCORRECT     | INCORRECT   | INCORRECT       | INCORRECT      | UNKNOWN                | UNKNOWN                |
| sub-0261   | HAS ISSUES     | INCORRECT     | INCORRECT   | INCORRECT       | INCORRECT      | UNKNOWN                | UNKNOWN                |
+------------+----------------+---------------+-------------+-----------------+----------------+------------------------+------------------------+

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
