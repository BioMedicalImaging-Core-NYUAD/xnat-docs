Accessing XNAT
==============

This guide covers how to access the NYUAD XNAT platform, from initial account creation to project access.

Account Registration
--------------------

   .. image:: ../_static/5.1.access.png
      :alt: access
      :align: center
      :width: 900px

--------------------------------

**Step 1: Navigate to XNAT**
   Visit https://xnat.abudhabi.nyu.edu

**Step 2: Sign in with Google**
   Click the "Sign in with Google" button to begin registration.

**Step 3: Complete Registration**
   Enter information in the required fields.

**Step 4: Submit Registration**
   Scroll to the bottom and click "Register" to submit your account request.

Account Approval Process
------------------------

**Authorization Required**
   All new accounts require administrator approval for security purposes.

**Approval Timeline**
   - Your registration request is sent to the site administrator
   - **Contact**: admin.nyuad.xnat@nyu.edu
   - **Processing time**: Typically 1-2 business days

**Approval Notification**
   You'll receive an email confirmation once your account is approved.

Project Access
--------------

**Requesting Project Access**

After your account is approved, you'll need access to specific projects:

1. **Identify Projects**: Determine which research projects you need access to
2. **Email Request**: Contact us (admin.nyuad.xnat@nyu.edu) with:

   - Your name and email address
   - Specific project names you need access to
   - Brief explanation of your role/purpose

**Project Access Timeline**
   Project access is typically granted within 1 business day of request.

Signing In
----------

**For Existing Users**

Once your account is approved:

1. Navigate to https://xnat.abudhabi.nyu.edu
2. Click "Sign in with Google"
3. Use your approved Google account credentials
4. Access your authorized projects

**Authentication Method**
   XNAT uses Google OAuth for secure authentication. You must use the same Google account that was approved during registration.

Account Management
------------------

**API Tokens**
   For programmatic access (scripts, automated downloads):

   .. image:: ../_static/5.1.API.png
      :alt: API
      :align: center
      :width: 900px

--------------------------------

   - Go to your profile → "Manage Alias Tokens"
   - Create new tokens as needed
   - Use tokens instead of passwords for security

**Password Requirements**
   No separate XNAT password needed - authentication is handled through Google OAuth.

**Session Management**
   - Sessions remain active while using XNAT
   - Log out when finished for security
   - Re-authentication required after extended inactivity

Next Steps
----------

After gaining access to XNAT:

- Explore :doc:`navigation` to learn the XNAT interface
- Set up :doc:`install_desktop_client` for bulk downloads
- Learn about :doc:`../data_download/browser` methods
- Review :doc:`../processing_pipelines/overview` for data analysis