Enabling Pipelines for Your Project
===================================

This page explains how to enable processing pipelines for your XNAT project. Pipeline availability depends on project configuration and user permissions.

Pipeline Availability
---------------------

**By Default:**
- New projects have limited pipeline access
- Basic data conversion tools are typically available
- Advanced preprocessing requires explicit activation

**Project-Specific:**
- Some pipelines are enabled per project
- Availability depends on resource allocation
- Custom pipelines may require special setup

Requesting Pipeline Access
--------------------------

**For Standard Pipelines:**

1. **Contact your project administrator** or XNAT support
2. **Specify which pipelines** you need enabled:
   - Data conversion (dcm2niix, dcm2bids, dcm2hcp)
   - Quality control (mriqc, ari-validator)
   - Preprocessing (fmriprep, tractoflow, HCP pipeline)
3. **Provide justification** for computational resource requirements
4. **Review resource limits** and usage policies

**For Custom Pipelines:**

1. **Prepare pipeline specifications**:
   - Docker container requirements
   - Input/output specifications
   - Resource requirements (CPU, memory, storage)
2. **Submit request** through appropriate channels
3. **Coordinate testing** and validation process
4. **Complete deployment** and user training

Administrative Setup
--------------------

**For Project Administrators:**

**1. Access Project Settings**
- Navigate to your project in XNAT
- Select "Project Settings" or "Administration"
- Look for "Pipeline Configuration" section

**2. Enable Pipeline Access**
- Select pipelines from available options
- Configure resource limits and permissions
- Set user access levels

**3. Configure Resources**
- Set compute allocation limits
- Configure storage quotas
- Define notification preferences

**4. Test Configuration**
- Run test jobs with sample data
- Verify output generation and storage
- Check user permissions and access

User Permissions
----------------

**Required Permissions:**
- **Project Member:** Basic access to view and run pipelines
- **Project Collaborator:** Can submit jobs and access results
- **Project Owner:** Full pipeline configuration access

**Permission Levels:**
- **Read-Only:** View pipeline results only
- **Execute:** Run pipelines on existing data
- **Configure:** Modify pipeline parameters and settings
- **Admin:** Full pipeline management access

Resource Considerations
-----------------------

**Computing Resources:**
- **CPU Requirements:** Pipeline-specific processing needs
- **Memory Limits:** RAM requirements for large datasets
- **Storage Space:** Input data, temporary files, and results
- **Time Limits:** Maximum job duration policies

**Cost Implications:**
- **Compute Time:** Charges based on CPU hours used
- **Storage Costs:** Long-term storage of results
- **Network Usage:** Data transfer costs

**Quota Management:**
- **Monthly Limits:** Maximum compute hours per month
- **Concurrent Jobs:** Number of simultaneous pipeline runs
- **Storage Limits:** Maximum data storage per project

Common Issues
-------------

**Pipeline Not Available:**
- Check project settings and permissions
- Verify pipeline is enabled for your project
- Contact administrator for access

**Insufficient Resources:**
- Review resource allocation limits
- Request quota increase if needed
- Optimize pipeline parameters for efficiency

**Permission Denied:**
- Verify user role and permissions
- Check project membership status
- Request appropriate access level

Getting Help
------------

**For Pipeline Requests:**
- Contact your project administrator
- Submit support ticket with specific requirements
- Provide details about computational needs

**For Technical Issues:**
- Check :doc:`../support/troubleshooting` for common problems
- Review :doc:`running_pipelines` for usage instructions
- Contact support with error messages and logs

Next Steps
----------

After enabling pipelines for your project:

1. **Review** :doc:`running_pipelines` for general usage instructions
2. **Explore** specific pipeline documentation in :doc:`../processing_pipelines/overview`
3. **Test** pipeline functionality with sample data
4. **Configure** notifications and output settings
5. **Train** project members on pipeline usage

Related Documentation
---------------------

- :doc:`running_pipelines` - How to run any pipeline
- :doc:`../processing_pipelines/overview` - Available pipelines
- :doc:`project_management` - Project administration
- :doc:`../support/troubleshooting` - Common issues and solutions