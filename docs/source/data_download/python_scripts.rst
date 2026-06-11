XNAT API with Python
====================

This guide shows how to use Python to work with NYUAD XNAT directly from your laptop, lab workstation, or Jubail HPC. It is intended for users who want to create their own scripts instead of asking XNAT administrators to write one-off download or processing helpers.

Most users should start with the official Python package:

- Install package: ``pip install xnat``
- Package documentation: `XNAT Python Client <https://xnat.readthedocs.io/en/stable/>`_
- XNAT server: ``https://xnat.abudhabi.nyu.edu``

When to Use the API
-------------------

Use the API when the browser or Desktop Client is too manual for your workflow. Common examples include:

- Download all scans for selected subjects and sessions.
- Download only one scan type, such as T1w, DWI, or fieldmaps.
- Download only pipeline outputs, such as ``fmriprep``, ``mriqc``, ``rawdata``, or ``freesurfer`` resources.
- Extract one specific file from many sessions, such as FreeSurfer ``aseg.stats``.
- Build a manifest of what exists in XNAT before downloading.
- Download data directly to Jubail before running your own processing.
- Run the same script repeatedly without re-downloading files that already exist.

Prefer the XNAT Desktop Client for simple large DICOM downloads. Prefer the API when you need filtering, manifests, automation, or downstream analysis.

Safety Rules
------------

Before writing scripts, follow these rules:

- Start with read-only tasks: list projects, list sessions, list resources, then download.
- Do not delete, overwrite, archive, or upload data from a script unless you have discussed the plan with the XNAT administrators.
- Test on one subject and one session before running a whole project.
- Keep a manifest of what your script downloaded.
- Never put token secrets directly in scripts, notebooks, GitHub repos, email, Slack, or shared folders.
- If an AI tool helps you write code, ask it to avoid destructive operations and to keep credentials in environment variables.

Create an Alias Token
---------------------

Use an XNAT alias token rather than your Google password.

1. Log into XNAT.
2. Click your user name in the top right.
3. Open **Manage Alias Tokens**.
4. Create a new token.
5. Copy the token alias and token secret.

Treat the alias and secret like a password. If you think they were exposed, delete the token and create a new one.

Environment Setup
-----------------

Laptop or Workstation
~~~~~~~~~~~~~~~~~~~~~

Create a small Python environment:

.. code-block:: bash

   python3 -m venv xnat-api-env
   source xnat-api-env/bin/activate
   python -m pip install --upgrade pip
   python -m pip install xnat pandas python-dotenv

If you prefer conda:

.. code-block:: bash

   conda create -n xnat-api python=3.11
   conda activate xnat-api
   pip install xnat pandas python-dotenv

Jubail HPC
~~~~~~~~~~

For workflows that produce large outputs, it is often better to download directly to Jubail instead of downloading to a laptop and uploading again.

.. code-block:: bash

   ssh <your-netid>@jubail.abudhabi.nyu.edu
   mkdir -p ~/xnat-api-work
   cd ~/xnat-api-work
   python3 -m venv xnat-api-env
   source xnat-api-env/bin/activate
   python -m pip install --upgrade pip
   python -m pip install xnat pandas python-dotenv

For long downloads or downstream processing, use a Jubail job instead of leaving work running in an interactive shell. See the CRC documentation for `Jubail system details <https://crc-docs.abudhabi.nyu.edu/hpc/system/index.html>`_ and `SLURM job submission <https://crc-docs.abudhabi.nyu.edu/hpc/jobs/quick_start.html>`_.

Secrets Management
------------------

Option 1: Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the recommended default.

.. code-block:: bash

   export XNAT_HOST="https://xnat.abudhabi.nyu.edu"
   export XNAT_USER="your-token-alias"
   export XNAT_PASS="your-token-secret"

Then your Python code can read:

.. code-block:: python

   import os

   XNAT_HOST = os.environ["XNAT_HOST"]
   XNAT_USER = os.environ["XNAT_USER"]
   XNAT_PASS = os.environ["XNAT_PASS"]

Option 2: Private ``.env`` File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a project folder on your own machine:

.. code-block:: bash

   cat > .env <<'EOF'
   XNAT_HOST=https://xnat.abudhabi.nyu.edu
   XNAT_USER=your-token-alias
   XNAT_PASS=your-token-secret
   EOF
   chmod 600 .env
   echo ".env" >> .gitignore

Use it in Python:

.. code-block:: python

   from dotenv import load_dotenv
   import os

   load_dotenv()
   XNAT_HOST = os.environ["XNAT_HOST"]
   XNAT_USER = os.environ["XNAT_USER"]
   XNAT_PASS = os.environ["XNAT_PASS"]

On Jubail, keep token files in your home directory or a private project directory. Do not store secrets in shared group folders unless the permissions are restricted.

