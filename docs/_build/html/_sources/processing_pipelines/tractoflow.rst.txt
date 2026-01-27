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

2. **FreeSurfer (Recommended)**: While TractoFlow can perform its own brain extraction, running FreeSurfer beforehand and having the outputs available in ``Resources/freesurfer`` is highly recommended. The XNAT pipeline script explicitly checks for existing FreeSurfer outputs to improve T1w processing and registration.

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
- ``Tractography/*.trk``: The whole-brain tractogram. This can be visualized in software like `MI-Brain <https://imeka.ca/mi-brain/>`_, `Dipy`, or `Mrtrix`.
- ``report.html``: A visual report of the processing steps. Check this to verify brain extraction and registration quality.

Component Versions
------------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Component
     - Version
     - Filename / Command
   * - Java
     - 1.8.0_31
     - ``module load jdk/1.8.0_31``
   * - Nextflow
     - 21.10.6
     - ``/scratch/mri/singularityimages/nextflow``
   * - Tractoflow
     - 2.4.4
     - ``/scratch/mri/singularityimages/tractoflow/main.nf``
   * - Container
     - 1.6.0
     - ``scilus_1.6.0.sif``

Pipeline Command
----------------

The pipeline is executed on the cluster using the following command structure:

.. code-block:: bash

   /scratch/mri/singularityimages/nextflow run /scratch/mri/singularityimages/tractoflow/main.nf \
       --input <input_directory> \
       --output_dir <output_directory> \
       -with-singularity /scratch/mri/singularityimages/scilus_1.6.0.sif \
       -profile use_gpu,fully_reproducible \
       -resume

.. note::
   The pipeline is configured to use the GPU profile and ensures full reproducibility.

Troubleshooting
---------------

- **Missing T1w or DWI**: The pipeline will fail immediately if these are not found in the BIDS structure.
- **Registration Failures**: If the tracking results look wrong (e.g., streamlines exiting the brain), check the `report.html` for registration errors between T1w and DWI.
- **Job Errors**: If the job fails, download the ``slurm-*.out`` and ``slurm-*.err`` logs from the ``tractoflow/logs`` directory (or `temp_files` if the transfer failed) and contact support.

References
----------

- `TractoFlow Documentation <https://tractoflow-documentation.readthedocs.io/en/latest/>`_
- `Nextflow <https://www.nextflow.io/>`_
