Data Upload Procedures
======================

This guide covers the various methods and procedures for uploading data to XNAT.

Overview
--------

XNAT provides multiple ways to upload research data, each suited for different use cases and data types.

.. note::
   **Prearchive vs. Archive**:
   In XNAT, data typically lands in a temporary holding area called the **Prearchive** first. Here, you can review, label, and clean up data before committing it to the permanent **Archive**.
   
   *   **Prearchive**: Staging area. Data can be edited or deleted.
   *   **Archive**: Permanent storage. Data is indexed and protected.
   
   For more details, refer to the `Official XNAT Documentation on Data Archiving <https://wiki.xnat.org/display/XNAT18/Archiving+Data>`_.

Important Considerations
------------------------

Before uploading, please be aware of the following safety guidelines:

.. warning::
   **Overwriting and Merging Data**
   
   Uploading data to an existing project or session can overwrite existing files or merge new data into an existing session.
   
   *   **Overwrite**: If you upload a file with the same name as an existing file, the old file may be replaced.
   *   **Merge**: If you upload new scans to an existing session, they will be added to that session.
   
   Always check your project's upload settings and ensure you are uploading to the correct Subject and Session labels.

.. caution::
   **Permissions**
   
   Your ability to upload, archive, or edit data depends on your user role and project permissions. If you encounter errors, ensure you have "Member" or "Owner" access to the destination project.

.. _data-anonymization-warning:

.. warning::
   **Data Anonymization**
   
   Data from MRI scanners is anonymized at the acquisition step. When uploading data manually (via Desktop Client or Compressed Uploader), ensure that your data is properly anonymized before upload. All personally identifiable information (PII) and protected health information (PHI) must be removed or de-identified according to your project's requirements.

Upload Methods
--------------

There are three primary ways to upload data to this XNAT instance.

.. contents:: Methods
   :local:
   :depth: 1

1. Uploading using Scripts (DICOM Receiver)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method is the standard way for MRI scanners and automated scripts (like `storescu` or C-STORE clients) to push data directly to XNAT.

**Connection Details**

Configure your scanner or sender script with the following parameters:

*   **Remote AE Title**: ``xnatad``
*   **Remote IP**: ``10.230.12.52``
*   **Remote Port**: ``8104``

**How it works**

Data sent to this receiver is routed to the XNAT Prearchive. From the Prearchive, you can review and archive the sessions.

**Study Description Routing**

The DICOM Study Description field is used to automatically route data during the archiving process. The routing string must follow this format:

::

   xnat://project_id/subject_label/session_label

**Examples:**
* ``xnat://MyProject/SUBJECT001/SESSION001``
* ``xnat://ResearchStudy/P001/Baseline``

If the Study Description field contains no routing information or conflicting information, the data will remain in the Prearchive until it is manually routed by an administrator or project member with appropriate permissions.

.. note::
   **Manual Routing Required**
   
   If your scanner or DICOM sender cannot populate the Study Description field with the routing string, you will need to manually route sessions from the Prearchive after they are received. Contact the XNAT NYUAD administrator if you need assistance with automated routing setup.

2. XNAT Desktop Client
~~~~~~~~~~~~~~~~~~~~~~

The **XNAT Desktop Client** is a standalone application that provides a robust way to upload large batches of data or complex folder structures. It is recommended for users who prefer a graphical interface with resumable uploads.

**Installation**
Ensure you have the XNAT Desktop Client installed. (See :doc:`install_desktop_client` if available, or check the `Official XNAT Desktop Client Wiki <https://wiki.xnat.org/xnat-tools/xnat-desktop-client>`_).

**Step-by-Step Upload Guide**

1.  **Login**: Open the Desktop Client and log in with your XNAT credentials.
2.  **Start Upload**: Click the **Upload Images** button on the main dashboard.

    .. figure:: images/desktop_client_upload_button.png
       :alt: XNAT Desktop Client Dashboard
       
       *[SCREENSHOT: XNAT Desktop Client Dashboard - highlighting the 'Upload Images' button]*