Option 3: Prompt at Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prompting avoids saving secrets on disk:

.. code-block:: python

   import getpass

   XNAT_USER = input("XNAT alias token: ")
   XNAT_PASS = getpass.getpass("XNAT alias secret: ")

First Connection Test
---------------------

Create ``01_test_connection.py``:

.. code-block:: python

   import os
   import xnat

   host = os.environ.get("XNAT_HOST", "https://xnat.abudhabi.nyu.edu")
   user = os.environ["XNAT_USER"]
   password = os.environ["XNAT_PASS"]

   with xnat.connect(host, user=user, password=password) as session:
       print("Connected to:", host)
       print("Accessible projects:")
       for project_id in sorted(session.projects.keys()):
           print(" -", project_id)

Run it:

.. code-block:: bash

   python 01_test_connection.py

If this fails, check VPN/network access, token spelling, and project permissions.

Common XNAT Objects
-------------------

The XNAT Python client exposes XNAT as a hierarchy:

::

   session
     projects[project_id]
       subjects[subject_label]
         experiments[session_label]
           scans[scan_id]
             resources[resource_label]
               files[file_name]

In XNAT, imaging sessions are often called ``experiments`` in the API. That is normal.

List Subjects, Sessions, Scans, and Resources
---------------------------------------------

This is usually the first script to write for a new project.

.. code-block:: python

   import os
   import xnat

   PROJECT_ID = "your_project_id"

   with xnat.connect(
       os.environ.get("XNAT_HOST", "https://xnat.abudhabi.nyu.edu"),
       user=os.environ["XNAT_USER"],
       password=os.environ["XNAT_PASS"],
   ) as session:
       project = session.projects[PROJECT_ID]

       for subject in project.subjects.values():
           print(f"Subject: {subject.label}")
           for experiment in subject.experiments.values():
               print(f"  Session: {experiment.label}")
               for scan in experiment.scans.values():
                   resource_names = ", ".join(scan.resources.keys())
                   print(f"    Scan {scan.id}: {scan.type} resources=[{resource_names}]")
               if experiment.resources:
                   print("    Session resources:", ", ".join(experiment.resources.keys()))

Use the output from this script to decide what to download.

Download Selected DICOM Scans
-----------------------------

This pattern appears often in project-specific scripts: choose subjects, choose sessions, then download each scan resource.

.. code-block:: python

   import os
   from pathlib import Path
   import xnat

   PROJECT_ID = "your_project_id"
   SUBJECTS = ["Subject_0001", "Subject_0002"]
   SESSIONS = ["ses_01"]
   OUTPUT_DIR = Path("xnat_downloads")

   def safe_name(value):
       return "".join(c if c.isalnum() or c in "-_." else "_" for c in str(value))

   with xnat.connect(
       os.environ.get("XNAT_HOST", "https://xnat.abudhabi.nyu.edu"),
       user=os.environ["XNAT_USER"],
       password=os.environ["XNAT_PASS"],
   ) as session:
       project = session.projects[PROJECT_ID]

       for subject_label in SUBJECTS:
           subject = project.subjects.get(subject_label)
           if subject is None:
               print("Missing subject:", subject_label)
               continue

           for experiment in subject.experiments.values():
               if SESSIONS and experiment.label not in SESSIONS:
                   continue

               for scan in experiment.scans.values():
                   if "DICOM" not in scan.resources:
                       continue

                   scan_dir = (
                       OUTPUT_DIR
                       / safe_name(subject.label)
                       / safe_name(experiment.label)
                       / f"scan-{safe_name(scan.id)}_{safe_name(scan.type)}"
                   )
                   if scan_dir.exists() and any(scan_dir.iterdir()):
                       print("Skipping existing:", scan_dir)
                       continue

                   print("Downloading:", subject.label, experiment.label, scan.id, scan.type)
                   scan.resources["DICOM"].download_dir(str(scan_dir))

This downloads one directory per scan. For large projects, add logging and retry logic.

Download Session Resources
--------------------------

Pipeline outputs usually live in session resources such as ``rawdata``, ``mriqc``, ``fmriprep``, ``freesurfer``, or ``tractoflow``.

.. code-block:: python

   import os
   from pathlib import Path
   import xnat

   PROJECT_ID = "your_project_id"
   RESOURCE_LABEL = "fmriprep"
   OUTPUT_DIR = Path("pipeline_outputs")

   with xnat.connect(
       os.environ.get("XNAT_HOST", "https://xnat.abudhabi.nyu.edu"),
       user=os.environ["XNAT_USER"],
       password=os.environ["XNAT_PASS"],
   ) as session:
       project = session.projects[PROJECT_ID]

       for subject in project.subjects.values():
           for experiment in subject.experiments.values():
               resource = experiment.resources.get(RESOURCE_LABEL)
               if resource is None:
                   continue

               out_dir = OUTPUT_DIR / subject.label / experiment.label / RESOURCE_LABEL
               print("Downloading resource:", subject.label, experiment.label, RESOURCE_LABEL)
               resource.download_dir(str(out_dir))

