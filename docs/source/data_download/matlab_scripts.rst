Download via MATLAB
===================

This guide covers using MATLAB scripts to download data from XNAT programmatically.

Overview
--------

MATLAB scripts provide a powerful way to download data from XNAT within the MATLAB environment. This method is particularly useful for:

- Researchers already working in MATLAB
- Integration with existing MATLAB workflows
- Custom data processing pipelines
- Batch operations within MATLAB

Prerequisites
-------------

- MATLAB installed on your system
- Network access to the XNAT server
- Valid XNAT credentials
- Basic MATLAB programming knowledge

Getting Started
---------------

Example Scripts
~~~~~~~~~~~~~~~

The ``matlab-example`` folder in the template-scripts repository contains several example scripts:

- ``downloadXNAT.m`` - Main download function
- ``run_download.m`` - Example usage script
- ``setup_xnat_env.m`` - Environment setup script
- ``session-download-v1.py`` - Python helper script
- ``session-resources-v1.py`` - Resource listing script

[PLACEHOLDER: Add detailed description of each script's purpose and usage]

Installation and Setup
----------------------

Environment Setup
~~~~~~~~~~~~~~~~~

[PLACEHOLDER: Instructions for setting up the MATLAB environment]

1. Add the matlab-example folder to your MATLAB path
2. Configure server connection settings
3. Set up authentication credentials

Dependencies
~~~~~~~~~~~~

[PLACEHOLDER: List any required MATLAB toolboxes or external dependencies]

Basic Usage
-----------

Simple Download
~~~~~~~~~~~~~~~

[PLACEHOLDER: Basic example of downloading a single session]

.. code-block:: matlab

   % Example usage (to be filled with actual code)
   % setup_xnat_env;
   % [PLACEHOLDER: Add actual function calls]

Batch Downloads
~~~~~~~~~~~~~~~

[PLACEHOLDER: Instructions for downloading multiple sessions]

Advanced Usage
--------------

Custom Filtering
~~~~~~~~~~~~~~~~

[PLACEHOLDER: Information about filtering data before download]

Error Handling
~~~~~~~~~~~~~~

[PLACEHOLDER: Best practices for error handling in MATLAB scripts]

Integration with Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

[PLACEHOLDER: Examples of integrating downloads with processing pipelines]

Configuration Options
---------------------

Server Settings
~~~~~~~~~~~~~~~

[PLACEHOLDER: Information about configuring server connections]

Authentication
~~~~~~~~~~~~~~

[PLACEHOLDER: Security considerations and authentication setup]

Download Parameters
~~~~~~~~~~~~~~~~~~~

[PLACEHOLDER: Available parameters for customizing downloads]

- File format options
- Compression settings
- Metadata inclusion

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

[PLACEHOLDER: Common MATLAB-specific issues and solutions]

- Path configuration problems
- Authentication failures
- Network connectivity issues

Performance Tips
~~~~~~~~~~~~~~~~

[PLACEHOLDER: Tips for optimizing MATLAB download performance]

- Memory management
- Parallel processing options
- Large file handling

See Also
--------

- :doc:`python_scripts` - For Python-based downloads
- :doc:`browser` - For web-based downloads
- :doc:`../support/troubleshooting` - For additional troubleshooting

Next Steps
----------

[PLACEHOLDER: Suggested next steps after setting up MATLAB downloads]

- Integrate with existing MATLAB workflows
- Explore custom processing pipelines
- Set up automated download schedules
- Develop custom analysis scripts