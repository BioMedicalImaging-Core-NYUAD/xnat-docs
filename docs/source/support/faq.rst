Frequently Asked Questions
==========================

This section contains answers to commonly asked questions about using XNAT.

General Questions
-----------------

What is XNAT?
~~~~~~~~~~~~~

XNAT is an open source imaging informatics platform designed to facilitate common management, productivity, and quality assurance tasks for imaging-based research projects.

**Key Features:**
- Neuroimaging data management platform
- Multi-site research support  
- Data organization and sharing capabilities
- Pipeline integration for automated processing
- Web-based interface for easy access

For comprehensive information about XNAT, visit the `official XNAT documentation <https://wiki.xnat.org/documentation/>`_.

How do I get access to XNAT?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access to our XNAT instance (xnat.abudhabi.nyu.edu) is managed through:

1. **NYU AD Institutional Access** - Contact your research supervisor or IT support
2. **Project Membership** - Request access to specific research projects
3. **Account Setup** - See :doc:`../working_with_xnat/access` for detailed instructions

For general information about XNAT user management, see the `official XNAT user documentation <https://wiki.xnat.org/documentation/how-to-use-xnat>`_.

What browsers are supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT supports modern web browsers including:

- **Chrome** (recommended)
- **Firefox** 
- **Safari**
- **Edge**

For optimal performance, use the latest version of your browser with JavaScript enabled.

Account and Access
------------------

I forgot my password. How do I reset it?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Password reset procedures depend on your institution's authentication system:

**For NYU AD Users:**
- Use NYU AD's NetID password reset system
- Contact NYU AD IT support if needed
- XNAT will automatically sync with updated credentials

**Self-Service Options:**
- Look for "Forgot Password" link on the login page
- Check your email for reset instructions
- Contact your XNAT administrator if self-service isn't available

**Security Best Practices:**
- Use strong, unique passwords
- Enable two-factor authentication if available
- Never share login credentials

How do I change my account information?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can update your account information through the XNAT web interface:

**To Update Your Profile:**
1. Log into XNAT and click your name in the top-right corner
2. Select "Edit Details" from the dropdown menu
3. Update your contact information, affiliations, and preferences
4. Click "Save" to apply changes

**Editable Information:**
- Contact details (email, phone)
- Institutional affiliation
- Notification preferences
- Display preferences

**Note:** Some information (like username) cannot be changed after account creation. Contact your XNAT administrator for assistance with protected fields.

Why can't I access certain projects?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project access in XNAT is controlled through a permission-based system:

**Permission Levels:**
- **Project Owner:** Full control over project data and settings
- **Project Member:** Can view and download data, run approved pipelines
- **Project Collaborator:** Enhanced access for data contribution and analysis
- **Read-Only:** View-only access to specific datasets

**Common Access Issues:**
- You haven't been added to the project member list
- Your permission level doesn't include the action you're trying to perform
- The project has restricted access settings
- Your account needs approval from the project administrator

**Requesting Access:**
1. Contact the project owner or administrator directly
2. Provide justification for your access needs
3. Specify what level of access you require
4. Include your XNAT username in the request

For more information on XNAT user roles, see the `official XNAT user documentation <https://wiki.xnat.org/documentation/how-to-use-xnat>`_.

Data Upload and Download
------------------------

What file formats are supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT supports a wide range of neuroimaging and research data formats:

**Primary Imaging Formats:**
- **DICOM** (.dcm) - Digital Imaging and Communications in Medicine standard
- **NIfTI** (.nii, .nii.gz) - Neuroimaging Informatics Technology Initiative format
- **ANALYZE** (.hdr/.img) - Legacy neuroimaging format
- **MINC** (.mnc) - Medical Image NetCDF format

**Specialized Formats:**
- **BIDS** - Brain Imaging Data Structure compliant datasets
- **HCP** - Human Connectome Project formats
- **FreeSurfer** - Surface and volume formats (.mgz, .surf)
- **GIFTI** (.gii) - Geometry format for cortical surfaces
- **CIFTI** (.nii) - Connectivity format for dense time series

**Archive Formats:**
- **ZIP** archives for bulk uploads
- **TAR** archives (compressed and uncompressed)

