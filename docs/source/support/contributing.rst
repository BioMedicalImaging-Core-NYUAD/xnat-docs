Contributing to this repository
===============================

Your contribution, mistake correction, code contributions are very welcome.
Contributions are made through pull reqests, please do the following steps:

- Fork the current repository to your account
- Create a new branch named with the feature you are developping or change you are making
- Make the change on that branch
- Create a pull request from this branch  to the main brach
- Wait until your pull request is approved, or commented on
- Address all comments until the PR is approved
- Once the PR is merged to the main branch, delete your branch


Sphinx header templates
^^^^^^^^^^^^^^^^^^^^^^^


If you'd like to contribute to this documentation, please follow the heading-adornment conventions below:

+---------------------+------------------------+----------------+------------+
| Level               | Overline & Underline   | Underline only | Character  |
+=====================+========================+================+============+
| Document title      | ``=============``      | N/A            | ``=``      |
+---------------------+------------------------+----------------+------------+
| Top-level section   | ``-------------``      | ``-----------``| ``-``      |
+---------------------+------------------------+----------------+------------+
| Sub-section         | N/A                    | ``^^^^^^^^``   | ``^``      |
+---------------------+------------------------+----------------+------------+
| Sub-sub-section     | N/A                    | ``""""""""``   | ``"``      |
+---------------------+------------------------+----------------+------------+
| Fourth-level        | N/A                    | ``~~~~~~~~``   | ``~``      |
+---------------------+------------------------+----------------+------------+
| Fifth-level         | N/A                    | ``++++++++``   | ``+``      |
+---------------------+------------------------+----------------+------------+


Referencing your code that is in a repository or submodule into the documentation pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can reference code parts or full scripts that are in the repository or a submodule as such (Check the .rst code of this page)


.. literalinclude:: ../../../fmriprep/code/fmriprep.py
  :language: python