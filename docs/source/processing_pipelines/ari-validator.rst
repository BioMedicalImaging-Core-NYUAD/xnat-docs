ari-validator 
=============
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.

The ari-validator pipeline validates BIDS datasets for ARI (Affective Brain and Reward Imaging) compliance and ensures data quality.

Overview
--------

The ari-validator provides:
- BIDS structure validation
- ARI-specific compliance checking
- Detailed validation reports
- Quality control metrics
- Integration with XNAT workflows

Features
--------

- **BIDS Validation:** Ensures data adheres to BIDS standards
- **ARI Compliance:** Specialized validation for ARI lab requirements
- **Comprehensive Reporting:** Detailed validation logs and summaries
- **Quality Control:** File integrity and parameter checking
- **Integration:** Seamless integration with XNAT processing workflows

Validation Steps
----------------

The validator performs these checks:

1. **Required Files Presence:** Verifies all necessary files exist
2. **Unexpected Extra Files:** Identifies files that shouldn't be present
3. **NIFTI Properties:** Checks image dimensions, TR, and other parameters
4. **Sbref Phase Encoding:** Validates phase encoding directions
5. **Fieldmap IntendedFor:** Ensures proper fieldmap associations
6. **DWI Parameter Matching:** Verifies diffusion parameter consistency

Input Requirements
------------------

**Required:**
- BIDS-formatted dataset
- Python 3 environment
- FreeSurfer (mri_info command must be available)

**Supported Data Types:**
- Structural MRI (T1w, T2w)
- Functional MRI (task, resting-state)
- Diffusion MRI (DWI)
- Fieldmap data

How to Run
----------

**Basic Validation:**
.. code-block:: bash

   python aricheck.py /path/to/bids/directory


**Ignore DWI Parameter Mismatches:**
.. code-block:: bash

   python aricheck.py --ignoredwi /path/to/bids/directory


**XNAT Interface:**

For general instructions on running pipelines, see: :doc:`../working_with_xnat/running_pipelines`

**Pipeline-Specific Parameters:**
- **BIDS Directory:** Path to BIDS dataset for validation
- **Validation Mode:** Standard or strict compliance checking
- **Ignore DWI:** Option to skip DWI parameter validation
- **Output Location:** Where to save validation reports

Output and Reports
------------------

**Validation Log:**
- Creates `ari_validation.log` in current directory
- Returns 0 if validation passes, 1 if fails
- Detailed summary of findings

**Report Contents:**
- Missing files summary
- Extra files identification
- NIFTI properties validation
- Phase encoding direction checks
- IntendedFor field validation
- DWI parameter matching results

Data Validation Dashboard
-------------------------

.. note::
   This dashboard is automatically updated when the ARI validation pipeline runs.
   Last updated: 2025-07-17 16:48:04 UTC

Quick Summary
~~~~~~~~~~~~~

* **Total Subjects:** 2
* **Passed:** 0 (0.0%)
* **Issues Found:** 0

Validation Results Table
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+---------+---------------+-------------+-----------------+-----------------+-------------+----------------+-------------+-------------+
| Subject ID   | Status  | Missing Files | Extra Files | File Properties | Sbref Direction | IntendedFor | DWI Parameters | DWI Version | ASL Version |
+=====================================================================================================================================================+
| Subject_041  | CORREC  | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | VERSION 2      | VERSION 2   | SEPARATE    |
| Subject_045  | CORREC  | CORRECT       | CORRECT     | CORRECT         | CORRECT         | INCORRECT   | VERSION 1      | VERSION 2   | SEPARATE    |
+--------------+---------+---------------+-------------+-----------------+-----------------+-------------+----------------+-------------+-------------+

.. note::
   - **Status**: PASSED = No issues found, HAS ISSUES = One or more validation failures
   - **Missing Files/Extra Files/File Properties**: CORRECT = No issues, INCORRECT = Issues found
   - **DWI Parameters**: CORRECT = Parameters match between DWI and reverse phase-encode
   - **Version**: Version 1 (Deprecated) or Version 2 (Latest)

Download Complete Data
~~~~~~~~~~~~~~~~~~~~~

For detailed validation information including specific file names and parameters:

.. raw:: html

   <div style="margin: 20px 0;">
     <a href="../_static/xnat_ari_dashboard.csv" 
        style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; 
               text-decoration: none; border-radius: 5px;">
       📥 Download Complete Dashboard Data (CSV)
     </a>
   </div>

Quick Summary
~~~~~~~~~~~~~

* **Total Subjects:** 2
* **Passed:** 0 (0.0%)
* **Issues Found:** 0