**Metadata and Documentation:**
- **JSON** files for BIDS metadata
- **TSV/CSV** files for tabular data
- **TXT** files for documentation
- **PDF** files for protocols and reports

**Note:** XNAT can store any file type as a resource, but automated processing pipelines may require specific formats.

How do I upload large datasets?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For large datasets, use these strategies to ensure successful uploads:

**Recommended Upload Methods:**

1. **XNAT Desktop Client** - Best for datasets > 1GB

   - Supports resume functionality
   - Better progress monitoring
   - See :doc:`../working_with_xnat/install_desktop_client`

2. **ZIP Archives** - For many small files
   - Compress related files together
   - Upload single archive instead of individual files
   - XNAT can automatically extract archives

3. **Programmatic Upload** - For automation
   - Use Python scripts with the XNAT API
   - See :doc:`../data_download/python_scripts`

**Best Practices:**
- **Stable Network:** Use wired connection when possible
- **Split Large Files:** Break multi-GB uploads into smaller chunks
- **Upload During Off-Peak:** Better performance during low-usage times
- **Verify Uploads:** Check file integrity after completion
- **Monitor Progress:** Keep track of upload status

**Troubleshooting Large Uploads:**
- **Browser Timeouts:** Switch to desktop client or scripts
- **Network Interruptions:** Use tools that support resume functionality
- **File Size Limits:** Contact administrators if you hit upload limits

Why is my download failing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download failures can occur for several reasons. Here are common issues and solutions:

**Common Causes:**
- **Network Timeouts:** Large files may exceed browser timeout limits
- **Insufficient Storage:** Check available disk space on your device
- **Permission Issues:** Verify you have download access to the data
- **Browser Limitations:** Some browsers have download size restrictions
- **Server Load:** High server usage can cause slow or failed downloads

**Solutions by Download Method:**

1. **Browser Downloads:**

   - Try smaller file selections
   - Use "Save As" instead of direct opening
   - Clear browser cache and cookies
   - Disable browser extensions that might interfere

2. **Desktop Client:**
   - Restart the download client
   - Check network connectivity
   - Verify authentication credentials
   - See :doc:`../data_download/desktop_client`

3. **Programmatic Downloads:**
   - Implement retry logic in scripts
   - Use chunked downloads for large files
   - Verify API authentication tokens
   - See :doc:`../data_download/python_scripts`

**When to Contact Support:**
- Repeated failures with different methods
- Error messages you don't understand
- Suspected server-side issues
- Authentication problems

Data Organization
-----------------

How should I organize my data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proper data organization is crucial for efficient XNAT usage and pipeline processing:

**XNAT Hierarchy:**
- **Project** → **Subject** → **Session** → **Scan** → **Resource**
- Each level can store metadata and files
- Follow consistent naming conventions throughout

**Naming Best Practices:**
- **Subjects:** Use consistent IDs (e.g., ``sub-001``, ``sub-002``)
- **Sessions:** Include timepoint info (e.g., ``ses-baseline``, ``ses-followup``)
- **Scans:** Descriptive names (e.g., ``T1w_MPRAGE``, ``task-rest_bold``)
- **Avoid:** Special characters, spaces, and overly long names

**BIDS Organization (Recommended):**
- Use Brain Imaging Data Structure standards when possible
- Enables automatic pipeline processing
- Improves data sharing and collaboration
- See :doc:`../understanding_data/bids` for details

**Metadata Requirements:**
- **Essential:** Subject demographics, scan parameters, study protocol
- **Helpful:** Scanner details, acquisition date, quality notes
- **Custom:** Project-specific fields as needed

**Resource Organization:**
- **rawdata:** Original DICOM or source files
- **derivatives:** Processed outputs from pipelines
- **documentation:** Protocols, notes, and supporting files

What metadata should I include?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete metadata ensures data usability and compliance with research standards:

**Required Fields:**
- **Subject Information:** Demographics, group assignments, study ID
- **Session Details:** Scan date, session type, timepoint
- **Scan Parameters:** Acquisition protocol, scanner model, sequence details
- **Quality Metrics:** Usability ratings, motion assessments, artifacts

