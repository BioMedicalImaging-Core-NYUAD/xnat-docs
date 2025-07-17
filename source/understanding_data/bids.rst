BIDS Format
===========

BIDS (Brain Imaging Data Structure) is **the main data structure we support on XNAT**. It provides a standardized way to organize neuroimaging data that unlocks access to numerous analysis pipelines.

What is BIDS?
-------------

BIDS is a community-driven standard for organizing brain imaging data. When you organize your data in BIDS format via :doc:`../processing_pipelines/dcm2bids` pipeline, it opens your data up to many available pipelines such as :doc:`../processing_pipelines/mriqc`, :doc:`../processing_pipelines/fmriprep`, :doc:`../processing_pipelines/tractoflow`, and many others.

**Key Benefits:**

- **Pipeline Compatibility**: Works with modern analysis tools (fMRIPrep, MRIQC, etc.)
- **Standardized Structure**: Consistent organization across research projects
- **Metadata Integration**: JSON sidecar files preserve acquisition parameters
- **Data Sharing**: Facilitates collaboration and reproducible research

For comprehensive information about BIDS, visit the `BIDS Starter Kit <https://bids-standard.github.io/bids-starter-kit/>`_.

BIDS on XNAT
------------

**How to Get BIDS Data:**

1. Upload your DICOM data to XNAT
2. Run the :doc:`../processing_pipelines/dcm2bids` pipeline 
3. Your data will be converted to BIDS format in the ``rawdata`` directory

**Resulting example structure:**
::

    Resources/
    └── rawdata/
        ├── dataset_description.json
        ├── participants.tsv
        └── sub-<subject>/
            └── ses-<session>/
                ├── anat/
                │   ├── sub-<subject>_ses-<session>_T1w.nii.gz
                │   └── sub-<subject>_ses-<session>_T1w.json
                ├── func/
                │   ├── sub-<subject>_ses-<session>_task-<task>_bold.nii.gz
                │   └── sub-<subject>_ses-<session>_task-<task>_bold.json
                └── fmap/
                    ├── sub-<subject>_ses-<session>_dir-<dir>_epi.nii.gz
                    └── sub-<subject>_ses-<session>_dir-<dir>_epi.json

- **anat**: Structural images (T1w, T2w, FLAIR)
- **func**: Functional images (bold, sbref)
- **fmap**: Fieldmap images for distortion correction
- **dwi**: Diffusion-weighted images

File Naming and Organization
---------------------------

BIDS uses systematic file naming with key-value pairs separated by underscores:

**Basic Pattern:** `sub-<subject>_[ses-<session>_][task-<task>_]<suffix>.nii.gz`

Each NIfTI file has a corresponding JSON file with the same name containing acquisition metadata.

For detailed naming conventions, see the `BIDS specification on files and folders <https://bids.neuroimaging.io/getting_started/folders_and_files/files.html>`_.

BIDS Validation
---------------

- :doc:`../processing_pipelines/dcm2bids` pipeline includes built-in BIDS validation
- Use pipelines such as the :doc:`../processing_pipelines/ari-validator` for project-specific validation (if available for your project)
- External validation: `BIDS Validator <https://bids-standard.github.io/bids-validator/>`_
- Complete specification: `BIDS Specification <https://bids-specification.readthedocs.io/en/stable/>`_

Available BIDS Pipelines
------------------------

Once your data is in BIDS format, you can run these pipelines:


- :doc:`../processing_pipelines/mriqc` - Automated quality metrics and reports
- :doc:`../processing_pipelines/fmriprep` - Robust fMRI preprocessing
- :doc:`../processing_pipelines/tractoflow` - Diffusion MRI processing
- Additional format conversions available through BIDS-compatible tools

Next Steps
----------

1. **Convert your data**: See :doc:`../processing_pipelines/dcm2bids` to get started
2. **Run quality control**: Use :doc:`../processing_pipelines/mriqc` to assess data quality
3. **Preprocess your data**: Choose appropriate preprocessing pipelines
4. **Learn more**: Visit the `BIDS Starter Kit <https://bids-standard.github.io/bids-starter-kit/>`_ for comprehensive tutorials

Related Documentation
--------------------

- :doc:`../processing_pipelines/dcm2bids` - Convert DICOM to BIDS
- :doc:`../processing_pipelines/overview` - All available pipelines
