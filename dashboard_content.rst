
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
