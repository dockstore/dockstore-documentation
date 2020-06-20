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
Installing our Dockstore GitHub App onto your Github repository or organization will automatically sync your workflow on Dockstore whenever code is pushed to GitHub.
This means less manual work for workflow developers, and less waiting for content to update.

This requires the addition of a ``/.dockstore.yml`` file to your repository on Github.
This file contains workflow information such as workflow path, test parameter paths, etc. that Dockstore will use to setup
the corresponding workflow on Dockstore. It's important to note, that you will need a ``/.dockstore.yml`` file on each branch of your Github
repository if you want to sync multiple branches (versions) of your workflow.

You can read more about it at :doc:`/getting-started/github-apps/github-apps`.

How does this change my development flow?
-------------------------------------------
If you have a ``/.dockstore.yml`` file in your master or develop branches on GitHub, any new branches you create from these as your template
will have a  ``/.dockstore.yml``.
As long as your workflow is already registered on Dockstore, your new branches will automatically sync corresponding new versions of the workflow on Dockstore.

*Note:* If you want to edit version information, such as workflow path, you will have to update the ``/.dockstore.yml`` file directly on the corresponding GitHub branch.
You can no longer do this directly on Dockstore.

How do I check if the Dockstore Github App was installed?
-----------------------------------------------------------
If you don't see changes, try waiting a couple of minutes and refreshing the browser on the My Workflows page again.

You can also verify that the GitHub App was given access to the right repository or organization. If access was given to the wrong organization or repository,
you'll need to push another commit after correcting it to activate the sync to Dockstore.


    - Go to your repo on GitHub, click the Settings tab, click Integrations on the left and verify our app is installed and configured correctly

.. image:: /assets/images/docs/github-repo-settings.png

- Double check the ``/.dockstore.yml`` file.

    - Is it in the root directory?
    - Is it on the right branch?
    - Are all indentation levels correct?
    - Does the name field match, if applicable?

Can I use Github Apps to register tools?
------------------------------------------
The Dockstore Github App currently only supports Workflows and Services.

Why was a new workflow registered instead of migrating my existing one?
--------------------------------------------------------------------------
..
    Todo: Add information of how to delete

During the original registration for your workflow, you may have filled out the ``Workflow Name`` field shown in the picture below.
A new separate workflow can be registered if the original ``Workflow Name`` isn't included or doesn't match the ``name`` field in your ``/.dockstore.yml``.

.. figure:: /assets/images/docs/workflow-name-field.png
   :alt: Workflow to Migrate
   :width: 75 %


How can I convert my entire existing workflow at once?
----------------------------------------------------------
Currently you cannot convert all existing branches/versions at once. You must add a ``/.dockstore.yml`` to each branch in order for the Github app
automatically detect and sync changes with the corresponding version on Dockstore.

If you have a ``/.dockstore.yml`` file in your master or develop branches on GitHub, any new branches you create from these as your template
will have a  ``/.dockstore.yml``.
