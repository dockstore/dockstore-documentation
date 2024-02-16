Installing the GitHub App is simple. Navigate to ``/my-tools``, ``/my-workflows``, ``/my-notebooks``, or ``/my-services`` by navigating to My Dashboard then selecting the desired option in the left sidebar. In these screenshots, we will go via ``/my-tools``, but the process is essentially the same for any of the other options.

.. image:: /assets/images/docs/my-dashboard-sidebar.png  

|

Click the ``Register a Tool`` button on the left hand sidebar.

.. image:: /assets/images/docs/add-tool-button.png
   :width: 30 %

|

A window will appear asking how you would like to register your tool, workflow, or service. Select ``Register using GitHub Apps``.

.. image:: /assets/images/docs/register-tool-github-apps.png
   :width: 50 %

Click ``+ Manage Dockstore Installations on GitHub``.

.. image:: /assets/images/docs/manage-gh-app-installation.png
   :width: 50 %

You'll then be redirected to GitHub where you can install the app in an organization or your personal account. For example, the username for my personal GitHub account is aofarrel. If I want to install the GitHub App so it could access aofarrel/mycoolrepo, I would choose the first option here.

.. figure:: /assets/images/docs/gh-app-install-where.png
   :width: 65 %

   Install our GitHub App in an organization or your personal account

After selection of an organization or a personal account, you can select whether to give access to all current and future repositories or only select ones. If the organization or personal account you choose is intended to be just for Dockstore tools/workflows/services/notebooks, you may want to allow access to all repositories. Otherwise, it may be more intuitive to select only certain repositories. Click save and you will be taken back to Dockstore.

.. important:: The GitHub user who first adds a workflow onto Dockstore must correspond to a user on Dockstore.

On Dockstore, under the GITHUB section, you should see the names of GitHub accounts that you have access to, such as organizations that you belong to and your personal account. If your repositories that you chose to keep track of contained a .dockstore.yml at the time of installing the GitHub App, then you will see the repositories under the GitHub personal/organization account name that it belongs to. Here's an example involving ``/my-services``:

.. figure:: /assets/images/docs/my-services-filled.png


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

Upon installing the GitHub App, Dockstore will find branches in your repository that contain a .dockstore.yml and attempt to register your workflows, tools, services, and notebooks. There may be some cases where Dockstore is unable to find all branches containing a .dockstore.yml, for example, if the GitHub repository has many branches.

If your workflow, tool, service, or notebook is not showing up on Dockstore after 5 minutes, push one *additional* commit to the branch in your repository that contains the .dockstore.yml that's not being synchronized. Dockstore will synchronize the branch that was updated, which helps make sure that your workflows, tools, services, and notebooks show up in Dockstore.

If your workflow, tool, service, or notebook still doesn't show up, check the :ref:`GitHub App logs <GitHub App logs FAQ>` to see if Dockstore encountered an error while processing your .dockstore.yml.