For fMRIPrep and TractoFlow, resources can be large. Test with one subject before downloading a full project.

Download One Specific File From Many Sessions
---------------------------------------------

A common request is: "Download every FreeSurfer ``aseg.stats`` file, but not the full fMRIPrep output." The safest approach is:

1. Loop through subjects and sessions.
2. Inspect the resource file listing.
3. Download only files whose path ends with ``stats/aseg.stats``.
4. Save a manifest.

The exact file listing can vary by resource, so inspect the file names before downloading. Many FreeSurfer resources store this file as ``<subject>/stats/aseg.stats``.

.. code-block:: python

   import csv
   import os
   from pathlib import Path
   import xnat

   PROJECT_ID = "your_project_id"
   RESOURCE_LABEL = "freesurfer"
   OUTPUT_DIR = Path("aseg_stats_bids")
   MANIFEST = OUTPUT_DIR / "aseg_stats_manifest.tsv"

   def safe_label(value):
       return "".join(c if c.isalnum() or c in "-_" else "_" for c in str(value))

   with xnat.connect(
       os.environ.get("XNAT_HOST", "https://xnat.abudhabi.nyu.edu"),
       user=os.environ["XNAT_USER"],
       password=os.environ["XNAT_PASS"],
   ) as session:
       project = session.projects[PROJECT_ID]
       MANIFEST.parent.mkdir(parents=True, exist_ok=True)

       with MANIFEST.open("w", newline="", encoding="utf-8") as manifest_file:
           writer = csv.writer(manifest_file, delimiter="\t")
           writer.writerow(["subject", "session", "resource", "xnat_file", "local_path"])

           for subject in project.subjects.values():
               for experiment in subject.experiments.values():
                   if RESOURCE_LABEL not in experiment.resources:
                       continue

                   resource = experiment.resources[RESOURCE_LABEL]
                   for file_key, file_obj in resource.files.items():
                       file_name = str(file_key or file_obj.name).replace("\\\\", "/")
                       if not file_name.endswith("stats/aseg.stats"):
                           continue

                       local_path = (
                           OUTPUT_DIR
                           / "derivatives"
                           / "freesurfer"
                           / safe_label(subject.label)
                           / safe_label(experiment.label)
                           / "stats"
                           / "aseg.stats"
                       )
                       local_path.parent.mkdir(parents=True, exist_ok=True)

                       if local_path.exists():
                           print("Skipping existing:", local_path)
                       else:
                           print("Downloading:", file_name, "->", local_path)
                           file_obj.download(str(local_path))

                       writer.writerow([subject.label, experiment.label, RESOURCE_LABEL, file_name, local_path])

The local output is intentionally BIDS-like:

.. code-block:: text

   aseg_stats_bids/
     derivatives/
       freesurfer/
         Subject_0001/
           ses_01/
             stats/
               aseg.stats
     aseg_stats_manifest.tsv

Parse ``aseg.stats`` Into a CSV
-------------------------------

After downloading ``aseg.stats`` files, you can parse them into a table. This minimal parser extracts ``Volume_mm3`` values by structure name.

.. code-block:: python

   import csv
   from pathlib import Path

   INPUT_DIR = Path("aseg_stats_bids")
   OUTPUT_CSV = Path("aseg_stats_wide.csv")

   def parse_aseg(path):
       measures = {}
       columns = None
       with path.open("r", encoding="utf-8", errors="replace") as f:
           for line in f:
               line = line.strip()
               if line.startswith("# ColHeaders"):
                   columns = line.split()[2:]
                   continue
               if not line or line.startswith("#") or columns is None:
                   continue
               values = line.split()
               row = dict(zip(columns, values))
               name = row.get("StructName")
               volume = row.get("Volume_mm3")
               if name and volume:
                   measures[name] = volume
       return measures

   rows = []
   all_columns = set()

   for stats_path in INPUT_DIR.rglob("aseg.stats"):
       parts = stats_path.parts
       subject = next((p for p in parts if p.startswith("sub-") or p.startswith("Subject_")), "")
       session = next((p for p in parts if p.startswith("ses")), "")
       values = parse_aseg(stats_path)
       values.update({"subject": subject, "session": session, "path": str(stats_path)})
       rows.append(values)
       all_columns.update(values)

   columns = ["subject", "session", "path"] + sorted(c for c in all_columns if c not in {"subject", "session", "path"})
   with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
       writer = csv.DictWriter(f, fieldnames=columns)
       writer.writeheader()
       writer.writerows(rows)

   print("Wrote:", OUTPUT_CSV)

