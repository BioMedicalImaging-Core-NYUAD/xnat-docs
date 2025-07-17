Download via Desktop Client
===========================

This guide covers using the XNAT Desktop Client for downloading data from XNAT. The Desktop Client provides the most reliable method for downloading large datasets with features like pause, resume, and background processing.

Prerequisites
-------------

- **XNAT Desktop Client installed** - see :doc:`../working_with_xnat/install_desktop_client`
- **Server connection configured** with your XNAT credentials
- **Network access** to xnat.abudhabi.nyu.edu

XML Catalog File Download via Desktop Client
--------------------------------------------

1. **Generate catalog file in XNAT:**

   - Go to your project and select "Download Images"
   - Choose "Catalog XML (.xml)" as the download format
   - Download the .xml file to your computer

2. **Import to Desktop Client:**

   - Open XNAT Desktop Client
   - Ensure you're logged into the correct XNAT server
   - Select "Download Files" from the main menu
   - Browse and select your downloaded .xml file
   - Set download location and click "Download"

For comprehensive downloading instructions, see the `official download guide <https://wiki.xnat.org/xnat-tools/downloading-image-sessions>`_.

Transfer Management
-------------------

**Progress Monitoring:**

- The Transfer Monitor shows real-time download progress
- Track file counts, transfer speeds, and estimated completion time
- View "Download Progress" for active transfers
- Access "View Archived Transfers" for download history

**Transfer Controls:**

- **Pause** downloads as needed
- **Resume** interrupted downloads
- **Cancel** transfers if necessary
- Downloads continue in background even if you close your browser

**Performance Note:** Current download speed is limited to 5MB/s.

File Organization
-----------------

Downloaded files are organized as follows:

- **Root folder:** Named after your XNAT server (e.g., "xnat.abudhabi.nyu.edu")
- **Structure:** Maintains XNAT's project/subject/session/scan hierarchy
- **File names:** Preserves original names and metadata
- **Location:** Files download to your specified download location

Download Options
----------------

**Scan Formats:**
- DICOM (original format)
- NIfTI (converted format)  
- Analyze and other converted formats

**Scan Types:**
- Filter by specific scan types from your sessions
- Include/exclude particular acquisition types

**Resource Types:**
- Raw imaging data
- Processed data and derivatives
- Assessment files and reports

**File Structure:**
- Keep original XNAT folder hierarchy (recommended)
- Simplified structure (not recommended - uncheck this option)

Authentication and Security
---------------------------

**Secure Authentication:**
- Desktop Client uses secure tokens, never saves passwords
- Authentication is passed automatically from XNAT web session
- Must reauthenticate for each new session

**Session Management:**
- Desktop Client creates its own user session
- Downloads can continue even after closing browser
- Avoid conflicting sessions by ensuring consistent login credentials

Troubleshooting
---------------

**Conflicting Sessions:**
- Issue: Download conflicts with existing Desktop Client session
- Solution: Ensure you're logged into the same XNAT server with the same credentials in both web browser and Desktop Client

**Slow Downloads:**
- Current speed limit: 5MB/s
- Large datasets will take time - use pause/resume as needed
- Plan downloads during off-peak hours

**Failed Downloads:**
- Check network connectivity to xnat.abudhabi.nyu.edu
- Verify authentication credentials are current
- Use Transfer Monitor to identify specific failed files

**Download Location Issues:**
- Set a default download location in Application Settings
- Ensure sufficient disk space for large datasets
- Check folder permissions for write access

Getting Help
------------

**For Desktop Client specific issues:**
- Review the `official XNAT Desktop Client documentation <https://wiki.xnat.org/xnat-tools/xnat-desktop-client-dxm>`_
- Check `application settings guide <https://wiki.xnat.org/xnat-tools/xnat-desktop-client-dxm/application-settings>`_
- Consult `version compatibility matrix <https://wiki.xnat.org/xnat-tools/desktop-client-version-compatibility-matrix>`_

**For download issues:**
- Contact support with Transfer Monitor logs
- Include session details and error messages
- Specify file types and sizes involved

Next Steps
----------

After downloading your data:

1. **Organize locally** according to your analysis workflow
2. **Verify data integrity** by checking file counts and sizes
3. **Begin analysis** with your preferred tools
4. **Consider automation** for regular download workflows

Related Documentation
---------------------

- :doc:`../working_with_xnat/install_desktop_client` - Installation guide
- :doc:`browser` - Web browser download method
- :doc:`python_scripts` - Programmatic download methods