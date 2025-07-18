ari-validator 
=============
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.

The ari-validator pipeline validates BIDS datasets for project ARI. 
Similar pipelines can be created for your projects if you have specific requirements for your scans and want to have a way to validate your data before spending time on preprocessing. A dashboard is also provided to track the status of your data.

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

   <div class="dashboard-container" style="max-height: 400px; overflow-y: auto; border: 1px solid #ddd; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
     <table class="dashboard-table" style="width: 100%; border-collapse: collapse; font-size: 0.9em;">
       <thead style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; position: sticky; top: 0; z-index: 10;">
         <tr>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Subject ID</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Status</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Missing Files</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Extra Files</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">File Properties</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Sbref Direction</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">IntendedFor</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">DWI Parameters</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">DWI Version</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">ASL Version</th>
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
         
         // Add hover effect and alternating row colors
         row.style.cursor = 'pointer';
         row.style.backgroundColor = i % 2 === 0 ? '#f8f9fa' : 'white';
         row.onmouseover = function() { 
           this.style.backgroundColor = '#e3f2fd'; 
           this.style.transform = 'scale(1.02)';
           this.style.transition = 'all 0.2s ease';
         };
         row.onmouseout = function() { 
           this.style.backgroundColor = i % 2 === 0 ? '#f8f9fa' : 'white';
           this.style.transform = 'scale(1)';
         };
         
         for (let j = 0; j < columns.length; j++) {
           const cell = document.createElement('td');
           cell.style.padding = '10px 8px';
           cell.style.border = '1px solid #ddd';
           cell.style.fontSize = '0.85em';
           cell.style.transition = 'all 0.2s ease';
           
           let cellContent = columns[j].trim();
           
           // Color code status column (index 1)
           if (j === 1) {
             cell.style.fontWeight = '600';
             if (cellContent === 'PASSED') {
               cell.style.backgroundColor = '#d4edda';
               cell.style.color = '#155724';
               cell.style.borderColor = '#c3e6cb';
               cellContent = '✅ PASSED';
             } else if (cellContent === 'HAS ISSUES') {
               cell.style.backgroundColor = '#f8d7da';
               cell.style.color = '#721c24';
               cell.style.borderColor = '#f5c6cb';
               cellContent = '❌ HAS ISSUES';
             } else if (cellContent === 'MULTIPLE SESSION') {
               cell.style.backgroundColor = '#fff3cd';
               cell.style.color = '#856404';
               cell.style.borderColor = '#ffeaa7';
               cellContent = '⚠️ MULTIPLE SESSION';
             } else if (cellContent.includes('Validation Outdated')) {
               cell.style.backgroundColor = '#e2e3e5';
               cell.style.color = '#6c757d';
               cell.style.borderColor = '#d1ecf1';
               cellContent = '🔄 OUTDATED';
             }
           }
           
           // Color code validation columns (indices 2-7)
           if (j >= 2 && j <= 7) {
             if (cellContent === 'CORRECT') {
               cell.style.backgroundColor = '#d1f2eb';
               cell.style.color = '#0c5460';
               cell.style.borderColor = '#bee5eb';
               cellContent = '✓ CORRECT';
             } else if (cellContent === 'INCORRECT') {
               cell.style.backgroundColor = '#f8d7da';
               cell.style.color = '#721c24';
               cell.style.borderColor = '#f5c6cb';
               cellContent = '✗ INCORRECT';
             } else if (cellContent === '' || cellContent === 'nan') {
               cell.style.backgroundColor = '#f8f9fa';
               cell.style.color = '#6c757d';
               cellContent = '—';
             }
           }
           
           // Color code version columns (indices 8-9)
           if (j >= 8 && j <= 9) {
             if (cellContent.includes('v2') || cellContent.includes('LATEST')) {
               cell.style.backgroundColor = '#d4edda';
               cell.style.color = '#155724';
               cell.style.borderColor = '#c3e6cb';
               cellContent = '🟢 v2 (LATEST)';
             } else if (cellContent.includes('v1') || cellContent.includes('DEPRECATED')) {
               cell.style.backgroundColor = '#fff3cd';
               cell.style.color = '#856404';
               cell.style.borderColor = '#ffeaa7';
               cellContent = '🟡 v1 (DEPRECATED)';
             } else if (cellContent === 'UNKNOWN' || cellContent === '' || cellContent === 'nan') {
               cell.style.backgroundColor = '#f8f9fa';
               cell.style.color = '#6c757d';
               cellContent = '❓ UNKNOWN';
             }
           }
           
           // Truncate long text and add tooltip
           if (cellContent.length > 20) {
             cell.title = cellContent; // Show full text on hover
             cellContent = cellContent.substring(0, 17) + '...';
           }
           
           cell.textContent = cellContent;
           row.appendChild(cell);
         }
         
         tbody.appendChild(row);
       }
       
       // Add row count info
       const totalRows = lines.length - 1;
       const infoDiv = document.createElement('div');
       infoDiv.style.textAlign = 'center';
       infoDiv.style.marginTop = '10px';
       infoDiv.style.fontSize = '0.9em';
       infoDiv.style.color = '#6c757d';
       infoDiv.innerHTML = `<strong>Total subjects: ${totalRows}</strong> • Scroll within table to view all rows`;
       document.querySelector('.dashboard-container').parentNode.appendChild(infoDiv);
     })
     .catch(error => {
       console.error('Error loading CSV data:', error);
       document.getElementById('dashboard-table-body').innerHTML = 
         '<tr><td colspan="10" style="text-align: center; padding: 20px; color: #dc3545;">Error loading data. Please download the CSV file below.</td></tr>';
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