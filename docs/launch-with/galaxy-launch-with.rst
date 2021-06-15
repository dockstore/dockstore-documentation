######
Galaxy
######

Dockstore integrates with the `Galaxy Application <https://usegalaxy.org>`__, allowing you to launch Galaxy-based workflows from Dockstore into
any Galaxy instance. This works both from within the Dockstore interface and from within the Galaxy interface.
Here is some information on what that looks like from a user point of view in a mini tutorial.

While browsing Dockstore
========================
When browsing Galaxy workflows from within Dockstore, you will see a
Launch with Galaxy button on the right.

.. figure:: /assets/images/docs/galaxy/galaxy_workflow.png
   :alt: Galaxy workflow on Dockstore

The button will bring up a dropdown window where you may select which Galaxy instance to launch the workflow into. A few default options will
be provided by Dockstore, but if you need to launch into another instance, you may provide a custom URL. For your custom URL to work properly,
it must start with ``https://`` and there should not be an ending forward slash ``/``.

.. figure:: /assets/images/docs/galaxy/launch_with_options.png
   :alt: Launch options for Galaxy


While browsing Galaxy
=====================

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


.. discourse::
    :topic_identifier: 4189

