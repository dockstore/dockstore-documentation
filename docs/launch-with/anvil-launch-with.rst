AnVIL
=====

    For Dockstore 1.8.0+

Dockstore integrates with the `Analysis, Visualization, and Informatics Lab-space (AnVIL) <https://www.genome.gov/Funded-Programs-Projects/Computational-Genomics-and-Data-Science-Program/Genomic-Analysis-Visualization-Informatics-Lab-space-AnVIL>`__ platform,
allowing you to launch WDL-based workflows from Dockstore in AnVIL. Here is some information on
what that looks like from a user point of view in a mini-tutorial.

Exporting into AnVIL
--------------------

When browsing WDL workflows from within Dockstore, you will see a
"Launch with AnVIL" button on the right. The currently selected version
of the workflow will be exported.

.. figure:: /assets/images/docs/wdl_launch_with.png
   :alt: WDL workflow

   WDL workflow

If not logged into AnVIL, you will be prompted to login. Otherwise, or
after login, you will be presented with the following screen.

.. figure:: /assets/images/docs/anvil/anvil_from_dockstore.jpg
   :alt: WDL workflow import

   WDL workflow import

You will need to pick a workspace to export it into. You can either
select an existing workspace or create a new one.

Then hit the "Import" button and continue from within the Terra
interface to configure and run your workflow.

Note that you may want to double-check that the workflow specifies a
runtime environment (docker, cpu, memory, and disks) to avoid using
limiting defaults on AnVIL. See more
`here <https://cromwell.readthedocs.io/en/stable/wf_options/Overview>`__.

.. tip:: Upload your test parameter files
    Test parameter files are not included in the launch-with service.
    After a workflow launch is complete, users can download parameter files from
    Dockstore and upload them into their AnVIL workspace that contains the workflow.
    To download a test parameter file from Dockstore, select the Files tab of the
    workflow version, then select Test Parameter Files, select the file you want,
    then click the download button. Use the AnVIL UI to upload the file to AnVIL.

 .. figure:: /assets/images/docs/download-test-parameter.png
    :alt: Download test parameter file

.. _anvil-limitations:

Limitations
-----------

1. While we support launching of WDL workflows, tools as listed in
   Dockstore are currently not supported.
2. AnVIL only supports file-path based imports for GitHub-based workflows. The
   Launch-with AnVIL button is disabled if the selected workflow version
   has more than one descriptor file and is not GitHub-based.
3. Only the WDL language is supported.

See Also
--------

-  :doc:`CGC Launch With <../launch-with/cgc-launch-with/>`
-  :doc:`DNAnexus Launch With <../launch-with/dnanexus-launch-with/>`
-  :doc:`DNAstack Launch With <../launch-with/dnastack-launch-with/>`
-  :doc:`Terra Launch With <../launch-with/terra-launch-with/>`

.. discourse::
    :topic_identifier: 3323

