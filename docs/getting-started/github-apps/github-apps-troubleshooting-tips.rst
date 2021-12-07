================================================
Troubleshooting and Frequently Asked Questions
================================================

..
    Need to update with info about checking lambda errors in UI https://github.com/dockstore/dockstore/issues/3530

.. contents::
   :local:
   :depth: 2

Why should I migrate my existing workflows to use GitHub Apps and a .dockstore.yml?
----------------------------------------------------------------------------------------
Installing our Dockstore GitHub App onto your GitHub repository or organization will automatically sync your workflow on Dockstore whenever code is pushed to GitHub.
This means less manual work for workflow developers, and less waiting for content to update.

This requires the addition of a ``/.dockstore.yml`` file to your repository on GitHub.
This file contains workflow information such as workflow path, test parameter paths, etc. that Dockstore will use to setup
the corresponding workflow on Dockstore. Branches that do not have a ``/.dockstore.yml`` file will not be synchronized.

You can read more about it at :doc:`/getting-started/github-apps/github-apps`.

How does this change my development flow?
-------------------------------------------
Adding a ``/.dockstore.yml`` file to a template branch (ex: master, develop, main) will make it so
any new branches created from this template will be automatically added to and synced on Dockstore.

Therefore, as long as your workflow is already registered on Dockstore and your ``/.dockstore.yml`` is configured correctly,
then updates to the workflow (including adding new versions) should happen continuously and automatically.

You can use filters in a ``/.dockstore.yml`` to avoid generating a corresponding workflow-version on Dockstore.

*Note:* If you want to edit version information, such as workflow path, you will have to update the ``/.dockstore.yml`` file directly on the corresponding GitHub branch. For example, if develop has a ``/.dockstore.yml`` that points to my_workflow.wdl, but my_workflow.wdl is moved to another path on the branch develop-but-better, then the ``/.dockstore.yml`` on develop-but-better will need to point to the new location of my_workflow.wdl.

How do I check if the Dockstore GitHub App was installed on an individual repository?
--------------------------------------------------------------------------------------
Go to your repo on GitHub, click the Settings tab, click Integrations on the left and verify our app is installed and configured correctly

.. image:: /assets/images/docs/github-repo-settings.png

How do I configure the GitHub App across multiple repositories?
------------------------------------------------------------------
GitHub Apps can be installed on either an a user level, or an organizational level. If you installed the app for your own repos that are not in an organization, you will be able to verify the Dockstore GitHub App is installed by clicking "Applications" in the left menu in your GitHub settings. Our app, along with any others you may have installed, will be there. Clicking the "configure" button will allow you to adjust which repos the app has access to.

Depending on the permissions you have on an organization, you may not be able to directly access an organization's settings. You can only configure GitHub Apps for organizations you are not an admin in if you go through the app installation process again, during which, the option to configure will appear. Be aware that can only add repos that you have admin access to, not just maintainer acccess.

.. image:: /assets/images/docs/reinstall-app-to-cheese-org-settings.png
   :width: 50%

The changes made to my GitHub repo aren't appearing on Dockstore, but I've already installed the GitHub app and made the ``.dockstore.yml`` file. How can I figure out what's going wrong?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If you don't see changes, try waiting a couple of minutes and refreshing the browser on the My Workflows page again. 

Be aware that a service disruption can result in a connection between GitHub and Dockstore getting delayed or lost. If the signal was lost, another push must be made.

You can also verify that the GitHub app was given access to the right repository or organization. If access was given to the wrong organization or repository,
or this is your first time installing the app, you'll need to push another commit after adding the correct repository to activate the sync to Dockstore.

Double check the ``/.dockstore.yml`` file.

    - Is it in the root directory?
    - Is it on the right branch?
    - Are all indentation levels correct?
    - Does the name field match, if applicable?

If you've already tried waiting a couple of minutes and refreshing the browser on the My Workflows page, you can view GitHub App logs through Dockstore to see if there have been any errors.
Navigate to the ``/my-workflows`` page and expand the GitHub Organization that the repository belongs to on the left hand side. Then click on the bottom where it says ``See GitHub App Logs``.

.. image:: /assets/images/docs/github-app-logs-button.png
   :width: 40 %

Once loaded, the following window will be displayed.

.. image:: /assets/images/docs/github-app-logs-window.png

Here you can view all the GitHub app events Dockstore is aware of and whether they failed or were successful. If there was a failure, you can expand that row and view the error message as shown below.

.. image:: /assets/images/docs/github-app-logs-error-message.png

In the case shown above, the error message is from parsing the following ``/.dockstore.yml`` file.

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

Can I use GitHub Apps to register tools?
------------------------------------------
The Dockstore GitHub App currently only supports Workflows and Services.

Why was a new workflow registered instead of migrating my existing one?
--------------------------------------------------------------------------
..
    Todo: Add information of how to delete

During the original registration for your workflow, you may have filled out the ``Workflow Name`` field shown in the picture below.
A new separate workflow will be registered if the original ``Workflow Name`` isn't included or doesn't match the ``name`` field in your ``/.dockstore.yml``.

.. figure:: /assets/images/docs/workflow-name-field.png
   :alt: Workflow to Migrate
   :width: 75 %


How can I convert my entire existing workflow at once?
----------------------------------------------------------
Currently you cannot convert all existing branches/versions at once. You must add a ``/.dockstore.yml`` to each branch in order for the GitHub app
automatically detect and sync changes with the corresponding version on Dockstore.

If you have a ``/.dockstore.yml`` file in your master or develop branches on GitHub, any new branches you create from these as your template
will have a  ``/.dockstore.yml``.
