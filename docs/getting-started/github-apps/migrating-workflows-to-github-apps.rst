Migrating Your Existing Workflows to Use GitHub Apps
======================================================

Dockstore 1.9.0 provides users with a way to keep their workflows automatically updated (instead of needing to manually refresh) by using GitHub apps. Here, we will go over how to migrate your existing Dockstore workflows to use our GitHub App.

GitHub App Installation
-----------------------

The first step to migrating a workflow is the same as adding a new workflow via GitHub Apps: install our Dockstore GitHub App onto your repository or
organization, if you have not already done so.

.. include:: /getting-started/github-apps/snippet--installation.rst

.. include:: /advanced-topics/naming-workflows.rst

Creating a .dockstore.yml File
-------------------------------

Once the GitHub app is installed on the correct repo, the next step is to create a .dockstore.yml file. We'll cover a very straightforward example
first, but depending on how you configured the workflow during registration and whether your GitHub repository houses multiple workflows published on Dockstore,
there will be additional steps to writing your .dockstore.yml file.

Let's say we have the following CWL workflow registered on Dockstore that came from this `repository <https://github.com/NatalieEO/ghapps-single-workflow>`__ and you would like to convert the master branch.

.. figure:: /assets/images/docs/single-workflow-to-migrate.png
   :alt: Workflow to Migrate

As noted in our other documentation, create a .dockstore.yml file in the root directory of the branch you want to migrate (in this example, it's the master branch) in your repository. The file should look like the following

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test/dockstore.cwl.json

The information above was filled out using the following:

- ``subclass`` is taken from the ``Descriptor Type``
- ``primaryDescriptorPath`` is from ``Workflow Path``
- ``testParameterFiles`` is from ``Test File Path``

During the original registration for your workflow, you may have filled out the ``Workflow Name`` field shown in the picture below.

.. figure:: /assets/images/docs/workflow-name-field.png
   :alt: Workflow to Migrate
   :width: 60 %

To check if the workflow you want to migrate has a workflow name set, select the workflow and look at the title on top, seeing if it has a fourth component to its title. As mentioned above, if you see a workflow name inserted, you must include the name field in your .dockstore.yml file.

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test/dockstore.cwl.json
        name: optional-name

If you have multiple workflows registered on Dockstore that stem from the same GitHub repo, a single .dockstore.yml can be used to convert them.
Again, you need to check for the Workflow Name field being set because it's needed for multi workflow repositories.
If the name field in the ``dockstore.yml`` doesn't match the Workflow Name field in Dockstore, the migration of your workflow on Dockstore will not go through and it will instead create a new Dockstore entry.
Let's say we want to convert these two workflows that come from this `repository <https://github.com/NatalieEO/ghapps-single-workflow>`__.

.. image:: /assets/images/docs/github-apps-multiple-workflows.png

.. image:: /assets/images/docs/github-apps-multiple-workflows-with-name.png

Your .dockstore.yml would look like the following:

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test/dockstore.cwl.json
      - subclass: WDL
        primaryDescriptorPath: /Dockstore.wdl
        testParameterFiles:
            - /test/dockstore.wdl.json
        name: optional-name

Testing the Migration
----------------------

.. note:: Push events will only be captured by Dockstore **after** installing the GitHub app onto the repo.

To test out your GitHub app integration, make a push to a branch. Navigate to or refresh your browser on the My Workflows page, and select the workflow you wanted to convert.
You should see that the ``Workflow Information`` section looks a bit different.

.. image:: /assets/images/docs/workflow-information-after-migration.png

It now lists the mode as ``Automatically synced via GitHub App`` instead of ``Full``, and information about paths is no longer included.
You are also no longer able to refresh or restub the workflow any more. Since you can't refresh the entire workflow anymore, **new** versions from GitHub (releases/branches) that you want to add to Dockstore must have a .dockstore.yml file.
However, you can still refresh already existing versions/branches on Dockstore that you haven't converted by going to the Versions tab, clicking Actions, and selecting Refresh Version.


.. seealso::
    :doc:`Troubleshooting and FAQ <github-apps-troubleshooting-tips>` - tips on resolving Dockstore GitHub App issues.

.. discourse::
    :topic_identifier: 6487
