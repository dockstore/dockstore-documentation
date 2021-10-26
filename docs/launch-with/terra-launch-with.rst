Terra
=====

Dockstore integrates with the Terra platform, allowing you to launch
WDL-based workflows from Dockstore in Terra. Here is some information on
what that looks like from a user point of view in a mini tutorial.

Exporting into Terra
--------------------

When browsing WDL workflows from within Dockstore, you will see a
"Launch with Terra" button on the right. The currently selected version
of the workflow will be exported.

.. figure:: /assets/images/docs/wdl_launch_with.png
   :alt: WDL workflow

   WDL workflow

If not logged into Terra, you will be prompted to login. Otherwise, or
after login, you will be presented with the following screen.

.. figure:: /assets/images/docs/terra/terra_from_dockstore2.png
   :alt: WDL workflow import

   WDL workflow import

You will need to pick a workspace to export it into. You can either
select an existing workspace or create a new one.

Then hit the "Import" button and continue from within the Terra
interface to configure and run your workflow.

Note that you may want to double-check that the workflow specifies a
runtime environment (docker, cpu, memory, and disks) to avoid using
limiting defaults on Terra. See more
`here <https://cromwell.readthedocs.io/en/stable/wf_options/Overview>`__.

.. tip:: Upload your test parameter files
    Test parameter files are not included in the launch-with service.
    After a workflow launch is complete, users can download parameter files from
    Dockstore and upload them into their Terra workspace that contains the workflow.
    To download a test parameter file from Dockstore, select the Files tab of the
    workflow version, then select Test Parameter Files, select the file you want,
    then click the download button. Use the Terra UI to upload the file to Terra.

 .. figure:: /assets/images/docs/download-test-parameter.png
    :alt: Download test parameter file

.. _terra-limitations:

Limitations
-----------

1. While we support launching of WDL workflows, tools as listed in
   Dockstore are currently not supported.
2. Terra only supports file-path based imports for GitHub-based workflows. The
   Launch-with Terra button is disabled if the selected workflow version
   has more than one descriptor file and is not GitHub-based.
3. Only the WDL language is supported.

See Also
--------

-  :doc:`AWS Batch <../advanced-topics/aws-batch/>`
-  :doc:`Azure Batch <../advanced-topics/azure-batch/>`
-  :doc:`DNAnexus Launch With <../launch-with/dnanexus-launch-with/>`
-  :doc:`DNAstack Launch With <../launch-with/dnastack-launch-with/>`

.. discourse::
    :topic_identifier: 1841
