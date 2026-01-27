XNAT Pipelines Overview
=======================

We offer pipelines organized into three main categories: **Data Conversion**, **Quality Control**, and **Preprocessing**

.. image:: ../_static/3.0.pipeline.overview.png
   :alt: XNAT pipeline Structure
   :align: center
   :width: 900px

Data Conversion Pipelines
-------------------------

**dcm2niix**
- Converts DICOM files to NIfTI format
- Preserves acquisition metadata
- Industry standard conversion tool
- See: :doc:`dcm2niix`

**dcm2bids**
- Converts DICOM files to BIDS format
- Includes BIDS validation and quality checks
- Supports custom configuration files
- See: :doc:`dcm2bids`

**dcm2hcp** (Under Development)
- Converts DICOM files to HCP format
- Optimized for HCP pipeline
- See: :doc:`dcm2hcp`

Quality Control Pipelines
-------------------------

**mriqc**
- Comprehensive quality control for structural and functional MRI data
- Automated quality metrics and visual reports
- Group-level quality analysis and outlier detection
- See: :doc:`mriqc`

**ari-validator** (Project-Specific)
- Validates BIDS datasets for ARI project
- Checks file structure, metadata, and parameters
- Provides detailed validation reports
- See: :doc:`ari-validator`

Preprocessing Pipelines
-----------------------

**fmriprep**
- Robust fMRI preprocessing pipeline
- Runs on Jubail HPC cluster
- Produces analysis-ready derivatives
- See: :doc:`fmriprep`

**tractoflow**
- Processes diffusion MRI data
- See: :doc:`tractoflow`

**HCP Pipeline** (Under Development)
- Human Connectome Project-style processing
- See: :doc:`hcp-pipeline`

Next Steps
----------

- Learn about :doc:`../understanding_data/bids` format requirements
- See :doc:`../data_download/browser` for accessing pipeline outputs
- Explore individual pipeline documentation for detailed usage
- For general pipeline running instructions, see :doc:`../working_with_xnat/running_pipelines`