3.  **Select Project**: Choose the destination project for your upload. The Desktop Client will retrieve project-specific settings that may affect your upload workflow.

4.  **Select Files**: Drag and drop your DICOM folders or use the file browser to select them. The client will scan the files to identify image sessions.

**Single Session Upload Workflow**

For single session uploads, you have access to the following options:

*   **Subject Selection**: Choose an existing subject from your project, or create a new subject if your project allows subject creation.
*   **Subject Label**: Ensure this matches your project's naming convention.
*   **Session Label**: The client will auto-generate a session label based on the subject label and other variables. You can override this label if needed.
*   **Scan Selection**: You can select which scan series to include in the upload. By default, all scans are selected.

**Bulk Upload Workflow**

If you have multiple image sessions queued, you will be taken to the Bulk Upload Screen. Bulk upload may be restricted for some projects. When available, you can:

*   Apply standard subject and session labeling patterns
*   Upload multiple sessions in a single workflow
*   Note: Some features available in single session uploads (like scan selection) are not available in bulk upload mode until after the upload process

For more details on bulk upload workflows, see the `official XNAT documentation on uploading image sessions <https://wiki.xnat.org/xnat-tools/uploading-image-sessions>`_.

**Transfer Management**

5.  **Upload**: Click **Start Upload**. You will be taken to the transfer manager screen where you can:
    *   Monitor upload progress in real-time
    *   Pause, resume, or cancel uploads
    *   Start another workflow while uploads continue in the background
    
    As long as the application is running and you have an active network connection, uploads will proceed in the background.

For more information on managing transfers, see the `official XNAT documentation on managing data transfers <https://wiki.xnat.org/xnat-tools/managing-data-transfers>`_.

**Project Settings**

Some project settings may affect your upload workflow, including:

*   **Allow Subject Creation**: Whether you can create new subjects during upload
*   **Upload Destination**: Whether data goes directly to Archive or to Prearchive first
*   **Date Verification**: Whether you must verify the visit date before uploading
*   **Bulk Upload Restrictions**: Whether bulk uploads are allowed for the project
*   **Series Import Filters**: Which scan series are allowed or blocked

These settings may not be enabled for all projects. If you have questions about project-specific settings or encounter restrictions during upload, contact the XNAT NYUAD administrator.

For more information on project settings, see the `official XNAT documentation on setting project defaults <https://wiki.xnat.org/xnat-tools/setting-project-defaults-for-desktop-client-behavi>`_.

3. Compressed Uploader
~~~~~~~~~~~~~~~~~~~~~~

The **Compressed Uploader** is a web-based tool for quickly uploading zipped archives of DICOM or ECAT sessions. This is useful for single-session uploads or when you already have compressed archives.

**Supported Formats**: ``.zip``, ``.tar.gz`` containing DICOM or ECAT files.

**Instructions**

1.  Log in to the XNAT web interface.
2.  In the top navigation bar, go to **Upload** > **Images** > **Compressed Uploader**.

    .. figure:: images/compressed_uploader_menu.png
       :alt: Compressed Uploader Menu Navigation
       
       *[SCREENSHOT: Web UI Navigation - showing Upload > Images > Compressed Uploader]*

3.  **Select Project**: Choose the destination project.
4.  **Select Destination**:
    *   **Prearchive**: Recommended for safety. Allows review before archiving.
    *   **Archive**: Direct upload. Use only if you are confident in the data integrity and labels.
5.  **Choose File**: Click **Browse** to select your ``.zip`` or ``.tar.gz`` file.

    .. figure:: images/compressed_uploader_page.png
       :alt: Compressed Uploader Page
       
       *[SCREENSHOT: Compressed Uploader Page - showing file selection and project dropdown]*

6.  **Start Upload**: Click **Upload**. Wait for the confirmation message.

Data Preparation
----------------

Regardless of the method used, ensuring your data is organized helps prevent errors.

**DICOM Structure Requirements**

