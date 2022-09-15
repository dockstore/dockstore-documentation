Installing the GitHub App is simple. Navigate to ``/my-tools``, ``/my-workflows``, or ``/my-services`` using the drop down menu in the top right. In these screenshots, we will go via ``/my-tools``, but the process is essentially the same for any of the other options.

.. image:: /assets/images/docs/my-tools.png

Click the ``+`` button on the left hand sidebar.

.. image:: /assets/images/docs/add-tool-button.png
   :width: 40 %

A window will appear asking how you would like to register your tool, workflow, or service. Select ``Register using GitHub Apps``.

.. image:: /assets/images/docs/register-tool-github-apps.png
   :width: 50 %

Click ``+ Manage Dockstore Installation on GitHub``. You'll then be redirected to GitHub where you can select which repositories can be accessed by the GitHub app.

.. image:: /assets/images/docs/manage-gh-app-installation.png
   :width: 50 %

You'll then be redirected to GitHub where you can grant the app access to specific repositories within whatever organization you are installing into. Note that GitHub treats your username as its own "organization." For instance, my GitHub username is aofarrel. If I want to install the GitHub App so it could access aofarrel/mycoolrepo, I would choose the first option here.

.. figure:: /assets/images/docs/gh-app-install-where.png
   :width: 65 %

   Install our GitHub App on either all repositories in an organization or on specific repositories

After selection of an organization, you can select whether to give access to all repositories or only select ones. If the organization you choose is intended to be just for Dockstore tools/workflows/services, you may want to allow access to all repositories. Otherwise, it is may be more intuitive to select only certain repositories. Click save and you will be taken back to the page you started on in Dockstore -- either  ``/my-tools``, ``/my-workflows``, or ``/my-services``, depending where you started.

.. important:: The GitHub user who first adds a workflow onto Dockstore must correspond to a user on Dockstore.

You should now see the organization and the repositories you chose to keep track of in the "unpublished" tab. Here's an example involving ``/my-services``:

.. figure:: /assets/images/docs/my-services-filled.png


A note on permissions when installing the Dockstore GitHub App to a GitHub organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only organization admins and repository admins can install the Dockstore GitHub App. Organization admins will have the easiest time installing the Dockstore GitHub App because they can install it to any repository in the organization on the installation page.

Users who are not organization admins can only install the Dockstore GitHub App on repositories that they are an admin of.

For more information on troubleshooting GitHub App permissions, please see :ref:`this FAQ entry <GitHub App permissions FAQ>`.

.. seealso::
    - :doc:`Automatic Syncing with GitHub Apps and .dockstore.yml </getting-started/github-apps/github-apps/>` - details on writing a .dockstore.yml file
    - :doc:`Migrating Your Existing Workflows </getting-started/github-apps/migrating-workflows-to-github-apps>` - a tutorial on converting already registered workflows
    - :doc:`Troubleshooting and FAQ </getting-started/github-apps/github-apps-troubleshooting-tips>` - tips on resolving Dockstore Github App issues.

Ensuring sychronization
~~~~~~~~~~~~~~~~~~~~~~~

Once the GitHub App is installed and a .dockstore.yml is present, please make sure to push one *additional* commit to your repository. This helps make sure your workflows, tools, and services show up in Dockstore.

