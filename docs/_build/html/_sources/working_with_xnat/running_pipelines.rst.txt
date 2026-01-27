Running Pipelines on XNAT
=========================

This page provides general instructions for running any processing pipeline on XNAT. Individual pipeline pages reference this guide for the basic workflow.

General Pipeline Interface
--------------------------

All pipelines on XNAT follow the same basic interface through the web UI:

1. **Navigate to your project**
2. **Select the subject and session**
3. **Access the pipeline launcher**
4. **Configure pipeline parameters**
5. **Submit the job**
6. **Monitor progress and results**

Step-by-Step Instructions
-------------------------

**1. Navigate to Your Data**

- Log into XNAT (https://xnat.abudhabi.nyu.edu)
- Select your project from the project list
- Navigate to the subject and session you want to process

**2. Launch Pipeline Interface**

[PLACEHOLDER - Screenshot of pipeline button location]

- On the session page, look for the "Run Pipeline" or "Actions" button
- Click to open the pipeline selection interface

**3. Select Pipeline**

[PLACEHOLDER - Screenshot of pipeline selection dropdown]

- Choose the desired pipeline from the dropdown menu
- Available pipelines depend on your project configuration

**4. Configure Parameters**

[PLACEHOLDER - Screenshot of parameter configuration interface]

- **Input Selection:** Choose which scans to process
- **Output Destination:** Specify where results should be stored
- **Pipeline Parameters:** Set pipeline-specific options
- **Resource Allocation:** Configure computing resources (if applicable)

**5. Submit Job**

[PLACEHOLDER - Screenshot of job submission button]

- Review your configuration
- Click "Submit" or "Run" to start the pipeline
- Note the job ID for tracking

**6. Monitor Progress**

[PLACEHOLDER - Screenshot of job monitoring interface]

- Check job status in the "Processing" or "Jobs" section
- Monitor logs for progress and any errors
- Receive notifications when job completes

Common Parameters
-----------------

**Input Selection:**
- **Scan Selection:** Choose specific scans to process
- **Session Level:** Process entire session
- **Quality Control:** Include/exclude based on QC status

**Output Configuration:**
- **Output Location:** Where to store results
- **Naming Convention:** How to name output files
- **Sharing Settings:** Who can access results

**Processing Options:**
- **Resource Allocation:** CPU, memory, time limits
- **Notification Settings:** Email alerts for completion
- **Debug Mode:** Enable detailed logging

Troubleshooting
---------------

**Common Issues:**
- **Permission Errors:** Check project access rights
- **Input Validation:** Ensure required scans are present
- **Resource Limits:** Job may need more time or memory
- **Network Issues:** Check XNAT connectivity

**Getting Help:**
- Check pipeline logs for specific error messages
- Review pipeline documentation for parameter requirements
- Contact support if issues persist

**Data Loss Concerns:**
- If you accidentally delete pipeline outputs or data, see :doc:`../support/data_loss_recovery` for recovery options
- Contact XNAT administrators immediately if critical data is lost

Next Steps
----------

After completing this general overview:

- Explore specific pipeline documentation:
  - :doc:`../processing_pipelines/dcm2bids` for DICOM conversion
  - :doc:`../processing_pipelines/fmriprep` for fMRI preprocessing
  - :doc:`../processing_pipelines/tractoflow` for tractography
- Learn about :doc:`../data_download/browser` for accessing results
- See :doc:`../support/troubleshooting` for common issues