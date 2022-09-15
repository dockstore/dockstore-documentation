=================================
GitHub App Troubleshooting & FAQs
=================================

..
    Need to update with info about checking lambda errors in UI https://github.com/dockstore/dockstore/issues/3530

.. contents::
   :local:
   :depth: 2

Why should I migrate my existing workflows to use GitHub Apps and a .dockstore.yml?
----------------------------------------------------------------------------------------
Installing our Dockstore GitHub App onto your GitHub repository or organization will automatically sync your workflow/tool on Dockstore whenever code is pushed to GitHub.
This means less manual work for workflow developers, and less waiting for content to update.

This requires the addition of a .dockstore.yml file to your repository on GitHub.
This file contains information that Dockstore will use to setup
the corresponding workflow/tool entry on Dockstore. Branches that do not have a .dockstore.yml file, or that are filtered out via the filter feature, will not be synchronized.

You can read more about it at :doc:`/getting-started/github-apps/github-apps`.

How does this change my development flow?
-------------------------------------------
Adding a .dockstore.yml file to a template branch (ex: master, develop, main) will make it so
any new branches created from this template will be automatically added to and synced on Dockstore.

Therefore, as long as your workflow is already registered on Dockstore and your .dockstore.yml is configured correctly, updates to the workflow (including adding new versions) should happen continuously and automatically.

You can use filters in a .dockstore.yml to avoid generating a corresponding workflow-version on Dockstore.

*Note:* If you want to edit version information, such as workflow path, you will have to update the .dockstore.yml file directly on the corresponding GitHub branch. For example, if develop has a .dockstore.yml that points to my_workflow.wdl, but my_workflow.wdl is moved to another path on the branch develop-but-better, then the .dockstore.yml on develop-but-better will need to point to the new location of my_workflow.wdl.

.. _Check GitHub App installation on repository:

How do I check if the Dockstore GitHub App was installed on an individual repository?
--------------------------------------------------------------------------------------
Go to your repo on GitHub, click the Settings tab, click Integrations on the left and verify our app is installed and configured correctly

.. image:: /assets/images/docs/github-repo-settings.png

You may not have access to this page if you are not an administrator of your GitHub organization, :ref:`but you may still be able to see if it installed. <view github app permissions hack>`

How do I configure the GitHub App across multiple repositories?
------------------------------------------------------------------
GitHub Apps can be installed on either an a user level, or an organizational level. If you installed the app for your own repos that are not in an organization, you will be able to verify the Dockstore GitHub App is installed by clicking "Applications" in the left menu in your GitHub settings. Our app, along with any others you may have installed, will be there. Clicking the "configure" button will allow you to adjust which repos the app has access to.

.. _view github app permissions hack:

How do I view/configure the GitHub App if I am not the admin of an organization?
--------------------------------------------------------------------------------

A GitHub organization's admins can configure an app directly in the organization's settings, but other members of the organization with less access may not see this option. However, you may be able to tell if your organization has already installed the app by trying to install the app again, which will take you to the app configuration process, although depending on your permissions your selected changes may not be saved. (See next question.)

.. image:: /assets/images/docs/reinstall-app-to-cheese-org-settings.png
   :width: 50%

.. _GitHub App permissions FAQ:

Can I use the GitHub App if I am not the admin of the organization and/or repo I am trying to use it with?
----------------------------------------------------------------------------------------------------------

Perhaps. GitHub permissions can quickly get complicated, as it involves two levels of permissions (organization-level and repo-level). As such, it isn't possible for us to cover all possibilities here, but we can go over some of the more common ones.

First of all, you can only configure already-installed GitHub Apps for organizations you are not an admin in if you go through the app installation process again. Be aware that in this scenario, you can only add repos that you have admin access to, not just maintainer access.

There are two scenarios to be aware of when installing the Dockstore GitHub App as a repository admin who is not an organization admin.

1. An organization admin configured the Dockstore GitHub App to be installed on all repositories.

   * Attempts to install the Dockstore GitHub App on any repository in the organization will result in an error from GitHub, regardless of whether or not the repository is one that the user has admin access to.
   * If it is a repository that the user has admin access to, the user can :ref:`check the repository to see if the app is indeed installed <Check GitHub App installation on repository>`.

