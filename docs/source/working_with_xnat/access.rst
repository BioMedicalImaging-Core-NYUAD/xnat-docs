Accessing XNAT
==============

This guide covers how to access the NYUAD XNAT platform, from initial account creation to project access.

Account Registration
--------------------

**For First-Time Users**

If you don't have an XNAT account, follow these steps to register:

**Step 1: Navigate to XNAT**
   Visit https://xnat.abudhabi.nyu.edu

**Step 2: Sign in with Google**
   Click the "Sign in with Google" button to begin registration.

   .. image:: ../_static/Sign_in_page.png
      :alt: XNAT sign-in page showing Google authentication
      :align: center
      :width: 500px

**Step 3: Complete Registration**
   Enter your first and last name in the required fields.

   .. image:: ../_static/Reg_page.png
      :alt: Registration form with name fields
      :align: center
      :width: 500px

**Step 4: Submit Registration**
   Scroll to the bottom and click "Register" to submit your account request.

Account Approval Process
------------------------

**Authorization Required**
   All new accounts require administrator approval for security purposes.

**Approval Timeline**
   - Your registration request is sent to the site administrator
   - **Contact**: Soumen Mohanty (soumen.mohanty@nyu.edu)
   - **Processing time**: Typically 1-2 business days

**Approval Notification**
   You'll receive an email confirmation once your account is approved.

Project Access
--------------

**Requesting Project Access**

After your account is approved, you'll need access to specific projects:

1. **Identify Projects**: Determine which research projects you need access to
2. **Email Request**: Contact Soumen Mohanty (soumen.mohanty@nyu.edu) with:
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

   - Go to your profile → "Manage Alias Tokens"
   - Create new tokens as needed
   - Use tokens instead of passwords for security

**Password Requirements**
   No separate XNAT password needed - authentication is handled through Google OAuth.

**Session Management**
   - Sessions remain active while using XNAT
   - Log out when finished for security
   - Re-authentication required after extended inactivity

Troubleshooting
---------------

**Account Issues**

**Registration Not Approved**
   If your account hasn't been approved after 3 business days, email Soumen Mohanty directly.

**Can't Access Projects**
   Verify you've requested access to specific projects. General account approval doesn't include project access.

**Sign-in Problems**
   Ensure you're using the same Google account that was registered and approved.

**Google Authentication Issues**
   - Clear browser cache and cookies
   - Try an incognito/private browser window
   - Ensure pop-ups are allowed for the XNAT site

Getting Help
------------

**Primary Contact**
   Soumen Mohanty: soumen.mohanty@nyu.edu
   - Account approval requests
   - Project access requests
   - Technical access issues

**Support Requests**
   When contacting support, include:
   - Your full name and email address
   - Specific error messages (if any)
   - Which projects you're trying to access
   - Screenshots of any error pages

Next Steps
----------

After gaining access to XNAT:

- Explore :doc:`navigation` to learn the XNAT interface
- Set up :doc:`install_desktop_client` for bulk downloads
- Learn about :doc:`../data_download/overview` methods
- Review :doc:`../processing_pipelines/overview` for data analysis