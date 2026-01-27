Download via Python
===================

Automated data download using Python scripts from the XNAT template-scripts repository.

Overview
--------

Python scripts provide automated, programmatic data access with batch download capabilities and integration with analysis workflows.

Available Scripts
-----------------

Four main Python scripts are available for different download tasks:

**1. List Projects** (``1_list_projects.py``)
   Lists all accessible projects on XNAT with IDs, names, and descriptions.

**2. List Subjects** (``2_list_subjects.py``)
   Shows detailed information for subjects in a project, including sessions, scans, and metadata.

**3. Download Single Scan** (``3_download_single_scan.py``)
   Downloads DICOM files from a specific scan with precise control over selection.

**4. Download Session** (``4_download_session.py``)
   Downloads all scans from a session, with optional filtering by scan type.

Setup Instructions
------------------

**1. Environment Setup**

.. code-block:: bash

   # Create conda environment
   conda create -n xnat-env python=3.9
   conda activate xnat-env
   pip install xnat

**2. Get Template Scripts**

.. code-block:: bash

   git clone https://github.com/XNAT-NYUAD/template-scripts.git
   cd template-scripts

**3. Configure Authentication**

1. Create API token in XNAT:
   - Go to your profile → "Manage Alias Tokens"
   - Click "Create New Token"
   - Copy the alias and secret values

2. Edit each script file and replace:
   - ``TOKEN_USER = "<paste your token alias here>"``
   - ``TOKEN_SECRET = "<paste your token secret here>"``

Usage Examples
--------------

**List Available Projects**

.. code-block:: bash

   python 1_list_projects.py

**Examine Subject Details**

.. code-block:: bash

   # Show first subject in project
   python 2_list_subjects.py
   
   # Show specific subject
   python 2_list_subjects.py --subject sub-001

**Download Single Scan**

.. code-block:: bash

   # Download first scan (uses default project)
   python 3_download_single_scan.py
   
   # Download specific scan
   python 3_download_single_scan.py --subject sub-001 --session ses-01 --scan 1

**Download Complete Session**

.. code-block:: bash

   # Download all scans
   python 4_download_session.py --subject sub-001 --session ses-01
   
   # Download only T1 and T2 scans
   python 4_download_session.py --subject sub-001 --session ses-01 --scan-types T1 T2

Script Configuration
--------------------

Each script contains these configurable parameters:

- ``XNAT_SERVER``: Server URL (default: https://xnat.abudhabi.nyu.edu)
- ``TOKEN_USER``: Your API token alias
- ``TOKEN_SECRET``: Your API token secret
- ``PROJECT_ID``: Default project (default: rokerslab_ari-clean)

Output Structure
----------------

Downloaded files are organized as:

.. code-block:: text

   downloaded_data/
   ├── scan-1_T1/          # Single scan downloads
   │   ├── file1.dcm
   │   └── file2.dcm
   └── session-ses-01/     # Session downloads
       ├── scan-1_T1/
       ├── scan-2_T2/
       └── scan-3_func/

Security Best Practices
-----------------------

- Never commit API tokens to version control
- Regularly rotate API tokens
- Use project-specific tokens when possible
- Store tokens in environment variables for production use

Troubleshooting
---------------

**Authentication Errors**
   Verify your API token is correct and hasn't expired. Create a new token if needed.

**Project Not Found**
   Check project ID spelling and ensure you have access permissions.

**No Scans Found**
   Verify subject/session IDs exist and contain DICOM data.

**Download Failures**
   Check network connectivity and ensure sufficient disk space.

Next Steps
----------

- Learn about :doc:`../understanding_data/bids` for data organization
- See :doc:`../processing_pipelines/overview` for processing pipelines
- Try :doc:`matlab_scripts` for MATLAB-based downloads