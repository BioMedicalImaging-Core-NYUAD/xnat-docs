TractoFlow 
==========
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.

The TractoFlow pipeline provides tractography analysis and white matter fiber tracking using preprocessed diffusion MRI data.

Overview
--------

The TractoFlow pipeline provides:
- Comprehensive tractography analysis workflow
- Multiple tractography algorithms and approaches
- White matter bundle segmentation
- Tractography quality control and validation
- Integration with XNAT for seamless data processing
- Support for various diffusion models and reconstruction methods

Features
--------

- **Multiple Tractography Methods:** Support for deterministic and probabilistic tractography
- **Bundle Segmentation:** White matter bundle extraction and analysis
- **Quality Control:** Built-in tractography validation and QC metrics
- **Visualization:** Tractography visualization and reporting tools
- **BIDS Compatibility:** Process BIDS-formatted diffusion data
- **Integration:** Works with QSIPrep preprocessed data

Input Requirements
------------------

**Required:**
- Preprocessed diffusion MRI data (preferably from QSIPrep)
- T1w anatomical images
- Valid XNAT project with appropriate permissions
- Diffusion tensor or advanced diffusion model data

**Optional:**
- White matter atlas for bundle segmentation
- Custom tractography parameters
- [PLACEHOLDER - Specific preprocessing requirements]
- [PLACEHOLDER - Minimum data quality thresholds]

How to Run
----------

For general instructions on running pipelines, see: :doc:`../working_with_xnat/running_pipelines`

**Pipeline-Specific Parameters:**
- **BIDS Input:** Select BIDS-formatted diffusion dataset
- **Participant Selection:** Choose subjects to process
- **Tractography Algorithm:** Select tracking method
- **Output Options:** Choose derivatives to generate
- **Resource Allocation:** Configure HPC resources

[PLACEHOLDER - Tractography algorithm selection]

Tractography Methods
--------------------

[PLACEHOLDER - Deterministic tractography options]

[PLACEHOLDER - Probabilistic tractography methods]

[PLACEHOLDER - Advanced tractography algorithms]

[PLACEHOLDER - Parameter optimization strategies]

Bundle Analysis
---------------

[PLACEHOLDER - White matter bundle segmentation]

[PLACEHOLDER - Bundle-specific metrics]

[PLACEHOLDER - Atlas-based analysis]

[PLACEHOLDER - Custom bundle definition]

Output Structure
----------------

[PLACEHOLDER - TractoFlow output directory structure]

[PLACEHOLDER - Tractography files and formats]

[PLACEHOLDER - Bundle segmentation results]

[PLACEHOLDER - Quality control reports]

[PLACEHOLDER - Visualization outputs]

Quality Control
---------------

[PLACEHOLDER - Tractography quality metrics]

[PLACEHOLDER - Bundle validation methods]

[PLACEHOLDER - Visual inspection tools]

[PLACEHOLDER - Statistical quality assessment]

Troubleshooting
---------------

[PLACEHOLDER - Common issues and solutions]

[PLACEHOLDER - Error messages and their meanings]

[PLACEHOLDER - Memory and computational requirements]

[PLACEHOLDER - Data quality requirements]

[PLACEHOLDER - How to get help]

Next Steps
----------

- Quality check tractography results
- Use bundle metrics for statistical analysis
- Learn about :doc:`../understanding_data/tractography` concepts
- See :doc:`../data_download/overview` for accessing tractography data
- Consider integration with :doc:`qsiprep-jubail` preprocessing