TractoFlow
==========

This page provides information on running the TractoFlow pipeline via XNAT.
**TractoFlow** is a robust diffusion MRI processing pipeline developed by the SCIL (Sherbrooke Connectivity Imaging Lab). It performs a fully automated dMRI processing from raw data to tractography.

What is TractoFlow?
-------------------

TractoFlow processes diffusion MRI data to correct for artifacts and reconstruct white matter pathways. Its main steps include:

- **Denoising**: MP-PCA denoising on DWI data.
- **Preprocessing**: Eddy current correction, Topup (if reverse phase encoding is available), and motion correction.
- **T1w Image Processing**: Brain extraction and registration to DWI space.
- **DTI Metrics**: Computation of Fractional Anisotropy (FA), Mean Diffusivity (MD), Axial Diffusivity (AD), and Radial Diffusivity (RD).
- **fODF computation**: Fiber Orientation Distribution Function using Constrained Spherical Deconvolution (CSD).
- **Tractography**: Probabilistic or deterministic tracking (Particle Filtering Tracking).

For detailed information, visit the `official Tractoflow documentation <https://tractoflow-documentation.readthedocs.io/en/latest/>`_.

What You Need Before Running
----------------------------

1. **BIDS Conversion**: You must run :doc:`dcm2bids` first. The pipeline expects data in the ``Resources/rawdata`` folder.
   
   - **Required**: A valid T1w anatomical image.
   - **Required**: A valid DWI acquisition (dwi.nii.gz, .bval, .bvec).
   - **Optional but Recommended**: A reverse phase encoding b0 image (fmap) for distortion correction.

2. **FreeSurfer**: While TractoFlow can perform its own brain extraction, running FreeSurfer beforehand and having the outputs available in ``Resources/freesurfer`` is highly recommended. The XNAT pipeline script explicitly checks for existing FreeSurfer outputs to improve T1w processing and registration.

How to Launch the Pipeline
--------------------------

.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`. For running pipelines across multiple subjects in parallel, see :doc:`../working_with_xnat/parallel_processing`.

1. Navigate to your **session** on XNAT.
2. Click **"Run Preprocessing Pipeline"**.
3. Select **"TractoFlow"** from the pipeline dropdown.
4. Configure the parameters:

   - **Session Label**: Typically auto-filled.
   - **Project ID**: Typically auto-filled.
   - **FMRIPrep Flags**: (Optional) Although labeled generic flags, this field is intended for passing specific Tractoflow Nextflow arguments if supported by the wrapper. *Note: In standard configuration, the pipeline runs with optimal defaults.*

.. warning::
   The pipeline requires significant computational resources. Please allow 12-24 hours for completion.

Output Structure
----------------

TractoFlow generates a comprehensive set of derivatives. The XNAT pipeline transfers these back to a **tractoflow** folder in the session Resources.

.. parsed-literal::

    **<Resources>/**
      **tractoflow/**
        **DTI_Metrics/**
            sub-01_ses-01__fa.nii.gz       (Fractional Anisotropy)
            sub-01_ses-01__md.nii.gz       (Mean Diffusivity)
            sub-01_ses-01__ad.nii.gz
            sub-01_ses-01__rd.nii.gz
        **FODF_Metrics/**
            ... (fODF data for tracking)
        **Tractography/**
            sub-01_ses-01__pft_tracking_prob_sc_t1_seeding_mask.trk
        **Readme.md**
        **report.html** (Quality Control Report)

**Key Output Files:**

- ``DTI_Metrics/*_fa.nii.gz``: Use this for voxel-based analysis of white matter integrity.
- ``Tractography/*.trk``: The whole-brain tractogram. This can be visualized in software like `MI-Brain <https://github.com/imeka/mi-brain>`_, Dipy, or MRtrix.
- ``report.html``: A visual report of the processing steps. Check this to verify brain extraction and registration quality.

Version and Runtime Notes
-------------------------

TractoFlow runs through NYUAD-managed compute infrastructure after you submit it from XNAT. You do not need to run Nextflow manually. If your analysis requires a specific TractoFlow or container version, contact support before launching a large batch.

For users who need to understand the runtime environment, see the CRC documentation for `Jubail system details <https://crc-docs.abudhabi.nyu.edu/hpc/system/index.html>`_, `job submission and SLURM <https://crc-docs.abudhabi.nyu.edu/hpc/jobs/quick_start.html>`_, and `Singularity on HPC <https://crc-docs.abudhabi.nyu.edu/hpc/software/singularity_commands.html>`_.

Troubleshooting
---------------

- **Missing T1w or DWI**: The pipeline will fail immediately if these are not found in the BIDS structure.
- **Registration Failures**: If the tracking results look wrong (e.g., streamlines exiting the brain), check the `report.html` for registration errors between T1w and DWI.
- **Job Errors**: If the job fails, download the available logs from the ``tractoflow/logs`` directory and contact support with the project, subject, session, and pipeline name.

References
----------

- `TractoFlow Documentation <https://tractoflow-documentation.readthedocs.io/en/latest/>`_
- `Nextflow <https://www.nextflow.io/>`_
