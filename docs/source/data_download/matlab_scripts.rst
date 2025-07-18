Download via MATLAB
===================

MATLAB scripts for downloading data from XNAT, integrating seamlessly with MATLAB analysis workflows.

Overview
--------

MATLAB scripts provide automated data download capabilities within the MATLAB environment, ideal for researchers who work primarily in MATLAB and want to integrate data retrieval with their analysis pipelines.

Available Scripts
-----------------

The ``matlab-example`` folder contains three main MATLAB scripts:

**1. Environment Setup** (``setup_xnat_env.m``)
   Creates and configures a conda environment with required Python packages.

**2. Download Function** (``downloadXNAT.m``)
   Main download function that handles DICOM files and session resources.

**3. Example Usage** (``run_download.m``)
   Demonstrates configuration and usage patterns.

Setup Instructions
------------------

**1. Prerequisites**

- MATLAB installed
- Miniconda or Anaconda installed
- Network access to XNAT server

**2. Get Template Scripts**

.. code-block:: bash

   git clone https://github.com/XNAT-NYUAD/template-scripts.git
   cd template-scripts/matlab-example

**3. Environment Setup**

Run this once to create the Python environment:

.. code-block:: matlab

   setup_xnat_env;

This creates a conda environment named ``xnat_env`` with required Python packages.

**4. Configure Authentication**

Edit ``run_download.m`` and update:

.. code-block:: matlab

   config.api_token_id = 'your_token_alias';
   config.api_token_secret = 'your_token_secret';
   config.project_id = 'your_project_id';

Basic Usage
-----------

**Download DICOM Files**

.. code-block:: matlab

   % Configure XNAT connection
   config = struct();
   config.server_url = 'https://xnat.abudhabi.nyu.edu/';
   config.api_token_id = 'your_alias';
   config.api_token_secret = 'your_secret';
   config.project_id = 'your_project';
   
   % Download specific subject/session
   status = downloadXNAT('config', config, ...
                        'subjects', {'sub-001'}, ...
                        'sessions', {'ses-01'});

**Download Session Resources**

.. code-block:: matlab

   % Download processed data (e.g., 'rawdata' folder)
   status = downloadXNAT('config', config, ...
                        'subjects', {'sub-001'}, ...
                        'sessions', {'ses-01'}, ...
                        'resource', 'rawdata');

**Test Mode**

.. code-block:: matlab

   % Test connection without downloading
   status = downloadXNAT('config', config, ...
                        'test', true);

Function Parameters
-------------------

The ``downloadXNAT`` function accepts these parameters:

- ``config`` (required): Struct with server and authentication settings
- ``subjects``: Cell array of subject IDs to download
- ``sessions``: Cell array of session IDs to download  
- ``resource``: Specific resource name (e.g., 'rawdata', 'BIDS')
- ``test``: Boolean flag for test mode (no actual download)

Output Structure
----------------

Downloads are organized in the script directory:

.. code-block:: text

   matlab-example/
   ├── downloads/           # Downloaded data
   │   ├── session-ses-01/
   │   └── session-ses-02/
   └── logs/               # Download logs
       ├── download.log
       └── download_complete

Error Handling
--------------

The scripts include comprehensive error handling:

- **Conda not found**: Install Miniconda or Anaconda
- **Environment creation failed**: Check conda permissions
- **Python package installation failed**: Verify internet connectivity
- **Download failed**: Check authentication and project access

Configuration Options
---------------------

**Server Configuration**

.. code-block:: matlab

   config.server_url = 'https://xnat.abudhabi.nyu.edu/';
   config.api_token_id = 'your_alias';
   config.api_token_secret = 'your_secret';
   config.project_id = 'your_project';

**Download Options**

- Download entire sessions (DICOM files)
- Download specific resources (processed data)
- Test connections before downloading
- Filter by subject and session IDs

Integration with Workflows
--------------------------

**Example Analysis Pipeline**

.. code-block:: matlab

   % 1. Download data
   status = downloadXNAT('config', config, ...
                        'subjects', {'sub-001'});
   
   % 2. Process downloaded data
   if status == 0
       dataPath = fullfile(pwd, 'downloads', 'session-ses-01');
       % Add your analysis code here
       dicomFiles = dir(fullfile(dataPath, '**', '*.dcm'));
       % Process DICOM files...
   end

Security Best Practices
-----------------------

- Store API tokens securely, never in version control
- Use project-specific tokens when possible
- Regularly rotate API tokens
- Test with limited data first

Troubleshooting
---------------

**Conda Environment Issues**
   Run ``setup_xnat_env`` again or check conda installation.

**Authentication Errors**
   Verify API token alias and secret are correct and haven't expired.

**Download Failures**
   Check project access permissions and network connectivity.

**Python Environment Problems**
   Ensure conda is properly installed and accessible from MATLAB.

Next Steps
----------

- Learn about :doc:`../understanding_data/bids` for data organization
- See :doc:`../processing_pipelines/overview` for analysis pipelines
- Try :doc:`python_scripts` for Python-based alternatives