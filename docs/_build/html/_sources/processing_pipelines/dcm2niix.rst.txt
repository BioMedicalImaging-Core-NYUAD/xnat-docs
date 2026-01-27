dcm2niix 
========
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`. For running pipelines across multiple subjects in parallel, see :doc:`../working_with_xnat/parallel_processing`.

The dcm2niix pipeline converts DICOM files to NIfTI format for analysis compatibility.

Overview
--------

The dcm2niix pipeline provides:
- DICOM to NIfTI conversion using the industry-standard dcm2niix tool
- Metadata preservation in JSON sidecar files
- Automatic handling of multi-echo and complex data
- Quality control and validation checks

Input Requirements
------------------

**Required:**
- DICOM files organized in XNAT sessions
- Valid XNAT project with appropriate permissions

**Supported Data Types:**
- Structural MRI (T1w, T2w, FLAIR, etc.)
- Functional MRI (BOLD, ASL)
- Diffusion MRI (DWI, DTI)
- Fieldmap data

How to Run
----------

For general instructions on running pipelines, see: :doc:`../working_with_xnat/running_pipelines`

**Pipeline-Specific Parameters:**
- **Output format:** NIfTI (.nii.gz)
- **Metadata export:** JSON sidecar files
- **Naming convention:** BIDS-compatible names
- **Quality control:** Automatic validation

Output Structure
----------------

**Generated Files:**
- ``*.nii.gz`` - NIfTI image files
- ``*.json`` - Metadata sidecar files
- ``conversion_report.txt`` - Conversion log
- ``validation_summary.html`` - Quality control report

**File Organization:**
- Files organized by scan type and sequence
- Consistent naming across subjects
- Metadata preserved in JSON format

Troubleshooting
---------------

**Common Issues:**
- **Incomplete conversions:** Check for corrupted DICOM files
- **Missing metadata:** Verify DICOM header completeness
- **Orientation issues:** Review spatial orientation settings

**Quality Control:**
- Verify image orientation and dimensions
- Check metadata completeness
- Validate conversion accuracy

Next Steps
----------

- Organize converted NIfTI files using :doc:`dcm2bids`
- Run quality control with :doc:`ari-validator`
- Proceed with preprocessing pipelines
- Learn about NIfTI format from the `official NIfTI documentation <https://nifti.nimh.nih.gov/>`_