**Recommended Fields:**
- **Clinical Information:** Diagnosis, medication status, symptom scores
- **Technical Details:** Software versions, reconstruction parameters
- **Study Context:** Protocol deviations, operator notes, environmental factors
- **Data Processing:** Preprocessing steps, quality control results

**BIDS-Compatible Metadata:**
- **participants.tsv:** Subject-level information
- **sessions.tsv:** Session-level details (for longitudinal studies)
- **JSON sidecars:** Scan-specific parameters and acquisition details
- **README files:** Study description and data collection procedures

**Custom Metadata:**
- Project-specific assessments and measurements
- Laboratory results and biomarker data
- Behavioral and cognitive test scores
- Custom forms can be created for specialized data collection

**Best Practices:**
- Use standardized terminology when possible
- Include units for all numerical measurements
- Document any coding schemes or scales used
- Regularly backup metadata along with imaging data

How do I manage data versions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT provides several mechanisms for managing data versions and tracking changes:

**Automatic Versioning:**
- XNAT automatically tracks when files are uploaded or modified
- Each resource upload creates a new snapshot
- Previous versions remain accessible unless explicitly deleted
- Modification timestamps and user information are logged

**Version Control Best Practices:**
- **Clear Naming:** Use version numbers in resource names (e.g., ``rawdata_v1``, ``rawdata_v2``)
- **Documentation:** Include change logs explaining what was modified
- **Resource Separation:** Store different processing versions in separate resources
- **Backup Strategy:** Maintain copies of critical datasets before major changes

**Managing Processed Data Versions:**
- **Pipeline Outputs:** Each pipeline run creates new timestamped results
- **Derivative Tracking:** Link processed data back to source versions
- **Quality Control:** Mark data quality and usability status
- **Snapshot Creation:** Create project-wide snapshots before major updates

**Change Tracking:**
- Review modification history in XNAT interface
- Monitor automated processing pipeline versions
- Document manual corrections and quality assessments
- Track protocol changes that affect data collection

**Archive Management:**
- Regularly clean up obsolete or test data
- Establish retention policies for different data types
- Use project-level archiving for completed studies
- Coordinate with system administrators for long-term storage

Processing and Analysis
-----------------------

How do I run processing pipelines?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running processing pipelines in XNAT follows a standardized workflow:

**Basic Steps:**
1. **Navigate to your data** - Go to Project → Subject → Session
2. **Access pipeline interface** - Click "Run Pipeline" or "Actions" button
3. **Select pipeline** - Choose from available processing tools
4. **Configure parameters** - Set input data and processing options
5. **Submit job** - Review settings and launch the pipeline
6. **Monitor progress** - Track job status and review results

**Before Running Pipelines:**
- Ensure your data is properly organized (preferably in BIDS format)
- Verify you have the necessary permissions for the project
- Check that required input scans are present and properly labeled
- Review pipeline documentation for specific requirements

**Parameter Configuration:**
- **Input Selection:** Choose which scans/sessions to process
- **Output Settings:** Specify where results should be stored
- **Processing Options:** Configure pipeline-specific parameters
- **Resource Allocation:** Set computational requirements if available

**Monitoring and Results:**
- Check job status in the "Processing" or "Jobs" section
- Review processing logs for errors or warnings
- Access results through the session's "Resources" section
- Download or share processed data as needed

For detailed instructions, see :doc:`../working_with_xnat/running_pipelines`.

What processing pipelines are available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our XNAT instance offers several categories of processing pipelines:

**Data Conversion Pipelines:**
- **dcm2niix** - DICOM to NIfTI conversion with metadata preservation
- **dcm2bids** - DICOM to BIDS format conversion with validation
- **dcm2hcp** - DICOM to HCP format conversion (in development)

**Quality Control Pipelines:**
- **mriqc** - Comprehensive quality metrics for structural and functional MRI
- **ari-validator** - Project-specific BIDS validation (ARI project)

**Preprocessing Pipelines:**
- **fmriprep** - Robust fMRI preprocessing with FreeSurfer integration
- **tractoflow** - Diffusion MRI preprocessing and tractography
- **HCP Pipeline** - Human Connectome Project processing (in development)