For production analysis, keep the original ``aseg.stats`` files and the manifest alongside the CSV.

Download Directly to Jubail and Run Your Own Processing
-------------------------------------------------------

For larger workflows, use this pattern:

1. Create a script locally and test it on one session.
2. Copy the script to Jubail, or write it directly in your Jubail project folder.
3. Store XNAT credentials in environment variables or a private ``.env`` file.
4. Download data to a project scratch/work directory.
5. Submit downstream processing as a SLURM job.

Example job wrapper:

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=xnat-download-test
   #SBATCH --time=01:00:00
   #SBATCH --cpus-per-task=2
   #SBATCH --mem=8G
   #SBATCH --output=xnat-download-%j.out
   #SBATCH --error=xnat-download-%j.err

   set -euo pipefail

   cd "$HOME/xnat-api-work"
   source xnat-api-env/bin/activate

   # Keep this file private: chmod 600 ~/.xnat.env
   source "$HOME/.xnat.env"

   python 01_test_connection.py
   python download_selected_resources.py

Submit it:

.. code-block:: bash

   sbatch xnat_download_job.sh

Do not print token secrets in job logs. If a script prints its configuration, redact ``XNAT_PASS`` before sharing logs.

Build Scripts With AI Assistance
--------------------------------

AI tools can be helpful for turning a clear download request into a script. They are most useful when you give them:

- The XNAT server URL.
- The project ID.
- The exact subject/session labels you want.
- The resource label, such as ``DICOM``, ``rawdata``, ``fmriprep``, ``mriqc``, ``freesurfer``, or ``tractoflow``.
- The file pattern, such as ``stats/aseg.stats`` or ``*.html``.
- The desired output structure.

Use a prompt like this:

.. code-block:: text

   Write a Python script using the xnat package to connect to XNAT with
   XNAT_HOST, XNAT_USER, and XNAT_PASS from environment variables.
   The script should be read-only. It should not delete, upload, archive,
   overwrite, or modify anything on XNAT.

   Task:
   - Project: <project_id>
   - Subjects: <list or "all">
   - Sessions: <list or "all">
   - Resource: <resource label>
   - File pattern: <for example, stats/aseg.stats>
   - Output directory: <local path>

   Requirements:
   - Do a dry run option first.
   - Skip files that already exist.
   - Write a manifest TSV.
   - Print clear progress messages.
   - Keep token secrets out of the code and logs.

Always review AI-generated scripts before running them. If you are unsure whether a script is safe, send it to admin.nyuad.xnat@nyu.edu and ask for review.

Recommended Script Features
---------------------------

For scripts you plan to reuse, add:

- ``--dry-run`` to list planned downloads without writing files.
- ``--project`` to make the project configurable.
- ``--subject`` and ``--session`` filters.
- ``--resource`` to choose a resource label.
- ``--output-dir`` to choose where files go.
- Existing-file checks to avoid re-downloading.
- A manifest TSV with subject, session, resource, XNAT file name or URI, and local path.
- Logging to a text file.
- A small test mode that stops after the first matching session.

Troubleshooting
---------------

**Authentication fails**
   Confirm that ``XNAT_USER`` is the alias token and ``XNAT_PASS`` is the alias secret. Do not use your Google password.

**Cannot reach XNAT**
   Confirm you are on the NYUAD network or VPN. On Jubail, confirm that the job environment has network access to XNAT.

**Project or subject is missing**
   Check spelling and project access. The API only shows data your account is allowed to see.

**Resource label is missing**
   Open the session in XNAT and check the resource name. Common labels include ``DICOM``, ``rawdata``, ``mriqc``, ``fmriprep``, ``freesurfer``, and ``tractoflow``, but projects can differ.

**Downloads are incomplete**
   Add retry logic, skip existing complete files, and keep a manifest. For large DICOM downloads, consider using the Desktop Client.

**The script works for one subject but fails for a project**
   Add error handling around each subject/session so one bad session does not stop the whole run.

Getting Help
------------

If you need help, email admin.nyuad.xnat@nyu.edu with:

- The project ID.
- The subject/session you tested.
- The resource or file you are trying to download.
- The script or AI prompt you used.
- The error message or log.

Related Documentation
---------------------

- :doc:`browser` - Browser download method
- :doc:`desktop_client` - Desktop Client download method
- :doc:`../working_with_xnat/access` - Alias token creation
- :doc:`../processing_pipelines/fmriprep` - fMRIPrep outputs
- :doc:`../processing_pipelines/mriqc` - MRIQC outputs
- :doc:`../processing_pipelines/tractoflow` - TractoFlow outputs
- `XNAT Python Client documentation <https://xnat.readthedocs.io/en/stable/>`_
- `CRC Jubail documentation <https://crc-docs.abudhabi.nyu.edu/>`_
