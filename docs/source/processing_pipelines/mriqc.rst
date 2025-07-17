MRIQC 
=====
.. note::
   For step-by-step instructions on running any pipeline, see :doc:`../working_with_xnat/running_pipelines`. To enable pipelines for your project, see :doc:`../working_with_xnat/enabling_pipelines`.

The MRIQC pipeline provides comprehensive quality control assessment for structural and functional MRI data.

Overview
--------

The MRIQC pipeline provides:
- Automated quality assessment for T1w, T2w, and BOLD data
- No-reference image quality metrics
- Visual quality control reports
- Group-level quality analysis
- Integration with XNAT workflows

Features
--------

- **Comprehensive QC Metrics:** Automated calculation of image quality metrics
- **Visual Reports:** Interactive HTML reports with quality visualizations
- **Multi-modal Support:** Structural (T1w, T2w) and functional (BOLD) data
- **Group Analysis:** Compare quality metrics across subjects and sessions
- **BIDS Compatibility:** Works with BIDS-formatted datasets
- **Standardized Output:** Consistent quality metrics across studies

Input Requirements
------------------

**Required:**
- BIDS-formatted dataset
- Valid XNAT project with appropriate permissions

**Supported Data Types:**
- Structural MRI (T1w, T2w)
- Functional MRI (BOLD - task and resting-state)
- Multiple sessions and subjects

**Prerequisites:**
- Data should be converted to BIDS format using :doc:`dcm2bids`
- Basic BIDS validation recommended

How to Run
----------

For general instructions on running pipelines, see: :doc:`../working_with_xnat/running_pipelines`

**Pipeline-Specific Parameters:**
- **BIDS Input:** Select BIDS-formatted dataset
- **Participant Selection:** Choose subjects to process
- **Modalities:** Select T1w, T2w, and/or BOLD
- **Output Location:** Specify where to save QC reports
- **Group Analysis:** Enable for multi-subject comparisons

Quality Control Metrics
-----------------------

**Structural Metrics (T1w/T2w):**
- Signal-to-noise ratio (SNR)
- Contrast-to-noise ratio (CNR)
- Coefficient of joint variation (CJV)
- Foreground-to-background energy ratio (FBER)
- Entropy focus criterion (EFC)

**Functional Metrics (BOLD):**
- Temporal signal-to-noise ratio (tSNR)
- Ghost-to-signal ratio (GSR)
- Framewise displacement (FD)
- Standardized DVARS
- Artifact detection and outlier identification

**Additional Assessments:**
- Head motion parameters
- Slice timing and coverage
- Temporal autocorrelation
- Spatial normalization quality

Output Structure
----------------

**Individual Reports:**
- `sub-<subject>_[ses-<session>_]<modality>_report.html` - Visual QC report
- `sub-<subject>_[ses-<session>_]<modality>_metrics.json` - Quantitative metrics
- `sub-<subject>_[ses-<session>_]<modality>_figures/` - Quality control figures

**Group Reports:**
- `group_<modality>_report.html` - Group-level quality summary
- `group_<modality>_metrics.tsv` - All subjects' metrics in tabular format
- `group_<modality>_outliers.json` - Identified outliers and quality issues

**Quality Control Workflow:**
1. Review individual subject reports
2. Examine group-level distributions
3. Identify outliers and quality issues
4. Make decisions about data inclusion/exclusion

Configuration Options
---------------------

**Processing Options:**
- **Modality Selection:** T1w, T2w, BOLD, or combinations
- **Memory Allocation:** Adjust for dataset size
- **Parallel Processing:** Number of subjects to process simultaneously
- **Output Verbosity:** Detailed or summary reports

**Quality Thresholds:**
- **Custom Thresholds:** Set quality metric cutoffs
- **Outlier Detection:** Sensitivity for identifying problematic data
- **Reference Standards:** Compare against normative databases

Troubleshooting
---------------

**Common Issues:**
- **BIDS Validation Errors:** Ensure proper BIDS format
- **Missing Metadata:** Check for required JSON sidecar files
- **Memory Issues:** Reduce parallel processing or increase resources
- **Incomplete Reports:** Verify all required input files are present

**Quality Interpretation:**
- **Review Metrics:** Compare against typical ranges
- **Visual Inspection:** Always complement metrics with visual assessment
- **Group Context:** Consider metrics in context of full dataset
- **Multiple Modalities:** Cross-check quality across different data types

Best Practices
--------------

- **Run early:** Perform quality control before intensive preprocessing
- **Review systematically:** Check both individual and group reports
- **Document decisions:** Keep records of quality-based exclusions
- **Set thresholds:** Establish consistent quality criteria for your study
- **Regular monitoring:** Use for ongoing data collection quality assurance

Next Steps
----------

- Review quality control reports and metrics
- Make data inclusion/exclusion decisions
- Proceed with preprocessing using :doc:`fmriprep` for quality data
- Learn about :doc:`../understanding_data/bids` format requirements
- See :doc:`../data_download/browser` for accessing QC reports