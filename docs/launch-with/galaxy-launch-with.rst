######
Galaxy
######

Dockstore integrates with the `Galaxy Application <https://usegalaxy.org>`__, allowing you to launch Galaxy-based workflows from Dockstore into
any Galaxy instance. This works both from within the Dockstore interface and from within the Galaxy interface.
There are several ways to launch Galaxy-based workflows. Here is some information on what that looks like from a user point of view in a mini tutorial.

While browsing Dockstore
========================

Dockstore has a fully featured faceted search to effectively search for workflows. On the left panel, you can choose from several options to narrow down your search. Searching for workflows can be done using a specific search term. Results can be narrowed down based on the language of the workflow, author, organization, source control used among others.

Once you have clicked on a Galaxy workflow, you will see a Launch with Galaxy button on the right.

.. figure:: /assets/images/docs/galaxy/galaxy_workflow.png
   :alt: Galaxy workflow on Dockstore

Launching a workflow on an existing Galaxy server
-------------------------------------------------

The button will bring up a dropdown window where you may select which Galaxy instance to launch the workflow into. A few default options such as the `usegalaxy.org <https://usegalaxy.org/>`__ instances are provided by Dockstore, but if you need to launch into another instance, you may provide a custom URL. Further along in this tutorial, you will find how to generate a custom instance and provide the URL to Dockstore.

.. figure:: /assets/images/docs/galaxy/launch_with_options.png
   :alt: Launch options for Galaxy

Launching a workflow on a custom Galaxy instance on the cloud
-------------------------------------------------------------

You can use Terra to spin up a custom cloud environment for Galaxy. Terra has integrated Galaxy making it possible for users to spin up a custom Galaxy server backed by a cloud environment and dedicated resources. This feature is available on all "faces" of Terra, such as AnVIL and NHLBI BioData Catalyst. Apart from providing a rapid and customizable Galaxy cloud instance, Terra is able to access a rich data corpus hosted in the cloud, including many controlled-access datasets facilitating the user to securely carry out analyses using this data.

To spin up a custom cloud environment on Terra, navigate to the Notebooks tab on any Workspace on `Terra <https://app.terra.bio/>`__ and click on the "Create a Cloud Environment for Galaxy" on the left.

.. figure:: /assets/images/docs/galaxy/create_galaxy_environment.png
   :alt: Create a Cloud Environment for Galaxy

It takes 8-10 minutes for the cloud environment to launch. Once it is ready, you can click on the Galaxy button on the top right and then the Launch Galaxy button. Doing so will open the Galaxy page with a custom cloud environment. You can copy the URL and paste it into the Dockstore dropdown window to launch a workflow from Dockstore into this cloud instance. For your custom URL to work properly, it must start with ``https://`` and end with ``/galaxy``.

While browsing Galaxy
=====================

To import a workflow from Dockstore from the Galaxy interface, navigate to a Galaxy instance in your browser.
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

Use the search form
-------------------

If you want to search for a Dockstore workflow, click the *search form* link. This takes you to a
form where you can search for Galaxy workflows in Dockstore by the workflows' descriptions. In the 
example below, we are searching for the word *Plink*.

.. figure:: /assets/images/docs/galaxy/search.png

Click on the workflow you want to import. This will show all of the workflow's versions. Click
on the version you want to import.

Import from a TRS ID
---------------------

If you have already found a workflow on Dockstore that you would like to launch, click on the copy symbol next to the TRS in the Workflow Description box. This will copy the TRS ID to your clipboard.

.. figure:: /assets/images/docs/galaxy/copy_TRS_ID.png
   :alt: Copy TRS ID

Then you can navigate back to the import option on Galaxy and paste it in the text box below TRS ID. This will show all of the workflow's versions. Click on the version you want to import.

.. figure:: /assets/images/docs/galaxy/paste_TRS_ID.png
   :alt: Paste TRS ID

.. discourse::
    :topic_identifier: 4189

