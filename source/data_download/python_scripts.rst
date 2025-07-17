Download via Python
=================================

Automated data download using Python scripts from the XNAT-NYUAD template-scripts repository.

Overview
--------

Python scripts provide:
- Automated, programmatic data access
- Batch download capabilities
- Integration with analysis workflows
- Reproducible download procedures

Available Scripts
-----------------

The template-scripts repository (https://github.com/XNAT-NYUAD/template-scripts) provides four main scripts:

**1. List Projects** (`1_list_projects.py`)
- Lists all accessible projects on XNAT
- Useful for discovering available data
- Returns project IDs and descriptions

**2. List Subjects** (`2_list_subjects.py`)
- Lists all subjects in a specific project
- Shows subject IDs and metadata
- Helps plan download strategies

**3. Download Single Scan** (`3_download_single_scan.py`)
- Downloads a specific scan from XNAT
- Precise control over what gets downloaded
- Good for selective data retrieval

**4. Download Session** (`4_download_session.py`)
- Downloads an entire session with all scans
- Comprehensive data retrieval
- Maintains session organization

Setup Instructions
------------------

**1. Environment Setup:**

```bash
# Install Miniconda (if not already installed)
# Visit: https://docs.anaconda.com/miniconda/install/

# Create and activate environment
conda create -n xnat-env python=3.9
conda activate xnat-env

# Install required packages
conda install pip
pip install xnat
```

**2. Authentication Setup:**

1. Create API token in XNAT web interface:
   - Go to `<your name>` → `Manage Alias Tokens`
   - Create new token
   - Copy 'alias' and 'secret'

2. Configure each script with your credentials:
   - Edit `DEFAULT_TOKEN` variable with your alias
   - Edit `DEFAULT_SECRET` variable with your secret

**3. Download Scripts:**

```bash
# Clone the repository
git clone https://github.com/XNAT-NYUAD/template-scripts.git
cd template-scripts
```

Usage Examples
--------------

**List Available Projects:**

```python
python 1_list_projects.py
```

**List Subjects in Project:**

```python
python 2_list_subjects.py
# Follow prompts to specify project ID
```

**Download Single Scan:**

```python
python 3_download_single_scan.py
# Follow prompts to specify:
# - Project ID
# - Subject ID
# - Session ID
# - Scan ID
```

**Download Complete Session:**

```python
python 4_download_session.py
# Follow prompts to specify:
# - Project ID
# - Subject ID
# - Session ID
```

Customization
-------------

[PLACEHOLDER - How to modify scripts for specific needs]

[PLACEHOLDER - Adding custom filtering and selection]

[PLACEHOLDER - Integrating with analysis pipelines]

Best Practices
--------------

**Security:**
- Never commit API tokens to version control
- Use environment variables for sensitive data
- Regularly rotate API tokens

**Performance:**
- Test with small datasets first
- Use parallel downloads for large datasets
- Monitor network usage and server load

**Organization:**
- Plan your download directory structure
- Use consistent naming conventions
- Document your download procedures

Troubleshooting
---------------

**Common Issues:**
- [PLACEHOLDER - Authentication errors]
- [PLACEHOLDER - Network timeout problems]
- [PLACEHOLDER - Permission denied errors]

**Error Resolution:**
- [PLACEHOLDER - How to debug script issues]
- [PLACEHOLDER - Checking API token validity]
- [PLACEHOLDER - Network connectivity testing]

Next Steps
----------

- Learn about :doc:`../understanding_data/overview` to understand downloaded data formats
- See :doc:`../processing_pipelines/overview` for processing downloaded data
- Explore :doc:`matlab_scripts` for MATLAB-based alternatives
- Consider :doc:`desktop_client` for GUI-based downloads