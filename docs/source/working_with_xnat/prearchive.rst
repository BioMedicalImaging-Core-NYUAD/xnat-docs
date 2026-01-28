Understanding the Prearchive
============================

The **Prearchive** is XNAT's staging area where uploaded data is held temporarily before being committed to the permanent Archive. Understanding how the Prearchive works is essential for managing data uploads and resolving conflicts.

What is the Prearchive?
------------------------

The Prearchive is a temporary holding area where:

- Data is stored after upload but before permanent archiving
- You can review, inspect, and modify data before it becomes permanent
- Conflicts and errors can be identified and resolved
- Data can be deleted or corrected without affecting the Archive

Think of the Prearchive as a "review queue" where you have full control over the data before it's permanently stored.

What Operations Are Allowed in Prearchive
------------------------------------------

In the Prearchive, you can:

- **Review data**: Inspect sessions, scans, and metadata before archiving
- **Edit labels**: Modify Subject IDs and Session Labels to resolve conflicts
- **Delete data**: Remove sessions that are incorrect or no longer needed
- **Resolve conflicts**: Fix UID conflicts, labeling issues, or metadata problems
- **Inspect scans**: Review individual scans and their properties
- **Bulk operations**: Process multiple sessions simultaneously

Once data is archived, these operations become more restricted. The Prearchive gives you the flexibility to fix issues before data becomes permanent.

Why Prearchive is Crucial for Catching Conflicts
-------------------------------------------------

The Prearchive workflow allows you to:

1. **Identify conflicts early**: UID conflicts, duplicate labels, and other issues are detected and flagged in the Prearchive before archiving
2. **Review before committing**: You can see exactly what data will be merged and identify conflicts
3. **Resolve issues safely**: Fix labeling or mapping issues without affecting archived data
4. **Avoid data corruption**: Prevent invalid merges from reaching the Archive

Prearchive Status Indicators
-----------------------------

Sessions in the Prearchive display status indicators that help you identify issues:

- **Ready**: Data is ready to be archived (no conflicts detected)
- **Conflict**: A conflict has been detected (UID conflicts, duplicate labels, etc.)
- **Error**: An error occurred during processing
- **Receiving**: Data is still being uploaded
- **Building**: XNAT is processing the uploaded data

When you see a "Conflict" status, it means XNAT has detected an issue (such as a UID conflict) that must be resolved before archiving can proceed.

The Prearchive Workflow
------------------------

The typical workflow is:

::

   Upload → Prearchive → Review/Resolve → Archive

1. **Upload**: Data is uploaded to XNAT (via Desktop Client, Compressed Uploader, or DICOM receiver)
2. **Prearchive**: Data lands in the Prearchive for review
3. **Review/Resolve**: You review the data, identify conflicts, and fix any issues (like UID conflicts, incorrect labels, etc.)
4. **Archive**: Once conflicts are resolved, data is archived to permanent storage

This workflow ensures that data integrity issues are caught and resolved before data becomes permanent.

Accessing the Prearchive
-------------------------

To access the Prearchive:

1. Log into XNAT
2. Navigate to **Upload** > **Go to prearchive** from the top navigation menu
3. You'll see a table of sessions waiting to be archived, with their current status

From the Prearchive, you can:

- Review session details
- Edit Subject IDs and Session Labels
- Select sessions and click "Review and Archive" to proceed with archiving
- Delete sessions that are incorrect
- Resolve conflicts before archiving

See Also
--------

**Related Documentation**

- :doc:`uploading` - Upload procedures and methods
- :doc:`uid_errors_archiving` - Resolving UID errors in Prearchive
- :doc:`transferring_data` - Transferring data between projects

**Official XNAT Documentation**

- `XNAT Wiki: Prearchive <https://wiki.xnat.org/display/XNAT18/Prearchive>`_ - Official documentation on the Prearchive system
- `XNAT Wiki: Archiving Data <https://wiki.xnat.org/display/XNAT18/Archiving+Data>`_ - Information about the archiving process
