Running Pipelines on XNAT
=========================

This page explains the common workflow for launching processing pipelines from the XNAT web interface. Individual pipeline pages describe the inputs and outputs for each tool.

Before You Start
----------------

Before launching a pipeline, check the following:

- You have access to the project and session you want to process.
- The pipeline is enabled for your project. See :doc:`enabling_pipelines`.
- The required input data is present. For BIDS-based pipelines, run :doc:`../processing_pipelines/dcm2bids` first.
- You understand where the output will appear, usually in the session or project **Resources** area.

Session-Level Pipelines
-----------------------

Most conversion, quality-control, and preprocessing pipelines are launched from an imaging session.

1. Log into XNAT at https://xnat.abudhabi.nyu.edu.
2. Open your project.
3. Open the subject and session you want to process.
4. Use the session actions menu to choose the available pipeline launcher. Depending on the pipeline, this may appear as **Run Pipeline**, **Run Preprocessing Pipeline**, or **Run Containers**.
5. Select the pipeline.
6. Review the parameters. Leave optional fields unchanged unless the pipeline page tells you to change them.
7. Submit the job.
8. Monitor the job status and review logs if the job fails.

Project-Level Pipelines
-----------------------

Some workflows run across multiple sessions or subjects from the project page. Examples include group-level quality-control reports or project-wide batch launches.

1. Open the project page.
2. Use the project actions menu to find the batch or container launcher.
3. Select the pipeline and the subjects or sessions to include.
4. Submit the job and monitor progress from the project or processing view.

For multi-subject launches, see :doc:`parallel_processing`.

Choosing Parameters
-------------------

Pipeline forms vary, but these fields are common:

- **Subject or session label**: Usually auto-filled from the XNAT session. Change only when the pipeline documentation explicitly asks you to.
- **Input resource**: The folder or resource the pipeline reads from, such as ``rawdata`` for BIDS inputs.
- **Output resource**: The folder where results will be stored, such as ``mriqc``, ``fmriprep``, or ``tractoflow``.
- **Optional flags**: Advanced command options. Use these carefully; invalid flags can cause jobs to fail.

Monitoring Results
------------------

After submission:

- Check the job status in XNAT.
- Wait for the pipeline to finish before launching dependent pipelines.
- Open the output resource and review reports or logs.
- For quality-control and preprocessing pipelines, inspect HTML reports before using the derivatives for analysis.

Troubleshooting
---------------

**Pipeline is not listed**
   The pipeline may not be enabled for the project, or you may not have permission to run it. See :doc:`enabling_pipelines`.

**Pipeline fails quickly**
   Check whether the required input resource exists and whether the session labels match the expected format.

**Pipeline runs but output is missing**
   Check the logs in the output resource. If the transfer back to XNAT failed, include the workflow ID and session label when contacting support.

**Pipeline takes longer than expected**
   Some pipelines, especially fMRIPrep and TractoFlow, can take many hours. If a job appears stuck or repeatedly times out, contact support with the project, subject, session, pipeline name, and any available logs.

For more help, see :doc:`../support/troubleshooting`.

Next Steps
----------

- Explore :doc:`../processing_pipelines/overview` for available pipelines.
- Read the page for the specific pipeline you want to run.
- Use :doc:`../data_download/browser` or :doc:`../data_download/desktop_client` to access results.
