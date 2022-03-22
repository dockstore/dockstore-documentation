Services
========

.. note:: Dockstore Services is currently in beta mode. Also note that the screenshots below were taken on our staging site.

Tutorial Goals
--------------

- Get familiarized with the concept of services on Dockstore
- Learn the basics of creating a service using a ``.dockstore.yml`` file
- Learn how to register a service and create versions for it
- Publish your service to Dockstore

.. David will add context here.

Services are meant to be long running processes, usually web services or interactive applications, that can be launched by a user. The entire process for creating a service that can launch successfully is complex and dependent on the service or application you are trying to describe; so it is beyond the scope of this tutorial.
However, this document will outline what is needed to register, update, and publish a service onto Dockstore. Also, please keep in mind that service functionality is currently in beta mode.

Create Your Service
-------------------

The first step is to create a file named ``.dockstore.yml``. The ``.dockstore.yml``  is a configuration file used to describe your service. Technically, having a valid YAML and the right version is
all that is required for your service to appear on Dockstore. But, we will briefly cover an example ``.dockstore.yml`` written for the Xena Hub to show what will generally be needed to create a working service.
You can also view template ``.dockstore.yml`` files :doc:`here </assets/templates/services/services>`.

.. figure:: /assets/images/docs/service-example-1.2.png

Line 1 specifies the ``.dockstore.yml`` version. The latest version you should use is 1.2.

Next is a required key named ``service`` where your service description will lie.

Within this, you should specify the type which can be DOCKER_COMPOSE, KUBERNETES, HELM, SWARM, NOT_APPLICABLE.

Following lines 4-9, it is good practice to include the name, author, and a description of your service.

Next, is the files key. Here you can specify a list of other files (like scripts, READmes, and test parameter files) for Dockstore to index that are contained in your repository and are needed for your service.

Following that is a scripts section. Here you denote the script files or commands to be used for steps like starting, provisioning, specifying the port, and stopping for your service. Other possible keys not listed above include preprovision, prestart, and healthcheck.

Next is a section where you can list any environment variables a service needs to be passed into its scripts by the launcher. In this example, we provide a default HTTP port.

Finally, if your service needs to have data provisioned locally, you should include a data section in your ``.dockstore.yml``.


Registering Your Service
------------------------
Registering your service works differently than tools and workflows on Dockstore. For services, you need to install our Dockstore GitHub application into at least one of your organizations.
By doing so, Dockstore will automatically register the services you create by keeping track of the releases and pre-releases you make on GitHub. This makes getting your service registered to Dockstore easy!
You do not need the service to be fully working, and you can start experimenting on Dockstore while you write it. The following steps walk you through the installation process.

.. include:: /getting-started/github-apps/vocabulary-note.rst

Install the Dockstore GitHub App
--------------------------------
.. include:: /getting-started/github-apps/installation.rst


Publishing Your Service
-----------------------
When you select a repository from this panel to view, you will notice that information is missing. Clicking the Versions tab, you will see an info box letting you know that this service does not have any versions. When your service is in this state, the publish button is disabled.

To add a version, get the information to populate, and gain the ability to publish, all you need to do is create a release or prerelease on GitHub on a repository that has a valid ``.dockstore.yml`` located in its root directory. Any time this is done, Dockstore will automatically create versions for you.

.. figure:: /assets/images/docs/services-versions-tab.png

Now the Files tab will have your ``.dockstore.yml`` under the Primary Descriptor. Additionally, the files you choose to list in the in the files section of the ``.dockstore.yml`` will also be visible in the Files tab.

Once you have a version, you can now publish your service! Publishing will create a public page that is very similar to the ones we have for tools and workflows.

.. figure:: /assets/images/docs/services-public-page.png

Now other users can view and :doc:`star <../end-user-topics/starring>` your service. You will also have the option to add published services to a :doc:`collection <../advanced-topics/organizations-and-collections>`.


.. discourse::
    :topic_identifier: 1970