Enabling Pipelines for Your Project
===================================

This page explains how to enable processing pipelines for your XNAT project.

How to Enable Pipelines
-----------------------

If you have **Project Owner** access, you can enable pipelines directly:

1. Navigate to your project in XNAT
2. Click on **Project Settings** in the left sidebar
3. Scroll down to the **Pipelines** section
4. Check the boxes next to the pipelines you want to enable
5. Click **Save**

.. image:: ../_static/5.enable.pipeline.png
   :align: center
   :width: 900px

.. note::
   If you don't see the **Project Settings** option, you may not have Project Owner permissions. In that case, contact your project owner or the XNAT administrators and we will enable the pipelines for you.

Available Pipelines
-------------------

The following pipelines can be enabled for your project:

- **Data Conversion:** dcm2niix, dcm2bids, dcm2hcp
- **Quality Control:** mriqc, ari-validator
- **Preprocessing:** fmriprep, tractoflow, HCP pipeline

For details on each pipeline, see :doc:`../processing_pipelines/overview`.

Custom Pipeline Setup
---------------------

If you need a new pipeline that is not currently available on XNAT, please schedule a meeting with the XNAT administrators to discuss your requirements.

Next Steps
----------

After enabling pipelines for your project:

1. **Review** :doc:`running_pipelines` for usage instructions
2. **Explore** specific pipeline documentation in :doc:`../processing_pipelines/overview`
3. **Test** pipeline functionality with sample data

Related Documentation
---------------------

- :doc:`running_pipelines` - How to run any pipeline
- :doc:`../processing_pipelines/overview` - Available pipelines
- :doc:`../support/troubleshooting` - Common issues and solutions