**Pipeline Availability:**
- Pipeline access varies by project configuration
- Some pipelines require special approval or resource allocation
- Custom pipelines can be developed for specific research needs
- Contact your project administrator to enable additional pipelines

**Choosing the Right Pipeline:**
- **For raw DICOM data:** Start with dcm2bids or dcm2niix
- **For quality assessment:** Use mriqc after conversion
- **For fMRI analysis:** Run fmriprep on BIDS-formatted data
- **For diffusion analysis:** Use tractoflow for DTI/DWI data

For detailed information about each pipeline, see :doc:`../processing_pipelines/overview`.

How do I access processing results?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pipeline results are automatically stored in your XNAT session and can be accessed through multiple methods:

**Accessing Results in XNAT:**
1. **Navigate to your session** where the pipeline was run
2. **Check the "Resources" section** for new output directories
3. **Look for pipeline-specific folders** (e.g., ``fmriprep``, ``mriqc``, ``dcm2bids``)
4. **Review processing logs** for job completion status and any warnings

**Common Output Locations:**
- **fmriprep results:** ``Resources/fmriprep`` and ``Resources/freesurfer``
- **mriqc reports:** ``Resources/mriqc`` with HTML quality reports
- **dcm2bids output:** ``Resources/rawdata`` in BIDS format
- **Processing logs:** ``Resources/logs`` or within pipeline-specific directories

**Understanding Output Formats:**
- **NIfTI files** (.nii.gz) - Processed imaging data
- **HTML reports** - Quality control and processing summaries
- **TSV/CSV files** - Tabular data and confound regressors
- **JSON files** - Metadata and processing parameters
- **Log files** - Detailed processing information and error messages

**Quality Assessment:**
- **Review HTML reports** first for overall processing quality
- **Check for warnings** or errors in processing logs
- **Verify expected output files** are present and complete
- **Compare results** across subjects for consistency

**Downloading Results:**
- Use any of the download methods described in :doc:`../data_download/browser`
- For large datasets, consider the :doc:`../data_download/desktop_client`
- Automated downloads via :doc:`../data_download/python_scripts`

Technical Issues
----------------

Why is XNAT running slowly?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT performance can be affected by several factors. Here's how to troubleshoot slow performance:

**Network-Related Issues:**
- **Check your connection:** Test internet speed and stability
- **Use wired connection:** Ethernet is generally faster than WiFi
- **Try different times:** Performance may be better during off-peak hours
- **Clear browser cache:** Old cached data can slow down loading

**Browser Optimization:**
- **Use recommended browsers:** Chrome or Firefox typically perform best
- **Update your browser:** Ensure you're using the latest version
- **Disable extensions:** Some browser plugins can interfere with XNAT
- **Increase memory:** Close unnecessary tabs and applications
- **Enable JavaScript:** XNAT requires JavaScript for full functionality

**Server-Side Factors:**
- **Check server status:** Ask administrators about planned maintenance
- **Monitor system load:** High user activity can slow response times
- **Large data operations:** File uploads/downloads naturally take longer
- **Database maintenance:** Periodic maintenance may affect performance

**Data-Specific Issues:**
- **Large datasets:** Projects with many files load more slowly
- **Complex queries:** Searches across large amounts of data take time
- **Image viewing:** High-resolution images require more processing time

**When to Contact Support:**
- Performance issues persist across different devices/networks
- Specific error messages appear
- Only certain functions are slow while others work normally
- Performance degradation is sudden and significant

I'm getting error messages. What should I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Error messages provide important clues for troubleshooting. Here's how to handle them systematically:

**Initial Steps:**
1. **Take a screenshot** of the full error message
2. **Note what you were doing** when the error occurred
3. **Try the action again** - some errors are temporary
4. **Check your permissions** for the specific project/data
5. **Clear browser cache** and try again

**Common Error Types:**
- **Permission Denied:** Check your project access level and contact the project owner
- **File Not Found:** Verify the data exists and hasn't been moved or deleted
- **Upload Failed:** Check file size limits, network connection, and file format
- **Session Timeout:** Log out and log back in to refresh your session
- **Server Error (500):** Usually temporary; wait a few minutes and retry

