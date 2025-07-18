dcm2bids
=================

The dcm2bids converts your DICOM data to BIDS format on XNAT. This is the **essential first step** that unlocks access to all modern analysis pipelines including :doc:`mriqc`, :doc:`fmriprep`, :doc:`tractoflow`, and others.

For comprehensive information about dcm2bids, visit the `official documentation <https://unfmontreal.github.io/Dcm2Bids/3.1.1/>`_.

What You Need
-------------

- DICOM data uploaded to your XNAT session
- Project permissions to run pipelines


How to Launch the Pipeline
--------------------------

.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.

Navigate to your **session** in XNAT, click **"Run Pipeline"**, select **"dcm2bids"**, and configure these parameters:

- **Subject Number** (Optional): Override automatic subject numbering
- **Session Number** (Optional): Override automatic session numbering  
- **Enable Pydeface** (Default: True): Automatically deface anatomical images

**Automatic Features:**
- SBRef processing and fieldmap associations are handled automatically
- BIDS validation ensures compliant output


What You Get
------------

BIDS-formatted data in your session's **Resources/rawdata/** directory:

.. parsed-literal::

    **Resources/rawdata/**
      dataset_description.json
      participants.tsv
      **sub-<subject>/ses-<session>/**
        **anat/** → T1w, T2w images + JSON metadata
        **func/** → BOLD runs, SBRef images + JSON metadata  
        **fmap/** → Fieldmaps + JSON metadata (with IntendedFor configured)

For BIDS format details, see :doc:`../understanding_data/bids`.


Configuration Files (Advanced)
------------------------------

For non-standard acquisition protocols, create a **config.json** file and upload it to your parent project. The pipeline will automatically detect and use it.

For configuration file creation, see the `dcm2bids configuration guide <https://unfmontreal.github.io/Dcm2Bids/3.1.1/how-to/create-config-file/>`_.


Common Issues
-------------

**Non-Standard Sequence Names:** Create custom configuration file for site-specific protocols

**Missing Data:** Ensure all required sequences (T1w, functional) were acquired

**Privacy Settings:** Disable pydeface if needed using pipeline parameters


Next Steps
----------

1. **Quality Control**: Run :doc:`mriqc` to assess data quality  
2. **Preprocessing**: Use :doc:`fmriprep` for functional data processing
3. **Data Access**: Use :doc:`../data_download/browser` to download converted data

Related Documentation
---------------------

- :doc:`../understanding_data/bids` - Understanding BIDS format
- :doc:`mriqc` - Quality control after conversion
- :doc:`fmriprep` - fMRI preprocessing pipeline