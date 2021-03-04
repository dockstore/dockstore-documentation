BioData Catalyst
================

Dockstore integrates with the `NHLBI BioData Catalyst <https://biodatacatalyst.nhlbi.nih.gov/>`__ platform. You can
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

Limitations
-----------

1. Only workflows can be exported; Dockstore Tools are not supported.
2. For CWL workflows, NHLBI BioData Catalyst does not currently 
   support http(s) based imports. Dockstore disables the Launch
   with NHLBI BioData Catalyst button if the selected version has
   any http(s) imports.
