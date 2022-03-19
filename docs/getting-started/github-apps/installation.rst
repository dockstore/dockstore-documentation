====================================
Installing the Dockstore GitHub App
====================================

Installing the GitHub App is simple -- navigate to ``/my-workflows``, click the ``+`` button on the left hand sidebar, select ``Register using GitHub Apps``, and then click
``+ Manage Dockstore Installation on GitHub``.

.. image:: /assets/images/docs/add-workflow-button.png
   :width: 30 %

.. image:: /assets/images/docs/register-workflow-github-apps.png
   :width: 30 %

.. figure:: /assets/images/docs/gh-app-reg-1.png
   :width: 60 %

   Install our GitHub App on either all repositories in an organization or on specific repositories

You'll then be redirected to GitHub where you can grant the app access to specific repositories within whatever organization you are installing into. Note that GitHub treats your username as its own "organization." For instance, my GitHub username is aofarrel. If I want to install the GitHub App so it could access aofarrel/mycoolrepo, I would choose the first option here.

.. image:: /assets/images/docs/gh-app-install-where.png
   :width: 40 %

Once you've installed our GitHub app on a repository or organization, you'll need to add a ``/.dockstore.yml`` file to
the root directory of a branch of the repository that contains your workflow. This file contains information like
workflow path, test parameter file, workflow name, etc. When a push is made on GitHub to a branch
with a ``/.dockstore.yml``, Dockstore will add that branch to the corresponding workflow on Dockstore. If the
workflow doesn't already exist on Dockstore, one will be created (but will not automatically be published publically). Note that a single ``/.dockstore.yml`` file can describe multiple workflows, if all of those workflows are in the same repository.

Below is a simple example of a ``/.dockstore.yml`` file
for an alignment workflow to show you how easy it is to use. If you are interested in using this method, please see the 
complete documentation at the :doc:`Dockstore GitHub Apps </getting-started/github-apps/github-apps>` page. All paths in the file must be absolute.

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /aligner.cwl
        testParameterFiles:
        - /test/aligner.cwl.json

If you had our GitHub App installed on the repository ``myorg/alignments`` and then add the above ``/.dockstore.yml`` to the **develop** branch,
the following would occur.

* A **CWL** workflow with the ID ``github.com/myorg/alignments`` will be created on Dockstore
* The version **develop** is added to the workflow ``github.com/myorg/alignments``
* The version has the primary descriptor file set to ``/aligner.cwl``
* The version has one test parameter file: ``/test/aligner.cwl.json``

Now that your workflow has been added, any time there is a push to a branch on GitHub for this repository that has a ``/.dockstore.yml``,
it is automatically updated on Dockstore! Anytime there is a deletion of a branch on GitHub that has a ``/.dockstore.yml``, the version is
removed from Dockstore.

.. important:: The GitHub user who first adds a workflow onto Dockstore must correspond to a user on Dockstore.

A note on permissions
~~~~~~~~~~~~~~~~~~~~~

If you are adding the GitHub App to an organization for which you are not an admin, GitHub may block your ability to install the app, even if you have write access to the repository you are hoping to give the GitHub App permission to view. 

Sometimes, this will occur without GitHub notifying you that you have been blocked, but you might notice that if you go to install the GitHub App a second time, your previous selections have been cleared. For example, if you tried to give the GitHub App access to databiosphere/analysis_pipeline_wdl, and upon re-installation into the DataBiosphere organization, you do not see databiosphere/analysis_pipeline_wdl in the list of repositories it has access to, there is a good chance GitHub is blocking you.

If it seems your GitHub App access just won't "stick," consider asking the administrator of your organization to install the app. If they set it up to have access to all repositories on the organization, this will only need to be done once.

.. seealso::
    - :doc:`Automatic Syncing with GitHub Apps and .dockstore.yml </getting-started/github-apps/github-apps/>` - details on writing a .dockstore.yml file
    - :doc:`Migrating Your Existing Workflows </getting-started/github-apps/migrating-workflows-to-github-apps>` - a tutorial on converting already registered workflows
    - :doc:`Troubleshooting and FAQ </getting-started/github-apps/github-apps-troubleshooting-tips>` - tips on resolving Dockstore Github App issues.