*   **Standard Directory Structure**: Keep standard DICOM directory structures. Each session should be in its own folder.
*   **Unique IDs**: Ensure Patient IDs and Study Instance UIDs are consistent within a session.
*   **File Organization**: Organize DICOM files in a logical folder hierarchy. Avoid deeply nested folders that may cause issues during upload.

**Pre-Upload Checklist**

*   Verify that all DICOM files are present and readable
*   Ensure data is properly anonymized (see the :ref:`data-anonymization-warning` section above)
*   Remove non-image files (like desktop thumbs, hidden system files, or log files) before zipping for the Compressed Uploader
*   Check that Subject and Session labels follow your project's naming conventions
*   Verify you have the necessary permissions for the target project

**Common File Structure Issues**

*   **Mixed File Types**: Ensure folders contain only DICOM files. Remove any non-DICOM files before upload.
*   **Corrupted Files**: Corrupted DICOM files may cause upload failures. Verify file integrity before uploading.
*   **Incomplete Sessions**: Ensure all scan series for a session are included in the upload folder.

Troubleshooting
---------------

**Connection Issues (DICOM Receiver)**

*   **Connection Refused**: Check if you are on the correct network (VPN/Intranet) to access ``10.230.12.52``.
*   **Data Not Routing Automatically**: Verify that the DICOM Study Description field contains the routing string in the format ``xnat://project_id/subject_label/session_label``. If the routing string is missing or incorrect, data will remain in the Prearchive until manually routed.

**Permission Errors**

*   **Cannot Upload to Project**: Ensure you have "Member" or "Owner" access to the destination project. Contact the project owner or XNAT NYUAD administrator if you need access.
*   **Cannot Create Subject**: Some projects restrict subject creation. You must register subjects in the project before uploading data to them. Check with the project owner or administrator.

**Upload Failures**

*   **Upload Failed (Web/Desktop)**: Check your file permissions and quota. Ensure special characters are not used in Subject/Session labels.
*   **Series Rejected**: Some projects have Series Import Filters that whitelist or blacklist specific scan series. Rejected series will not appear in the Prearchive or Archive. Contact the project administrator if you believe a series should be accepted.

**Subject and Session Labeling Issues**

*   **Invalid Characters**: Avoid special characters in Subject and Session labels. Use alphanumeric characters, hyphens, and underscores.
*   **Duplicate Labels**: The Desktop Client will warn you if a Subject or Session label already exists. You can override this, but be aware that data may merge with existing sessions.

**Date Verification**

*   **Date Verification Required**: Some projects require you to enter the visit date before uploading. If you don't know the date, you can select "I don't know the dates of these sessions" to proceed, but this may violate your project's recommended processes.

**Bulk Upload Restrictions**

*   **Bulk Upload Not Available**: Some projects restrict bulk uploads for security or workflow reasons. You may need to upload sessions one at a time. Contact the project administrator if you need bulk upload enabled.

**General Issues**

*   **Slow Uploads**: Large datasets take time to upload. Use the transfer manager to monitor progress. Uploads continue in the background as long as the Desktop Client is running.
*   **Network Interruptions**: The Desktop Client supports resumable uploads. If your connection is interrupted, you can resume the upload when connectivity is restored.

See Also
--------

**Related Documentation**

*   :doc:`install_desktop_client` - Installation and setup guide for Desktop Client
*   :doc:`project_management` - Project management and configuration
*   :doc:`navigation` - General XNAT navigation

**Official XNAT Documentation**

*   `XNAT Wiki: Uploading Image Sessions <https://wiki.xnat.org/xnat-tools/uploading-image-sessions>`_ - Comprehensive guide to uploading image sessions
*   `XNAT Desktop Client Documentation <https://wiki.xnat.org/xnat-tools/xnat-desktop-client>`_ - Complete Desktop Client reference
*   `Setting Project Defaults for Desktop Client Behavior <https://wiki.xnat.org/xnat-tools/setting-project-defaults-for-desktop-client-behavi>`_ - Project configuration options
*   `Managing Data Transfers <https://wiki.xnat.org/xnat-tools/managing-data-transfers>`_ - Transfer management guide