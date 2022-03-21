====================================
Installing the Dockstore GitHub App
====================================

Installing the GitHub App is simple. Navigate to ``/my-tools``, ``/my-workflows``, or ``/my-services`` using the drop down menu in the top right.

.. image:: /assets/images/docs/my-tools.png

Click the ``+`` button on the left hand sidebar.

.. image:: /assets/images/docs/add-tool-button.png
   :width: 40 %


Select ``Register using GitHub Apps``.

.. image:: /assets/images/docs/register-tool-github-apps.png
   :width: 40 %

Click ``+ Manage Dockstore Installation on GitHub``. You'll then be redirected to GitHub where you can select which repositories can be accessed by the GitHub app.

.. image:: /assets/images/docs/manage-gh-app-installation.png
   :width: 40 %

You'll then be redirected to GitHub where you can grant the app access to specific repositories within whatever organization you are installing into. Note that GitHub treats your username as its own "organization." For instance, my GitHub username is aofarrel. If I want to install the GitHub App so it could access aofarrel/mycoolrepo, I would choose the first option here.

.. figure:: /assets/images/docs/gh-app-install-where.png
   :width: 40 %

   Install our GitHub App on either all repositories in an organization or on specific repositories

.. important:: The GitHub user who first adds a workflow onto Dockstore must correspond to a user on Dockstore.

You can also begin the installation via ``/my-workflows`` too.

.. image:: /assets/images/docs/add-workflow-button.png
   :width: 30 %

.. image:: /assets/images/docs/register-workflow-github-apps.png
   :width: 30 %

.. figure:: /assets/images/docs/gh-app-reg-1.png
   :width: 40 %

A note on permissions
~~~~~~~~~~~~~~~~~~~~~

If you are adding the GitHub App to an organization for which you are not an admin, GitHub may block your ability to install the app, even if you have maintainer access to the repository you are hoping to give the GitHub App permission to view. Please see :ref:`this FAQ entry <GitHub App permissions FAQ>` for more information.

.. seealso::
    - :doc:`Automatic Syncing with GitHub Apps and .dockstore.yml </getting-started/github-apps/github-apps/>` - details on writing a .dockstore.yml file
    - :doc:`Migrating Your Existing Workflows </getting-started/github-apps/migrating-workflows-to-github-apps>` - a tutorial on converting already registered workflows
    - :doc:`Troubleshooting and FAQ </getting-started/github-apps/github-apps-troubleshooting-tips>` - tips on resolving Dockstore Github App issues.