Validation Results Table
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+---------+---------------+-------------+-----------------+-----------------+-------------+------------------------+--------------------+-------------+
| Subject ID   | Status  | Missing Files | Extra Files | File Properties | Sbref Direction | IntendedFor | DWI Parameters         | DWI Version        | ASL Version |
+====================================================================================================================================================================+
| Subject_041  | CORREC  | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | VERSION 2 (LATEST)     | VERSION 2 (LATEST  | SEPARATE    |
| Subject_045  | CORREC  | CORRECT       | CORRECT     | CORRECT         | CORRECT         | INCORRECT   | VERSION 1 (DEPRECATED  | VERSION 2 (LATEST  | SEPARATE    |
+--------------+---------+---------------+-------------+-----------------+-----------------+-------------+------------------------+--------------------+-------------+

.. note::
   - **Status**: PASSED = No issues found, HAS ISSUES = One or more validation failures
   - **Missing Files/Extra Files/File Properties**: CORRECT = No issues, INCORRECT = Issues found
   - **DWI Parameters**: CORRECT = Parameters match between DWI and reverse phase-encode
   - **Version**: Version 1 (Deprecated) or Version 2 (Latest)

Download Complete Data
~~~~~~~~~~~~~~~~~~~~~

For detailed validation information including specific file names and parameters:

.. raw:: html

   <div style="margin: 20px 0;">
     <a href="../_static/xnat_ari_dashboard.csv" 
        style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; 
               text-decoration: none; border-radius: 5px;">
       📥 Download Complete Dashboard Data (CSV)
     </a>
   </div>

Quick Summary
~~~~~~~~~~~~~

* **Total Subjects:** 2
* **Passed:** 0 (0.0%)
* **Issues Found:** 0

Validation Results Table
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+---------+---------------+-------------+-----------------+-----------------+-------------+----------------------+--------------------+-------------+
| Subject ID   | Status  | Missing Files | Extra Files | File Properties | Sbref Direction | IntendedFor | DWI Parameters       | DWI Version        | ASL Version |
+==================================================================================================================================================================+
| Subject_0414 | CORRECT | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | VERSION 2 (LATEST)   | VERSION 2 (LATEST) | SEPARATE    |
| Subject_0457 | CORRECT | CORRECT       | CORRECT     | CORRECT         | CORRECT         | INCORRECT   | VERSION 1 (DEPRECATE | VERSION 2 (LATEST) | SEPARATE    |
+--------------+---------+---------------+-------------+-----------------+-----------------+-------------+----------------------+--------------------+-------------+

.. note::
   - **Status**: PASSED = No issues found, HAS ISSUES = One or more validation failures
   - **Missing Files/Extra Files/File Properties**: CORRECT = No issues, INCORRECT = Issues found
   - **DWI Parameters**: CORRECT = Parameters match between DWI and reverse phase-encode
   - **Version**: Version 1 (Deprecated) or Version 2 (Latest)

Download Complete Data
~~~~~~~~~~~~~~~~~~~~~

For detailed validation information including specific file names and parameters:

.. raw:: html

   <div style="margin: 20px 0;">
     <a href="../_static/xnat_ari_dashboard.csv" 
        style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; 
               text-decoration: none; border-radius: 5px;">
       📥 Download Complete Dashboard Data (CSV)
     </a>
   </div>

Project Validation Status
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 20px; margin: 20px 0;">
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
       <h4 style="margin: 0 0 10px 0; color: #28a745;">✅ Validation Summary</h4>
       <p style="margin: 5px 0;"><strong>Status:</strong> Dashboard will show live data</p>
       <p style="margin: 5px 0;"><strong>Total Subjects:</strong> Automatically updated</p>
       <p style="margin: 5px 0;"><strong>Pass Rate:</strong> Real-time calculation</p>
     </div>
     <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #17a2b8;">
       <h4 style="margin: 0 0 10px 0; color: #17a2b8;">📊 Live Dashboard Features</h4>
       <p style="margin: 5px 0;">• Real-time validation statistics</p>
       <p style="margin: 5px 0;">• Subject-by-subject results table</p>
       <p style="margin: 5px 0;">• Downloadable detailed reports</p>
       <p style="margin: 5px 0;">• Automatic updates on pipeline runs</p>
     </div>
   </div>

How the Dashboard Works
~~~~~~~~~~~~~~~~~~~~~~~

The dashboard automatically updates when:

1. **ARI Validation Pipeline Runs**: Each time validation is executed
2. **GitHub Action Triggers**: Manual or automated workflow execution
3. **Data Processing**: CSV data is processed and formatted for display
4. **Documentation Updates**: ReadTheDocs rebuilds with new content

**Dashboard Components:**

- **Summary Statistics**: Overall pass/fail rates and issue counts
- **Results Table**: Subject-by-subject validation status
- **Detailed Reports**: Downloadable CSV with full validation details
- **Version Tracking**: DWI and ASL version distribution
- **Issue Breakdown**: Categorized validation failures

**Data Sources:**
The dashboard pulls data from validation files located at:
``/Volumes/CTP-XNAT/xnat-main/xnat-data/archive/rokerslab_ari-hfs_2024_001/*/RESOURCES/ari-validation/``

Troubleshooting
---------------

**Common Issues:**
- [PLACEHOLDER - Missing file errors]
- [PLACEHOLDER - Parameter mismatch problems]
- [PLACEHOLDER - FreeSurfer dependency issues]

**Error Resolution:**
- [PLACEHOLDER - How to fix common validation failures]
- [PLACEHOLDER - When to ignore specific warnings]

Next Steps
----------

- Fix any validation errors identified
- Proceed with preprocessing using :doc:`fmriprep` or :doc:`tractoflow`
- Learn about :doc:`../understanding_data/bids` format requirements
- See :doc:`../data_download/browser` for accessing validated data