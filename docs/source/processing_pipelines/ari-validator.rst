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