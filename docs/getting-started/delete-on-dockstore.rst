Deleting an entry on Dockstore
============================

Tutorial Goals
--------------

-  Deleting an entry
-  Uninstalling the Dockstore GitHub App from the source GitHub repo

This tutorial walks through the process of deleting entries from Dockstore.
This action is permanent and after you delete the workflow, it will no longer appear on Dockstore.

Requirements for Deletion
-------------------------

An entry can only be deleted if it satisfies all the following:

-  Has never been published,
-  Was created on/after April 1, 2022, and
-  Is not a checked or checker workflow.


Deleting an Entry
------------------

Navigate to ``/my-tools``, ``/my-workflows``, ``/my-notebooks``, or ``/my-services`` by going to My Dashboard then selecting the desired option in the left sidebar.
In the sidebar accordion, find the github repository that your entry is in and click the entry you would like to delete.

.. image:: /assets/images/docs/sidebar-accordian-notebook-select.png
   :width: 50 %

You should now see your entry with the Delete button on the far right of the page. Click the Delete button.

.. image:: /assets/images/docs/notebook-showing-delete-button.png
   :width: 50 %

Read the dialog message and if you are sure you would like to delete, click the Delete this workflow/tool/notebook/service button

.. image:: /assets/images/docs/delete-notebook-dialog.png
   :width: 50 %

After you delete the entry, you must uninstall the Dockstore GitHub App from the source GitHub repo, or edit/remove the .dockstore.yml file so that it no longer describes the deleted entry.
If you do not, your deleted entry may reappear on Dockstore the next time you push to the repo.

