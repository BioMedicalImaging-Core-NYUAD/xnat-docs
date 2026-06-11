XNAT Navigation Basics
======================

This guide introduces the main areas of the XNAT web interface and where common actions live.

Main Hierarchy
--------------

XNAT data is organized in a hierarchy:

::

   Project -> Subject -> Session -> Scan -> Resource

- **Project**: A study, collaboration, or data collection.
- **Subject**: A participant or research subject within a project.
- **Session**: A visit or scan session for that subject.
- **Scan**: An individual imaging series.
- **Resource**: Files attached to a project, subject, session, or scan. Pipeline outputs are usually stored as resources.

Finding Your Data
-----------------

1. Log into XNAT at https://xnat.abudhabi.nyu.edu.
2. Open the project list from the home page or navigation menu.
3. Select your project.
4. Use the subject table to open the participant you need.
5. Open the session to review scans, resources, and available actions.

Common Actions
--------------

- **Upload data**: Use the project or upload menu. See :doc:`uploading`.
- **Review pending uploads**: Use **Upload** > **Go to prearchive**. See :doc:`prearchive`.
- **Download data**: Use browser download options or the Desktop Client. See :doc:`../data_download/browser`.
- **Run a pipeline**: Open the session or project and use the available actions menu. See :doc:`running_pipelines`.
- **Manage project settings**: Project owners can adjust selected project settings. See :doc:`project_management`.

Tips
----

- If a button or menu item is missing, you may not have the required project role.
- If a session is not where you expect it to be, check the Prearchive before assuming the upload failed.
- Use consistent subject and session labels. This avoids accidental merges and makes pipeline outputs easier to interpret.
