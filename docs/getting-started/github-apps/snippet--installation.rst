Installing the GitHub App is simple. Navigate to ``/my-tools``, ``/my-workflows``, or ``/my-services`` by navigating to My Dashboard then selecting the desired option in the left sidebar. In these screenshots, we will go via ``/my-tools``, but the process is essentially the same for any of the other options.

.. note:: Since Dockstore Notebooks is still in beta mode, it does not have a dedicated ``/my-notebooks`` page yet. To register a notebook, navigate to ``/my-workflows`` in the step above. 

.. image:: /assets/images/docs/my-dashboard-sidebar.png

Click the ``Register a Tool`` button on the left hand sidebar.

.. image:: /assets/images/docs/add-tool-button.png
   :width: 30 %

A window will appear asking how you would like to register your tool, workflow, or service. Select ``Register using GitHub Apps``.

.. image:: /assets/images/docs/register-tool-github-apps.png
   :width: 50 %

Click ``+ Manage Dockstore Installation on GitHub``. You'll then be redirected to GitHub where you can select which repositories can be accessed by the GitHub app.

.. image:: /assets/images/docs/manage-gh-app-installation.png
   :width: 50 %

You'll then be redirected to GitHub where you can grant the app access to specific repositories within whatever organization you are installing into. Note that GitHub treats your username as its own "organization." For instance, my GitHub username is aofarrel. If I want to install the GitHub App so it could access aofarrel/mycoolrepo, I would choose the first option here.

.. figure:: /assets/images/docs/gh-app-install-where.png
   :width: 65 %

   Install our GitHub App on either all current and future repositories in an organization or on specific repositories

After selection of an organization, you can select whether to give access to all current and future repositories or only select ones. If the organization you choose is intended to be just for Dockstore tools/workflows/services/notebooks, you may want to allow access to all repositories. Otherwise, it is may be more intuitive to select only certain repositories. Click save and you will be taken back to the page you started on in Dockstore -- either  ``/my-tools``, ``/my-workflows``, or ``/my-services``, depending where you started.

.. important:: The GitHub user who first adds a workflow onto Dockstore must correspond to a user on Dockstore.

You should now see the organization and the repositories you chose to keep track of in the "unpublished" tab. Here's an example involving ``/my-services``:

.. figure:: /assets/images/docs/my-services-filled.png

.. note:: You will not see unpublished notebooks because there is not a dedicated ``/my-notebooks`` page yet. To view your notebook, which should've been configured to automatically publish on Dockstore via the .dockstore.yml, navigate to ``/notebooks``
   and locate your notebook in the list of published notebooks.
   
   .. image:: /assets/images/docs/list-published-notebooks.png


A note on permissions when installing the Dockstore GitHub App to a GitHub organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only organization admins and repository admins can install the Dockstore GitHub App. 

Organization admins will have the easiest time installing the Dockstore GitHub App because they can install it to any repository in the organization on the installation page. Users who are not organization admins can only install the Dockstore GitHub App on repositories that they are an admin of.

For more information on troubleshooting GitHub App permissions, please see :ref:`this FAQ entry <GitHub App permissions FAQ>`.

.. seealso::
    - :doc:`Automatic Syncing with GitHub Apps and .dockstore.yml </getting-started/github-apps/github-apps/>` - details on writing a .dockstore.yml file
    - :doc:`Migrating Your Existing Workflows </getting-started/github-apps/migrating-workflows-to-github-apps>` - a tutorial on converting already registered workflows
    - :doc:`Troubleshooting and FAQ </getting-started/github-apps/github-apps-troubleshooting-tips>` - tips on resolving Dockstore Github App issues.

Ensuring sychronization
~~~~~~~~~~~~~~~~~~~~~~~

Upon installing the GitHub App, Dockstore will find branches in your repository that contain a .dockstore.yml and attempt to register your workflows, tools, services, or notebooks. There may be some cases where Dockstore is unable to find all branches containing a .dockstore.yml, for example, if the GitHub repository has many branches.

If your workflow, tool, service, or notebook is not showing up on Dockstore after 5 minutes, push one *additional* commit to your repository. This helps make sure your workflows, tools, and services show up in Dockstore.

