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
   Last updated: 2025-07-18 18:59:45 UTC

Quick Summary
~~~~~~~~~~~~~

* **Total Subjects:** 375
* **Passed:** 91 (24.3%)
* **Issues Found:** 247

Validation Results Table
~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------+---------------+-------------+-----------------+-----------------+-------------+----------------+-----------------+-----------------+
| Subject ID | Status              | Missing Files | Extra Files | File Properties | Sbref Direction | IntendedFor | DWI Parameters | DWI Version     | ASL Version     |
+=======================================================================================================================================================================+
| sub-0017   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0021   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0097   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | INCORRECT       | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v2 (LATEST)     |
| sub-0161   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0183   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0200   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0201   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0203   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0204   | HAS ISSUES          | CORRECT       | CORRECT     | INCORRECT       | CORRECT         | CORRECT     | CORRECT        | UNKNOWN         | v2 (LATEST)     |
| sub-0213   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0238   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0239   | HAS ISSUES          | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0248   | HAS ISSUES          | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0250   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0254   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | INCORRECT       | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v2 (LATEST)     |
| sub-0255   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0261   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0263   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0285   | Validation Outdate  | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0286   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0302   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0303   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0308   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0314   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0325   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0326   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0327   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0328   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0329   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0332   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0333   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0339   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0340   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0342   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0343   | HAS ISSUES          | CORRECT       | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0344   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0345   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0348   | HAS ISSUES          | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0354   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0357   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | INCORRECT   | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0358   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0359   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0360   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0361   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0363   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0365   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0366   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0368   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0370   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0375   | HAS ISSUES          | INCORRECT     | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
+------------+---------------------+---------------+-------------+-----------------+-----------------+-------------+----------------+-----------------+-----------------+

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

Quick Summary
~~~~~~~~~~~~~

* **Total Subjects:** 375
* **Passed:** 91 (24.3%)
* **Issues Found:** 247

