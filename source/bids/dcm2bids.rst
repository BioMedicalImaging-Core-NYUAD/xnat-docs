BIDS Usage on XNAT
==================

This page outlines how the Brain Imaging Data Structure (BIDS) is used by XNAT. 

   
Running dcm2bids
-------------------
* On the session page, navigate to Actions → Run preprocessing pipeline, and run dcm2bids

.. image:: ../_static/run_dcm2bids.png

|
* The "dcm2bids" pipeline will perform BIDS conversion *and* BIDS validation

|
Viewing BIDS Output
-------------------
* To view BIDS output, navigate to Manage Files → resources → BIDS, and expand to view the contents
* To view the validator output,  scroll down to the “Historyˮ window and click on the StdOut.log associated with the "bids-validator - session" activity:

|
Adding & Modifying a BIDS config.json file
------------------------------------------

The following instructions go through the steps needed to add and download a BIDS config.json file to a project. The config file is the responsibility of the project owner. If you do not have a BIDS config.json file, you can find a sample here:

   :download:`Download JSON file <_static/config.json>`


New Project
^^^^^^^^^^^
1. XNAT requires a folder to upload your config files to. This only needs to be done once when a new project is created on XNAT
2. Navigate to your project page, and select “Manage Files”

3. Click on “Add Folder”

4. Select “resources” from the “Level” drop-down menu

5. Name the folder and click “Create”. This will be the location of your BIDS config.json file

Uploading a config.json file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Click on “Upload Files”

2. Select “resources” from the “Level” drop-down menu, and then the folder you wish to upload the config file to

3. Click on “Choose File”, select you config file, and then hit “Upload”

Your config file has now been uploaded! dcm2bids will now use your config file to perform BIDS conversions for this project

**Notes**
1. If you want to download the config file on XNAT, simply click on the config.json and the download will begin
2. To upload a new config file, delete the old config file and upload the new one using the same instructions above



**add a sample config file**

