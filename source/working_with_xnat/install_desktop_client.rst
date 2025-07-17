Install XNAT Desktop Client
===========================

The XNAT Desktop Client (also called "Data Transfer Manager" or DXM) is a robust desktop application for downloading imaging data from XNAT servers. It's particularly valuable for downloading large datasets reliably with pause, resume, and cancel capabilities.

**Key Advantages:**
- **Bulk download reliability** - handles large datasets that might fail with browser downloads
- **Transfer management** - pause, resume, and cancel downloads as needed
- **Background processing** - downloads continue even if you close your browser
- **Automatic authentication** - seamless integration with XNAT web interface

For comprehensive documentation, visit the `official XNAT Desktop Client documentation <https://wiki.xnat.org/xnat-tools/xnat-desktop-client-dxm>`_.

Download and Installation
-------------------------

**Download Location:** https://www.xnat.org/download/desktop-client/

Windows Installation
~~~~~~~~~~~~~~~~~~~~

1. **Download** the .exe file from the official download page
2. **Run** the .exe file to launch the one-step installer
3. **Automatic setup** - installing the application will automatically install file-handling support for all your browsers

macOS Installation
~~~~~~~~~~~~~~~~~~

1. **Download** the .DMG file from the official download page
2. **Install** by opening the .DMG file and dragging the app into your Applications folder
3. **Security setup** - if you get a security warning when launching:
   - Open System Preferences > Security > General
   - Look for a message about this app and click "Open Anyway"

Linux Installation
~~~~~~~~~~~~~~~~~~

Linux installation requires additional setup steps. For detailed instructions, see the `official Linux installation guide <https://wiki.xnat.org/xnat-tools/installing-the-xnat-desktop-client>`_.

**Requirements:**
- Compatible JRE (Java Runtime Environment)
- C++ ABI version 1.3.9 support
- Supported distributions: Ubuntu 18.04+, CentOS 8

**Basic Steps:**
1. Verify system requirements
2. Install Java 8 JRE
3. Download .AppImage file
4. Make file executable and run

System Requirements
-------------------

**General:**
- Compatible with Mac, Windows, and Linux
- Recommended for native (non-virtualized) systems
- Network access to your XNAT server

**Linux Specific:**
- Java 8 JRE
- C++ ABI version 1.3.9 support
- Note: RHEL/CentOS 7.x and Fedora 19 (and earlier) are not supported

Initial Setup
-------------

**Server Connection:**
1. Launch the XNAT Desktop Client
2. Click "Settings" (gear icon) in the upper right corner
3. Navigate to server connections
4. Add your XNAT server:
   - **Server URL**: ``xnat.abudhabi.nyu.edu``
   - **Username**: Your XNAT alias (get from browser: click your name → copy alias)
   - **Password**: Secret key (get from browser: click your name → copy secret)

.. note::
   The Desktop Client uses secure tokens rather than passwords and never saves XNAT account passwords. You'll need to reauthenticate each session.

**Default Download Location:**
Set a default download location in Application Settings to avoid selecting a folder each time.

Verification
------------

After installation, verify the setup by:

1. **Launch** the Desktop Client
2. **Connect** to your XNAT server using your credentials
3. **Test** with a small download to ensure everything works properly

Troubleshooting
---------------

**Security Warnings (macOS):**
- Open System Preferences > Security > General
- Allow the application when prompted

**Connection Issues:**
- Verify server URL is correct: ``xnat.abudhabi.nyu.edu``
- Ensure you're using alias/secret from XNAT web interface
- Check network connectivity to XNAT server

**Linux Installation Issues:**
- Verify Java 8 JRE is properly installed
- Check C++ ABI compatibility
- Consult the `official Linux guide <https://wiki.xnat.org/xnat-tools/installing-the-xnat-desktop-client>`_

Next Steps
----------

Once installed and configured:

1. **Learn to use** the client: :doc:`../data_download/desktop_client`
2. **Download data** from your XNAT projects
3. **Set up** automated download workflows

Related Documentation
---------------------

- :doc:`../data_download/desktop_client` - Using the Desktop Client
- :doc:`../data_download/browser` - Browser download methods
- `Official XNAT Desktop Client Documentation <https://wiki.xnat.org/xnat-tools/xnat-desktop-client-dxm>`_