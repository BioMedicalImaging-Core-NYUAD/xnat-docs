Understanding the Prearchive
============================

The **Prearchive** is where XNAT stages uploaded imaging sessions before saving
them to the **Archive**, where they appear under a subject in the project.
While an upload is staged, you can check that it contains the expected scans
and is going to the right project and subject.

When uploads need manual archiving
----------------------------------

XNAT can archive uploads automatically or leave them in the Prearchive for
review, depending on the project settings and upload method. If your project
uses automatic archiving, look for the session in the destination project once
the upload has finished. Sessions left in the Prearchive can be reviewed and
archived by someone with permission to archive in the destination project.

.. _review-and-archive-prearchive:

Review and archive a session
----------------------------

Use **Review and Archive** to check the destination and save one staged session.

Find and review an upload
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Sign in to XNAT and choose **Upload** > **Go to prearchive**.
2. Find the row for your **Project**, **Subject**, **Session** and **Scan Date**.
   If the row is missing, see :ref:`prearchive-troubleshooting`.
3. Click the row to highlight it. Use **Details** to inspect the session and scan
   list. Compare the scans and file counts with what you expected to upload.
4. When the session shows **Ready** and the scans match what you expect,
   continue to the next step. For other statuses or unexpected data, see
   :ref:`prearchive-troubleshooting`.

.. _prearchive-confirm-destination:

Confirm the destination and submit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Highlight the intended row, then click **Check** above the table. Confirm
   that only that session is checked. Highlighting a row shows its details.
   Checking it selects it for the archive action.
2. Click **Review and Archive** in the **Actions** panel.
3. On the review form, confirm the **Project** and **Subject** and review the
   scans. Find the editable field containing the current **session label**.
4. Keep the proposed label if it is unused. To archive the upload as a separate
   session, enter a label that is unused in that project. Follow your project's
   naming convention. For example, a fuller export of
   ``ExampleSubject_ses_03`` might be saved as ``ExampleSubject_ses_03_recovered``.
   The recovery label refers to the same visit.
5. Click **Submit**. If XNAT warns that it will merge with or overwrite an
   existing session, cancel and recheck the destination and label.

.. figure:: ../_static/prearchive-review-and-archive.png
   :alt: In the Prearchive, select one row with Check and open Review and Archive. On the review form, confirm the project and subject, edit the session label and click Submit.
   :align: center
   :width: 720px

   Illustration with example labels. Use **Check** to select the row, then edit
   the label on the **Review and Archive** form.

Verify the archived session
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Wait for archiving to finish. Use **Refresh** if the row still shows
   **Archiving now**.
2. Open the destination project and subject, then locate the session under the
   label you submitted.
3. Confirm the project, subject, scan date, scan list and available file counts
   against the upload you reviewed. If you saved a recovery copy, identify the
   verified session when handing it off for analysis.

.. _prearchive-troubleshooting:

Troubleshoot an upload
----------------------

The upload is missing or still processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you cannot find the upload, check the destination project in the Archive and
clear any Prearchive filters that might hide the row. For **Receiving** or
**Building**, wait for XNAT to finish and click **Refresh**.

The upload shows Conflict or Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Conflict**: Compare the staged upload with the existing archive session.
  If both copies should be kept, follow :ref:`prearchive-confirm-destination`
  and enter an unused session label.
  For a Study Instance UID mismatch, see :doc:`uid_errors_archiving`.
* **Error**: Open **Details** to check the message. Contact XNAT support if
  the error persists or you are unsure how to proceed.

The scans or subject look wrong
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ask the project owner or XNAT support to review an incomplete upload, an upload
assigned to a different subject, or a duplicate of a complete archive session
before archiving it.

See also
--------

- :doc:`uploading`
- :doc:`transferring_data`
- `XNAT Wiki: Using the Prearchive <https://wiki.xnat.org/documentation/using-the-prearchive>`_