**Browser-Related Errors:**
- **JavaScript Errors:** Enable JavaScript and disable problematic extensions
- **Connection Errors:** Check internet connectivity and firewall settings
- **Display Issues:** Try a different browser or clear cache/cookies

**Data Processing Errors:**
- **Pipeline Failures:** Check processing logs for detailed error information
- **Format Errors:** Verify input data meets pipeline requirements
- **Resource Limits:** Contact administrators if jobs fail due to memory/time limits

**Documentation for Error Resolution:**
- Check :doc:`troubleshooting` for detailed error solutions
- Review pipeline-specific documentation for processing errors
- Consult the `official XNAT troubleshooting guide <https://wiki.xnat.org/documentation/getting-started-with-xnat/troubleshooting-xnat-login-and-session-issues>`_

**When to Contact Support:**
- Error persists after basic troubleshooting
- Error message is unclear or not documented
- Multiple users report the same issue
- Critical data or functionality is affected

How do I report bugs or issues?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Effective bug reporting helps administrators resolve issues quickly:

**Before Reporting:**
1. **Reproduce the issue** to confirm it's consistent
2. **Check existing documentation** to ensure it's not a known issue
3. **Try basic troubleshooting** (clear cache, different browser, etc.)
4. **Gather relevant information** (see details below)

**Information to Include:**
- **User account and project** you were working in
- **Exact steps to reproduce** the issue
- **Error messages** (screenshots are helpful)
- **Browser and version** you're using
- **Time and date** when the issue occurred
- **Expected vs. actual behavior**

**How to Report:**
- **Contact Information:** See :doc:`contact` for current support channels
- **Use descriptive subject lines** (e.g., "Upload fails for files >2GB in Chrome")
- **Include screenshots** of error messages when possible
- **Be specific** about the impact on your work

**Priority Levels:**
- **Critical:** System down, data loss, security issues
- **High:** Major functionality broken, affecting multiple users
- **Medium:** Feature not working as expected, workaround available
- **Low:** Minor issues, cosmetic problems, enhancement requests

**Follow-Up:**
- **Respond promptly** to requests for additional information
- **Test proposed solutions** and report results
- **Confirm resolution** once the issue is fixed
- **Provide feedback** on the support process

Data Security and Privacy
-------------------------

How is my data protected?
~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT employs multiple layers of security to protect your research data:

**Data Encryption:**
- **In Transit:** All data transfers use HTTPS/TLS encryption
- **At Rest:** Server storage uses industry-standard encryption
- **Authentication:** Secure login with institutional credentials

**Access Controls:**
- **Role-Based Permissions:** Users only access authorized projects and data
- **Project-Level Security:** Each project has independent access controls
- **Audit Logging:** All data access and modifications are logged
- **Session Management:** Automatic logout after inactivity

**Infrastructure Security:**
- **Secure Hosting:** Servers are housed in secure, monitored facilities
- **Regular Updates:** System software and security patches are maintained
- **Backup Systems:** Multiple redundant copies protect against data loss
- **Network Security:** Firewalls and intrusion detection systems

**Compliance and Policies:**
- **Institutional Requirements:** Follows NYU AD data protection policies
- **Research Standards:** Compliant with scientific data management best practices
- **Regular Security Audits:** Periodic reviews ensure continued protection

For specific security questions or concerns, contact your system administrator or see :doc:`contact`.

What are the privacy policies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT data privacy policies are designed to protect research participants and comply with institutional requirements:

**Data Usage Policies:**
- **Research Purpose Only:** Data may only be used for approved research activities
- **IRB Compliance:** All data use must comply with Institutional Review Board approvals
- **Principal Investigator Responsibility:** PIs are responsible for ensuring proper data use
- **No Commercial Use:** Data cannot be used for commercial purposes without explicit approval

**Data Sharing Restrictions:**
- **Project-Specific Access:** Data sharing is limited to authorized project members
- **External Sharing:** Requires specific approval and may need data use agreements
- **De-identification:** Personal identifiers must be removed for broader sharing
- **Publication Guidelines:** Follow institutional guidelines for data presentation