2. An organization admin configured the Dockstore GitHub App to be installed on select repositories or the Dockstore GitHub App is not configured at all. 

   * The user can install the Dockstore GitHub App on repositories that they are an admin of.
   * If they attempt to install the app on a repository that they are not an admin of, it may look like the app install successfully, but in reality, it did not install. Instead, an organization admin will receive a request to install the Dockstore GitHub App on the repository. 

You may also still run into scenarios where your changes appear to not get saved, even though GitHub will not throw an error. For example, if you tried to give the GitHub App access to databiosphere/analysis_pipeline_wdl, and upon re-installation into the DataBiosphere organization, you do not see databiosphere/analysis_pipeline_wdl in the list of repositories it already has access to, there is a good chance GitHub is blocking you.

If it seems your GitHub App access just won't "stick" or you are having other permissions issues, consider asking the administrator of your organization to install the app. If they set it up to have access to all repositories on the organization, this will only need to be done once.

The changes made to my GitHub repo aren't appearing on Dockstore, but I've already installed the GitHub app and made the .dockstore.yml file. How can I figure out what's going wrong?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The general troubleshooting flow we recommend is the following:

- Try waiting a couple of minutes and refreshing the browser on the My Workflows/My Tools page again. Sometimes, GitHub takes a few minutes to send Dockstore the changes made to a repository.
- Verify that the GitHub app was given access to the right repository or organization. 
- If access was given to the wrong organization or repository, or this is your first time installing the app, you'll need to push another commit after adding the correct repository to activate the sync to Dockstore.
- Double check the .dockstore.yml file.

    - Is it in the root directory?
    - Is it on the right branch?
    - Are all indentation levels correct?
    - Is it named `.dockstore.yml` instead of `dockstore.yml` or `.dockstore.yaml`?
    - Does the name field match, if applicable?

If you've already tried these, you can view GitHub App logs through Dockstore to see if there have been any errors (see next section).

How do I view the GitHub App logs?
----------------------------------
Navigate to the ``/my-workflows`` (or ``/my-tools``) page and expand the GitHub Organization that the repository belongs to on the left hand side. Then click on the bottom where it says ``See GitHub App Logs``.

.. image:: /assets/images/docs/github-app-logs-button.png
   :width: 40 %

Once loaded, the following window will be displayed.

.. image:: /assets/images/docs/github-app-logs-window.png

Here you can view all the GitHub app events Dockstore is aware of and whether they failed or were successful. If there was a failure, you can expand that row and view the error message as shown below.

.. image:: /assets/images/docs/github-app-logs-error-message.png

In the case shown above, the error message is from parsing the following .dockstore.yml file.

.. code:: yaml

   version: 1.2
   workflows:
      - name: single workflow
        subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:

It is saying that the workflow name ``single workflow`` is invalid. The workflow name may only consist of alphanumeric characters, internal underscores, and internal hyphens. This error can be fixed by changing ``single workflow`` to ``single_workflow``, ``single-workflow``, or ``singleWorkflow``.

If you're having trouble finding the relevant logs, try searching for the name of your repository by using the filter on the upper left. You can also sort the rows by clicking on a column heading.
For example, if you click the ``Success`` column heading once, it will list all the events that failed first.

Why was a new workflow registered instead of migrating my existing one?
--------------------------------------------------------------------------
..
    Todo: Add information of how to delete

During the original registration for your workflow/tool, you may have filled out the name field as shown in the pictures below.
A new separate workflow/tool will be registered if the original name isn't included or doesn't match the ``name`` field in your .dockstore.yml file.

.. figure:: /assets/images/docs/workflow-name-field.png
   :alt: Workflow to Migrate
   :width: 55 %

.. figure:: /assets/images/docs/tool-name-field.png
   :alt: Tool to Migrate
   :width: 55 %


How can I convert my entire existing workflow/tool at once?
-------------------------------------------------------------
Currently you cannot convert all existing branches/versions at once. You must add a .dockstore.yml to each branch in order for the GitHub app
automatically detect and sync changes with the corresponding version on Dockstore.

If you have a .dockstore.yml file in your master or develop branches on GitHub, any new branches you create from these as your template
will have a  .dockstore.yml.
