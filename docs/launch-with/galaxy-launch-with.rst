Galaxy
======

Dockstore integrates with `Galaxy <https://usegalaxy.org>`__. The Dockstore integration with Galaxy
is invoked from within Galaxy. There is currently no Launch with button in Dockstore for Galaxy. One
will be added in the future.

Importing into Galaxy
---------------------

To import a workflow into Galaxy, navigate to a Galaxy instance in your browser.
There are many Galaxy instances. In the steps here we are going to use
`usegalaxy.org <https://usegalaxy.org>`__. 

Login to Galaxy.

Click the Workflow menu item. You'll end up on a screen that includes an Import button.

.. figure:: /assets/images/docs/galaxy/workflow_import.png
   :alt: Galaxy import workflow

Click the import button. This will take you to a screen that includes a section that lets
you import a workflow from Dockstore.

.. figure:: /assets/images/docs/galaxy/dockstore_import.png
   :alt: Import workflow from Dockstore

You can either click the link to search for a workflow or click the link to import a specific workflow.

Search for a Workflow
---------------------

If you want to search for a Dockstore workflow, click the *search form* link. This takes you to a
form where you can search for Galaxy workflows in Dockstore by the workflows' descriptions. In the 
example below, we are searching for the word *Plink*.

.. figure:: /assets/images/docs/galaxy/search.png

Click on the workflow you want to import. This will show all of the workflow's versions. Click
on the version you want to import.

Import a Known Workflow
-----------------------

If you know the Dockstore workflow you want to import, click *import from a TRS id*. This takes to
a form where you can enter the TRS ID of the Dockstore workflow. After you enter the TRS id, you 
will be prompted to select which version of the workflow to import.

.. tip:: If you are viewing a Galaxy workflow in Dockstore and want to copy its TRS ID, click
    the *Copy TRS ID* icon in Dockstore. This will put the TRS ID in your clipboard, which
    you can paste if you select *import from a TRS id*

.. figure:: /assets/images/docs/galaxy/copy_trs.png