**Compliance Requirements:**
- **HIPAA:** Protected health information handled according to HIPAA requirements
- **FERPA:** Educational records protected under FERPA guidelines
- **International Standards:** Compliance with relevant international data protection laws
- **Institutional Policies:** Adherence to NYU AD data governance policies

**User Responsibilities:**
- Protect login credentials and never share accounts
- Report suspected data breaches immediately
- Follow project-specific data handling protocols
- Ensure data use aligns with consent and IRB approvals

Contact your IRB office or :doc:`contact` for specific policy questions.

How do I delete my data?
~~~~~~~~~~~~~~~~~~~~~~~~

Data deletion in XNAT requires careful consideration of research requirements and institutional policies:

**Before Requesting Deletion:**
- **Check retention requirements:** Many studies have minimum data retention periods
- **Consider collaborators:** Ensure deletion won't impact ongoing research
- **Review backup needs:** Consider if you need copies for future reference
- **Verify permissions:** Only project owners can authorize significant deletions

**Deletion Process:**
1. **Individual Files:** Can be deleted by users with appropriate permissions
2. **Sessions/Subjects:** Requires project owner approval
3. **Entire Projects:** Must coordinate with XNAT administrators
4. **Bulk Deletions:** Contact support for assistance with large-scale removal

**Data Retention Policies:**
- **Active Studies:** Data typically retained until study completion plus required period
- **Completed Studies:** May need to be retained for several years per institutional policy
- **Published Data:** Often requires longer retention to support research reproducibility
- **Grant Requirements:** Some funding agencies specify minimum retention periods

**Permanent Removal:**
- **Standard Deletion:** Files are removed from active storage but may remain in backups
- **Secure Deletion:** Complete removal including backups (available upon request)
- **Verification:** Administrators can provide confirmation of complete removal

**Alternative Options:**
- **Data Archiving:** Move data to long-term storage instead of deletion
- **Access Restriction:** Limit access without deletion
- **Project Deactivation:** Make inactive while preserving data

Contact :doc:`contact` or your project administrator for deletion requests.

Advanced Features
-----------------

How do I use the API?
~~~~~~~~~~~~~~~~~~~~~

XNAT provides a RESTful API for programmatic access to data and functionality:

**Getting Started:**
- **API Documentation:** Available at ``https://xnat.abudhabi.nyu.edu/xapi`` (requires login)
- **Authentication:** Use alias tokens or session-based authentication
- **Base URL:** All API calls use ``https://xnat.abudhabi.nyu.edu/xapi`` as the base

**Authentication Methods:**
1. **Alias Tokens:** Generate in XNAT under your user profile → "Manage Alias Tokens"
2. **Session Authentication:** Use JSESSIONID from web login
3. **Basic Authentication:** Username/password (less secure, not recommended)

**Common API Operations:**
- **GET /projects:** List available projects
- **GET /projects/{project}/subjects:** List subjects in a project
- **GET /projects/{project}/experiments:** List sessions/experiments
- **POST /projects/{project}/subjects:** Create new subjects
- **PUT /projects/{project}/experiments/{ID}/resources/{resource}/files:** Upload files

**Example Python Usage:**

.. code-block:: python

   import requests

   # Using alias token
   headers = {'Authorization': 'alias_token_here'}
   response = requests.get('https://xnat.abudhabi.nyu.edu/xapi/projects', headers=headers)


**Available Libraries:**
- **Python:** xnatpy library provides high-level interface
- **MATLAB:** XNAT MATLAB tools available
- **R:** RxNAT package for R users

For more examples, see :doc:`../data_download/python_scripts`.

Can I integrate XNAT with other tools?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT is designed to integrate with a wide range of research tools and workflows:

**Direct Integrations:**
- **Analysis Software:** FSL, FreeSurfer, AFNI, SPM, ANTs
- **Container Platforms:** Docker, Singularity for pipeline deployment
- **Programming Languages:** Python, MATLAB, R libraries available
- **Data Management:** REDCap, LabArchives, Electronic Lab Notebooks

**API-Based Integrations:**
- **Custom Scripts:** Python, MATLAB, R scripts for automated workflows
- **Web Applications:** Integration with lab-specific web tools
- **Database Systems:** Export data to external databases
- **Cloud Platforms:** Integration with cloud computing resources

