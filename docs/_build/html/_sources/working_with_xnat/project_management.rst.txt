Project Management
==================

This guide summarizes common project-level tasks for project owners and coordinators.

Project Roles
-------------

XNAT access is controlled at the project level. Common roles include:

- **Owner**: Can manage project settings, users, and data.
- **Member**: Can usually view, upload, download, and run enabled workflows.
- **Read-only access**: Can view and download data when permitted.

Exact permissions can vary by project configuration. If a user cannot see an expected action, first confirm their project role.

Adding or Updating Access
-------------------------

To request project access changes, email admin.nyuad.xnat@nyu.edu with:

- Project ID or project name
- User name and email address
- Requested role
- Brief reason for the access request

Use the least privileged role that supports the user's work.

Project Setup Checklist
-----------------------

Before collecting or uploading data, project owners should confirm:

1. Project name and ID are correct.
2. Subject and session label conventions are documented.
3. Upload destination is understood: Prearchive or Archive.
4. Required pipelines are enabled. See :doc:`enabling_pipelines`.
5. Project members know how to request support.
6. Data anonymization requirements are clear to the research team.

Naming Conventions
------------------

Consistent labels make uploads, transfers, and analysis easier. A simple convention such as ``sub-0001`` and ``ses-01`` works well for many projects.

Avoid spaces, special characters, and labels that could identify participants. Use only project-approved identifiers.

When to Contact Administrators
------------------------------

Contact admin.nyuad.xnat@nyu.edu for:

- New project setup
- Large access changes
- Pipeline enablement or custom pipeline requests
- Bulk transfer planning
- Unexpected merge, deletion, or archiving issues
- Questions about public documentation or user guidance
