ari-validator 
=============
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.

The ari-validator pipeline validates ARI project datasets by checking BIDS and ARI-specific compliance, producing a detailed log file which can be used to track the status of your data.

Similar validation pipelines can be created for your projects if you have specific requirements for your scans and want to have a way to validate your data before spending time on preprocessing. 

Validation Steps
----------------

1. **Sbref Phase Encoding:** Validates phase encoding directions of sbref scans. 
2. **Fieldmap IntendedFor:** Ensures bold images are associated with the correct fieldmap.
3. **DWI Parameter Matching:** Verifies diffusion parameter between DWI and reverse b0.
4. **NIFTI Properties:** Checks image dimensions, TR, and other parameters
5. **Required Files Presence:** Verifies all necessary files exist
6. **Unexpected Extra Files:** Identifies files that shouldn't be present
7. **Protocol Version:** Checks the version of of the protocol used for the DWI and ASL scans.


Input Requirements
------------------

**Required:**
- :doc:`dcm2bids` must have been run on the data before running the ari-validator pipeline.

How to Launch the Pipeline
--------------------------
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.


Output and Reports
------------------

**Validation Log:**
- Creates `ari-validation-details.txt` in session directory with detailed logs

.. raw:: html

   <style>
     /* overall container */
     .two-col{
       display: flex;
       gap: 20px;              /* space between the two panes */
       width: 680px;           /* total width as requested */
       margin: 20px auto;      /* centre the whole block */
     }

     /* generic scrollable pane */
     .scroll-box{
       flex: 1 1 0;            /* grow & shrink evenly */
       width: 340px;           /* each column 340px wide */
       height: 300px;          /* height as requested */
       overflow-y: auto;
       border: 1px solid #ccc;
       padding: 10px;
       margin: 0;
       background-color: #f8f9fa;
       border-radius: 4px;
       font-family: monospace;
       font-size: 12px;
       line-height: 1.4;
     }
     
     .scroll-box h3 {
       margin: 0 0 10px 0;
       padding: 8px;
       background-color: #e9ecef;
       border-radius: 4px;
       font-size: 14px;
       font-weight: bold;
       text-align: center;
     }
   </style>

   <div class="two-col">
     <div class="scroll-box">
       <h3>Example log of valid data</h3>
       <iframe src="../_static/3.5.ari-validation-details-good.txt" 
               style="width: 100%; height: 250px; border: none; background: white;">
       </iframe>
     </div>
     <div class="scroll-box">
       <h3>Example log of data with issues</h3>
       <iframe src="../_static/3.5.ari-validation-details-bad.txt" 
               style="width: 100%; height: 250px; border: none; background: white;">
       </iframe>
     </div>
   </div>

*can you tell what is wrong with the data on the right?*



Data Validation Dashboard
-------------------------

.. raw:: html

   <div id="validation-summary" style="margin-bottom: 10px;">
     Loading validation summary...
   </div>

   <script>
   // Load validation summary from text file
   fetch('../_static/validation_summary.txt')
     .then(response => response.text())
     .then(data => {
       document.getElementById('validation-summary').innerHTML = data.trim();
     })
     .catch(error => {
       console.error('Error loading validation summary:', error);
       document.getElementById('validation-summary').innerHTML = 'The ARI validation pipeline has been run on subjects. The following dashboard shows the current status. This dashboard is updated daily at 3:00 AM Abu Dhabi time.';
     });
   </script>

.. raw:: html

   <div class="dashboard-container" style="max-height: 400px; overflow-y: auto; border: 1px solid #ddd; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
     <table class="dashboard-table" style="width: 100%; border-collapse: collapse; font-size: 0.9em;">
       <thead style="background: linear-gradient(135deg, #6c757d 0%, #495057 100%); color: white; position: sticky; top: 0; z-index: 10;">
         <tr>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Subject ID</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Status</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Sbref Direction</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">IntendedFor</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">DWI Parameters</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">File Properties</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Missing Files</th>
           <th style="padding: 12px 8px; border: 1px solid #ddd; text-align: left; font-weight: 600;">Extra Files</th>
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
       document.querySelector('.dashboard-container').parentNode.appendChild(infoDiv);
     })
     .catch(error => {
       console.error('Error loading CSV data:', error);
       document.getElementById('dashboard-table-body').innerHTML = 
         '<tr><td colspan="10" style="text-align: center; padding: 20px; color: #dc3545;">Error loading data. Please download the CSV file below.</td></tr>';
     });
   </script>

*For detailed validation information including specific file names and parameters:*

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

- **SBREF:** Sometimes the phase encoding directions is flipped even though the the AP/PA direction in the file name is correct. You should delete the incorrect sbref files. 
- **IntendedFor:** Check the intendedFor field in the epi.json file in fmap and see exacly what is incorrect. First thing to check is if there's missing or extra files. If that's not the issue, then please contact us and we can help you take a look.
- **DWI Parameters:** Version 1 of the DWI protocol is deprecated due to mismatches in the DWI and reverse b0 parameters. If someone was not scanned under version 1 yet still has mismatching issues then you need to investigate further. 
- **Incorrect dimensions and TR:** Check if data is incomplete or if wrong sequence was used.
- **Missing files:** transfer missing files to the correct location.
- **Extra files:** delete extra files depending on the reason.


Next Steps
----------

- Fix any validation errors identified
- Proceed with preprocessing using :doc:`fmriprep` or :doc:`tractoflow`
- Learn about :doc:`../understanding_data/bids` format requirements
- See :doc:`../data_download/browser` for accessing validated data