**Pipeline Integration:**
- **Existing Pipelines:** fMRIPrep, MRIQC, TraCToflow already integrated
- **Custom Pipelines:** Docker containers can be added as XNAT pipelines
- **Workflow Managers:** Integration with Nextflow, Snakemake, etc.
- **HPC Systems:** Direct integration with SLURM job schedulers

**Data Export/Import:**
- **BIDS Format:** Native support for Brain Imaging Data Structure
- **DICOM Export:** Full DICOM metadata preservation
- **CSV/TSV:** Tabular data export for statistical analysis
- **Archive Formats:** ZIP/TAR for bulk data transfer

**Development Resources:**
- **REST API:** Full programmatic access to XNAT functionality
- **Plugin Framework:** Custom XNAT plugins for specialized needs
- **JavaScript APIs:** Client-side integration capabilities
- **Documentation:** Comprehensive developer guides available

Contact :doc:`contact` to discuss specific integration needs.

How do I set up automated workflows?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XNAT supports several approaches to workflow automation for efficient data processing:

**Built-in Automation:**
- **Pipeline Auto-Run:** Configure pipelines to run automatically on new data
- **Event Triggers:** Set up actions based on data upload or modification
- **Scheduled Processing:** Regular batch processing of accumulated data
- **Quality Gates:** Automatic quality checks before processing

**Scripted Automation:**
- **Python Scripts:** Use xnatpy library for automated data management
- **Cron Jobs:** Schedule regular tasks on the server or your workstation
- **API Integration:** Automated workflows using XNAT REST API
- **Webhook Integration:** Trigger external processes from XNAT events

**Workflow Configuration:**
1. **Define Triggers:** What events should start automated processing
2. **Set Parameters:** Default pipeline settings and resource allocation
3. **Configure Notifications:** Email alerts for completion or errors
4. **Test Automation:** Run trial workflows with test data
5. **Monitor Performance:** Regular checks on automated job success rates

**Example Automation Scenarios:**
- **New Upload Processing:** Automatically run dcm2bids on new DICOM uploads
- **Quality Control:** Run MRIQC whenever new BIDS data is available
- **Preprocessing Pipeline:** Chain dcm2bids → MRIQC → fMRIPrep automatically
- **Data Export:** Regular exports of processed data to analysis servers

**Best Practices:**
- **Start Simple:** Begin with single-step automation before complex workflows
- **Error Handling:** Include robust error detection and recovery
- **Logging:** Maintain detailed logs of automated processes
- **Testing:** Thoroughly test automation with sample data first
- **Documentation:** Document automation setup for team members

Contact :doc:`contact` for assistance setting up complex automated workflows.

Still Need Help?
----------------

If you can't find the answer to your question here, please:

- Check the :doc:`troubleshooting` guide
- Contact support through :doc:`contact`
- Search the documentation for more specific information

See Also
--------

- :doc:`troubleshooting` - For detailed troubleshooting steps
- :doc:`contact` - For contact information and support
- :doc:`../working_with_xnat/navigation` - For navigation basics
- :doc:`../data_download/browser` - For download procedures

Next Steps
----------

After reviewing the FAQ, here are suggested next steps based on your needs:

**New Users:**
- Complete account setup following :doc:`../working_with_xnat/access`
- Read the overview of :doc:`../understanding_data/overview`
- Try uploading a small test dataset
- Explore available :doc:`../processing_pipelines/overview`

**Experienced Users:**
- Set up :doc:`../data_download/python_scripts` for automation
- Configure :doc:`../working_with_xnat/install_desktop_client` for efficient downloads
- Explore advanced API features for custom workflows
- Share feedback to improve documentation

**Troubleshooting:**
- Check :doc:`troubleshooting` for detailed problem-solving guides
- Try suggested solutions from relevant FAQ sections
- Contact :doc:`contact` if issues persist after trying documented solutions
- Report bugs or documentation gaps to help improve the system

**Contributing:**
- Share feedback on documentation clarity and completeness
- Suggest additional FAQ topics based on your experience
- Report any errors or outdated information
- Help colleagues learn XNAT using these resources