Validation Results Table
~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------+---------------+-------------+-----------------+-----------------+-------------+----------------+-----------------+-----------------+
| Subject ID | Status              | Missing Files | Extra Files | File Properties | Sbref Direction | IntendedFor | DWI Parameters | DWI Version     | ASL Version     |
+=======================================================================================================================================================================+
| sub-0017   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0021   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0097   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | INCORRECT       | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v2 (LATEST)     |
| sub-0161   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0183   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0200   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0201   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0203   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0204   | HAS ISSUES          | CORRECT       | CORRECT     | INCORRECT       | CORRECT         | CORRECT     | CORRECT        | UNKNOWN         | v2 (LATEST)     |
| sub-0213   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0238   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0239   | HAS ISSUES          | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0248   | HAS ISSUES          | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0250   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0254   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | INCORRECT       | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v2 (LATEST)     |
| sub-0255   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0261   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0263   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0285   | Validation Outdate  | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | UNKNOWN         | UNKNOWN         |
| sub-0286   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0302   | PASSED              | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | CORRECT        | v2 (LATEST)     | v2 (LATEST)     |
| sub-0303   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0308   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0314   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0325   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0326   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0327   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0328   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0329   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0332   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0333   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0339   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0340   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0342   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0343   | HAS ISSUES          | CORRECT       | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0344   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | CORRECT     | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0345   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0348   | HAS ISSUES          | INCORRECT     | CORRECT     | INCORRECT       | INCORRECT       | INCORRECT   | INCORRECT      | UNKNOWN         | UNKNOWN         |
| sub-0354   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0357   | HAS ISSUES          | INCORRECT     | INCORRECT   | INCORRECT       | CORRECT         | INCORRECT   | INCORRECT      | v1 (DEPRECATED  | UNKNOWN         |
| sub-0358   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0359   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0360   | MULTIPLE SESSION    | nan           | nan         | nan             | nan             | nan         | nan            | nan             | nan             |
| sub-0361   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0363   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0365   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0366   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0368   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0370   | HAS ISSUES          | CORRECT       | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
| sub-0375   | HAS ISSUES          | INCORRECT     | CORRECT     | CORRECT         | CORRECT         | CORRECT     | INCORRECT      | v1 (DEPRECATED  | v1 (DEPRECATED  |
+------------+---------------------+---------------+-------------+-----------------+-----------------+-------------+----------------+-----------------+-----------------+

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

Quick Summary
~~~~~~~~~~~~~

The ARI validation pipeline has been run on all available subjects. The results show the current status of BIDS compliance and data quality across the dataset.

Validation Results
~~~~~~~~~~~~~~~~~~

The table below shows a summary of validation results for all subjects. The table displays 15 rows at a time - scroll within the table to view more subjects. For complete details including specific file names and parameters, download the full CSV file.

.. raw:: html

   <div class="dashboard-container" style="max-height: 400px; overflow-y: auto; border: 1px solid #ddd; margin: 20px 0;">
     <table class="dashboard-table" style="width: 100%; border-collapse: collapse; font-size: 0.9em;">
       <thead style="background-color: #f5f5f5; position: sticky; top: 0; z-index: 10;">
         <tr>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Subject ID</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Status</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Missing Files</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Extra Files</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">File Properties</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Sbref Direction</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">IntendedFor</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">DWI Parameters</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">DWI Version</th>
           <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">ASL Version</th>
         </tr>
       </thead>
       <tbody id="dashboard-table-body">
         <!-- Table content will be loaded by JavaScript -->
       </tbody>
     </table>
   </div>

   <script>
   // Load CSV data and populate table
   fetch('../_static/xnat_ari_dashboard_display.csv')
     .then(response => response.text())
     .then(data => {
       const lines = data.trim().split('\n');
       const tbody = document.getElementById('dashboard-table-body');
       
       // Skip header row (index 0)
       for (let i = 1; i < lines.length; i++) {
         const columns = lines[i].split(',');
         const row = document.createElement('tr');
         
         // Add hover effect
         row.style.cursor = 'pointer';
         row.onmouseover = function() { this.style.backgroundColor = '#f9f9f9'; };
         row.onmouseout = function() { this.style.backgroundColor = ''; };
         
         for (let j = 0; j < columns.length; j++) {
           const cell = document.createElement('td');
           cell.style.padding = '8px';
           cell.style.border = '1px solid #ddd';
           cell.style.fontSize = '0.85em';
           
           let cellContent = columns[j];
           
           // Color code status column
           if (j === 1) { // Status column
             if (cellContent === 'PASSED') {
               cell.style.backgroundColor = '#d4edda';
               cell.style.color = '#155724';
             } else if (cellContent === 'HAS ISSUES') {
               cell.style.backgroundColor = '#f8d7da';
               cell.style.color = '#721c24';
             } else if (cellContent === 'Unknown') {
               cell.style.backgroundColor = '#fff3cd';
               cell.style.color = '#856404';
             }
           }
           
           // Color code other status columns
           if (j >= 2 && j <= 7) { // Status columns
             if (cellContent === 'CORRECT') {
               cell.style.backgroundColor = '#d4edda';
               cell.style.color = '#155724';
             } else if (cellContent === 'INCORRECT') {
               cell.style.backgroundColor = '#f8d7da';
               cell.style.color = '#721c24';
             }
           }
           
           // Truncate long text
           if (cellContent.length > 20) {
             cell.title = cellContent; // Show full text on hover
             cellContent = cellContent.substring(0, 17) + '...';
           }
           
           cell.textContent = cellContent;
           row.appendChild(cell);
         }
         
         tbody.appendChild(row);
       }
     })
     .catch(error => {
       console.error('Error loading CSV data:', error);
       document.getElementById('dashboard-table-body').innerHTML = 
         '<tr><td colspan="10" style="text-align: center; padding: 20px;">Error loading data. Please download the CSV file below.</td></tr>';
     });
   </script>


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