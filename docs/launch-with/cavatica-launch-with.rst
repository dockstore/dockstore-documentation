Cavatica
========

Dockstore integrates with `Cavatica <https://cavatica.sbgenomics.com>`__
platform, allowing you to launch CWL-based workflows from Dockstore in the Cavatica. Here is
some information on what that looks like from a user point of view in a mini tutorial.


Exporting into Cavatica
-----------------------

When browsing CWL workflows from within Dockstore, you will see a
"Launch with Cavatica" button on the right. The currently selected version
of the workflow will be exported.

.. figure:: /assets/images/docs/sevenbridges/sb_from_dockstore.png
   :alt: CWL workflow

   CWL workflow

If not logged into the Cavatica, you will be prompted to login.

You will then be prompted to import the workflow into Cavatica. Please follow the Cavatica UI
prompts to import the workflow into Cavatica.

.. _cavatica-limitations:

Limitations
-----------

1. While we support launching of CWL workflows, tools as listed in
   Dockstore are currently not supported.
2. The CGC does not currently support http(s) based imports in CWL. Dockstore
   disables the Launch with CGC button if the selected version has any http(s) imports.
3. Only the CWL language is supported.

.. discourse::
    :topic_identifier: 4188

