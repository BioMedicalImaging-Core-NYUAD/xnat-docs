HCP (Under Development)
=======================
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.

The HCP pipeline provides Human Connectome Project-style processing for multi-modal connectome analysis.

Overview
--------

The HCP pipeline will provide:
- HCP-style structural and functional preprocessing
- Surface-based analysis workflows
- Multi-modal integration
- Connectome-ready derivatives

**Development Status:** This pipeline is currently under development and not yet available for use.

Planned Features
----------------

**Processing Capabilities:**
- Structural preprocessing with FreeSurfer integration
- Functional preprocessing with surface registration
- Multi-modal data integration
- Connectome Workbench compatibility

**Input Requirements:**
- HCP-formatted data (or organized structural/functional data)
- High-resolution structural images (T1w, T2w)
- Functional MRI data (task, resting-state)
- Diffusion MRI data (optional)

**Output Structure:**
- HCP-style derivatives
- Surface-based functional data
- Volume and surface registration
- Connectome matrices and metrics

How to Run
----------

For general instructions on running pipelines, see: :doc:`../working_with_xnat/running_pipelines`

**Note:** This pipeline is not yet available. Please check back for updates or contact support for development status.

Alternative Workflows
---------------------

While the HCP pipeline is under development, consider these alternatives:

- Use :doc:`fmriprep` for fMRI preprocessing
- Use :doc:`tractoflow` for tractography analysis
- Convert data to BIDS format using :doc:`dcm2bids`

Next Steps
----------

- Learn about :doc:`../understanding_data/hcp` format
- Explore :doc:`fmriprep` for current fMRI preprocessing
- See :doc:`../understanding_data/relationships` for format comparisons
- Contact support for development timeline updates