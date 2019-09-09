Cancer Genomics Cloud Launch-With
=================================

Dockstore integrates with the `Cancer Genomics Cloud <https://cgc.sbgenomics.com>`__ (CGC)
platform, allowing you to launch CWL-based workflows from Dockstore in the CGC. Here is
some information on what that looks like from a user point of view in a mini tutorial.

Exporting into CGC
------------------

When browsing CWL workflows from within Dockstore, you will see a
"Launch with CGC" button on the right. The currently selected version
of the workflow will be exported.

.. figure:: /assets/images/docs/cgc/cgc_from_dockstore.png
   :alt: CWL workflow

   CWL workflow

If not logged into the CGC, you will be prompted to login. Otherwise, or
after login, you will be presented with the following screen.

.. figure:: /assets/images/docs/cgc/cgc_from_dockstore2.png
   :alt: CWL workflow import

   CWL workflow import

You will need to pick a project to export it into. The project
must already exist.

Then hit the "Import" button and continue from within the CGC
interface to configure and run your workflow.


Limitations
-----------

1. While we support launching of CWL workflows, tools as listed in
   Dockstore are currently not supported.
2. The CGC does not currently support http(s) based imports in CWL. Dockstore
   disables the Launch with CGC button if the selected version has any http(s) imports.
3. Only the CWL language is supported.

See Also
--------

-  `AWS Batch <../advanced-topics/aws-batch/>`__
-  `Azure Batch <../advanced-topics/azure-batch/>`__
-  `DNAnexus Launch With <../end-user-topics/dnanexus-launch-with/>`__
-  `DNAstack Launch With <../end-user-topics/dnastack-launch-with/>`__
-  `Terra Launch With <../end-user-topics/terra-launch-with/>`__

.. discourse::
    :topic_identifier: 2006

