What is NYUAD XNAT?
===================

XNAT (eXtensible Neuroimaging Archive Toolkit) is an open-source platform for managing neuroimaging research data. At NYU Abu Dhabi, we use XNAT to store, organize, process, and share MRI data from our research projects.

What is XNAT?
-------------

XNAT is a web-based data management platform specifically designed for neuroimaging research. It provides:

- **Centralized Data Storage**: Secure, organized storage for MRI scans and related data
- **Data Organization**: Hierarchical structure (Projects → Subjects → Sessions → Scans) that matches research workflows
- **Automated Processing**: Integrated pipelines for data conversion, quality control, and preprocessing
- **Collaboration Tools**: Easy sharing and access control for research teams
- **Web Interface**: Access your data from anywhere through a browser

Why Do We Use XNAT at NYUAD?
----------------------------

XNAT helps our research community by:

**1. Streamlining Data Management**
   - Automatically receives DICOM files directly from MRI scanners
   - Organizes data in a consistent structure across all projects
   - Eliminates the need for manual file organization

**2. Enabling Automated Processing**
   - Runs preprocessing pipelines (like fMRIPrep, MRIQC) directly on stored data
   - Converts data between formats (DICOM → NIfTI → BIDS) automatically
   - Processes data on our HPC cluster without manual file transfers

**3. Facilitating Collaboration**
   - Multiple researchers can access the same data securely
   - Project-based access control ensures data privacy
   - Shared resources and configurations across team members

**4. Ensuring Data Quality**
   - Built-in quality control pipelines (MRIQC, ARI-validator)
   - Validation checks ensure data meets analysis requirements
   - Quality reports help identify issues early

**5. Supporting Reproducible Research**
   - Standardized data formats (BIDS) enable reproducible analyses
   - Processing history is tracked and documented
   - Easy access to both raw and processed data

How Do We Use XNAT at NYUAD?
-----------------------------

Our typical workflow follows these steps:

**1. Data Collection**
   - MRI scanners send DICOM files directly to XNAT
   - Data is automatically organized by project, subject, and session
   - Files are stored securely in the XNAT archive

**2. Data Conversion**
   - Convert DICOM files to NIfTI format using the ``dcm2niix`` pipeline
   - Organize data into BIDS format using the ``dcm2bids`` pipeline
   - BIDS format enables use of standard analysis pipelines

**3. Quality Control**
   - Run ``mriqc`` to assess data quality automatically
   - Review quality reports to identify problematic scans
   - Validate BIDS datasets using project-specific validators

**4. Preprocessing**
   - Run preprocessing pipelines like ``fMRIPrep`` for functional MRI data
   - Process diffusion data with ``tractoflow``
   - All processing happens on our HPC cluster automatically

**5. Data Access**
   - Download processed data through the web interface
   - Use the Desktop Client for bulk downloads
   - Access data programmatically using Python or MATLAB scripts

**6. Analysis**
   - Download analysis-ready data to your local machine or analysis server
   - Use standard neuroimaging tools (FSL, FreeSurfer, etc.) with the processed data
   - Results can be uploaded back to XNAT for sharing

Key Features of NYUAD XNAT
---------------------------

**Access and Security**
- Google OAuth authentication for secure login
- Project-based access control
- API tokens for programmatic access

**Available Pipelines**
- **Data Conversion**: dcm2niix, dcm2bids, dcm2hcp
- **Quality Control**: mriqc, ari-validator
- **Preprocessing**: fMRIPrep, tractoflow, HCP Pipeline

**Data Formats Supported**
- DICOM (raw scanner data)
- NIfTI (standard analysis format)
- BIDS (Brain Imaging Data Structure)
- HCP (Human Connectome Project format)

**Download Methods**
- Web browser interface
- XNAT Desktop Client
- Python scripts
- MATLAB scripts

Getting Started
---------------

**New to XNAT?**

1. **Set up your account**: See :doc:`../working_with_xnat/access` for registration and login instructions
2. **Learn about data formats**: Read :doc:`../understanding_data/overview` to understand MRI data organization
3. **Explore available tools**: Check :doc:`../processing_pipelines/overview` to see what pipelines are available
4. **Upload your first data**: Follow :doc:`../working_with_xnat/uploading` to upload data to XNAT

**Already have an account?**

- Browse your projects and data through the web interface
- Run pipelines on your data (see :doc:`../working_with_xnat/running_pipelines`)
- Download processed results using any of our :doc:`../data_download/browser` methods

Access Information
------------------

- **XNAT URL**: https://xnat.abudhabi.nyu.edu
- **Support Email**: admin.nyuad.xnat@nyu.edu
- **Documentation**: This user guide

For more information about XNAT in general, visit the `official XNAT documentation <https://wiki.xnat.org/documentation/>`_.

Next Steps
----------

- :doc:`../working_with_xnat/access` - Set up your account and get project access
- :doc:`overview` - Learn about the documentation structure
- :doc:`../understanding_data/overview` - Understand MRI data formats
- :doc:`../processing_pipelines/overview` - Explore available processing pipelines

