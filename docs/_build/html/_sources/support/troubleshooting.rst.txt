Troubleshooting Guide
=====================

This guide provides systematic approaches to resolving common issues with XNAT.

Login and Access
----------------

**XNAT does not load**
   Confirm that you are on the NYUAD network or connected to the NYUAD VPN. See :doc:`../working_with_xnat/access`.

**Google sign-in works but project is missing**
   Your account may not have access to that project. Request access using the instructions in :doc:`../working_with_xnat/access`.

**A button or action is missing**
   Your project role may not include that permission. Contact the project owner or XNAT administrators.

Upload and Prearchive
---------------------

**Upload appears complete but data is not in the project**
   Check the Prearchive. Uploaded sessions may be waiting for review before they appear in the Archive.

**Session shows Conflict in Prearchive**
   Review the session labels and Study Instance UIDs. For UID-specific conflicts, see :doc:`../working_with_xnat/uid_errors_archiving`.

**Upload is slow or interrupted**
   Use the XNAT Desktop Client for large uploads because it supports pause and resume. See :doc:`../working_with_xnat/uploading`.

Pipeline Jobs
-------------

**Pipeline is not listed**
   The pipeline may not be enabled for the project, or you may not have permission to run it. See :doc:`../working_with_xnat/enabling_pipelines`.

**Pipeline fails immediately**
   Check that the required input resource exists. For MRIQC, fMRIPrep, and TractoFlow, this usually means running dcm2bids first.

**Pipeline finishes but output looks wrong**
   Review the HTML report and logs before using the outputs for analysis. If you contact support, include the project, subject, session, pipeline name, and error logs.

Downloads
---------

**Browser download fails**
   Try the XNAT Desktop Client for large sessions or project-level downloads. See :doc:`../data_download/desktop_client`.

**Desktop Client cannot connect**
   Confirm the server URL, network access, and alias token/secret. See :doc:`../working_with_xnat/install_desktop_client`.

Data Safety
-----------

**Data was deleted or appears missing**
   Contact administrators immediately and include the project, subject, session, approximate time, and what changed. See :doc:`data_loss_recovery`.

Getting Help
------------

If you have tried the troubleshooting steps above and are still experiencing issues, contact the XNAT administrators at admin.nyuad.xnat@nyu.edu.

Before contacting support, please:

1. Try the solutions in this guide
2. Check the :doc:`faq` section
3. Gather error messages and logs
4. Document steps to reproduce the issue

See Also
--------

- :doc:`faq` - For frequently asked questions
- :doc:`contact` - For support contact information
- :doc:`../working_with_xnat/uid_errors_archiving` - Resolving UID errors during archiving
- :doc:`../data_download/browser` - For download procedures
