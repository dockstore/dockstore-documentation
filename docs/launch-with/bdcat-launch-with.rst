BioData Catalyst
================

Dockstore integrates with the `NHLBI BioData Catalyst <https://dockstore.org/organizations/bdcatalyst>`__ platform. You can
launch both CWL-based and WDL-based workflows from Dockstore in BioData Catalyst.

When browsing WDL and CWL workflows from with Dockstore, you will see a
"Launch with NHLBI BioData Catalyst" button on the right.

When you click the button, you will get redirected to different platform within BioData Catalyst depending
on whether you are on a WDL or a CWL workflow.

If you are not logged into BioData Catalyst, you will be prompted to log in.

You will then be prompted to import the workflow into BioData Catalyst. Please follow the BioData Catalyst UI
prompts to import the workflow into BioData Catalyst.


WDL Workflow with BioData Catalyst button
-----------------------------------------

.. figure:: /assets/images/docs/wdl_launch_with.png
   :alt: WDL workflow

CWL Workflow with BioData Catalyst button
-----------------------------------------
.. figure:: /assets/images/docs/sevenbridges/sb_from_dockstore.png
   :alt: CWL workflow

   CWL workflow

.. tip:: Upload your test parameter files
    Test parameter files are not included in the launch-with service.
    For WDL workflows, after a workflow launch is complete, users can download parameter files from
    Dockstore and upload them into their BioData Catalyst workspace that contains the workflow.
    To download a test parameter file from Dockstore, select the Files tab of the
    workflow version, then select Test Parameter Files, select the file you want,
    then click the download button. Use the BioData Catalyst UI to upload the file to BioData Catalyst.

 .. figure:: /assets/images/docs/download-test-parameter.png
    :alt: Download test parameter file

.. _bdcat-limitations:

Limitations
-----------

1. Only workflows can be exported; Dockstore Tools are not supported.
2. For CWL workflows, NHLBI BioData Catalyst does not currently 
   support http(s) based imports. Dockstore disables the Launch
   with NHLBI BioData Catalyst button if the selected version has
   any http(s) imports.
3. For WDL workflows, NHLBI BioData Catalyst only supports file-path based imports for GitHub-based workflows. The
   Launch-with NHLBI BioData Catalyst button is disabled if the selected WDL workflow version
   has more than one descriptor file and is not GitHub-based.

.. discourse::
    :topic_identifier: 4190

