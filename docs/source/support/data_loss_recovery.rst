Data Loss and Recovery
=======================

This page provides information about XNAT backup procedures and data recovery options.

Backup Procedures
-----------------

XNAT at NYUAD maintains regular backups to protect against data loss:

**Daily Backups**
- Rolling backups are taken every night
- These backups capture the current state of the XNAT system

**Full Backups**
- Two full backups are created every 30 days
- Full backups are retained for up to 60 days

These backup procedures help ensure data can be recovered in case of system failures or accidental deletions.

Data Deletion and Cache
------------------------

When data is deleted from XNAT:

- **User Deletion**: Data deleted by users is removed from the active system
- **Temporary Cache**: XNAT may store deleted data temporarily in its cache
- **Permanent Removal**: After cache expiration, data is permanently removed from the active system

**Important**: Once data is permanently removed from the system and cache, it cannot be recovered without restoring from backups.

Data Recovery
-------------

**User-Side Recovery**

Data recovery is **not available from the user side**. Once data is deleted, users cannot restore it themselves.

**Administrator-Assisted Recovery**

If you have experienced data loss or need to recover deleted data:

1. **Contact XNAT Administrators**: Email admin.nyuad.xnat@nyu.edu immediately
2. **Provide Details**: Include:
   - Project name and ID
   - Subject and session labels (if applicable)
   - Approximate date/time of deletion
   - Description of what was lost
3. **Recovery Process**: Administrators can restore data from backups if:
   - The data loss occurred within the backup retention period (60 days for full backups)
   - The backup contains the data you need
   - Recovery is technically feasible

**Recovery Timeline**

- Recovery requests are processed as quickly as possible
- Recovery time depends on:
  - The size of data to be recovered
  - The age of the backup needed
  - Current system load
- You will be notified once recovery is complete or if recovery is not possible

Preventing Data Loss
--------------------

To minimize the risk of data loss:

1. **Verify Before Deleting**: Always verify data before deletion, especially when transferring data between projects
2. **Use Prearchive**: When uploading, use Prearchive first to review data before archiving
3. **Document Important Data**: Keep records of critical data and processing steps
4. **Regular Backups**: For critical analysis results, maintain your own backups outside of XNAT
5. **Coordinate Deletions**: For large-scale deletions, coordinate with project administrators

See Also
--------

- :doc:`../working_with_xnat/transferring_data` - For safe data transfer procedures
- :doc:`../working_with_xnat/running_pipelines` - For pipeline execution and data management
- :doc:`../working_with_xnat/uploading` - For upload procedures and Prearchive usage
- :doc:`contact` - For administrator contact information
- :doc:`troubleshooting` - For troubleshooting data access issues

