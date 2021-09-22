
Getting Started with Galaxy
===========================

Dockstore supports Galaxy workflows and the :doc:`Launch with Galaxy <../../launch-with/galaxy-launch-with>` tutorial elaborates different ways to launch a Galaxy workflow. Please note that Galaxy workflows cannot be launched by the Dockstore CLI.

Unlike WDL and CWL, Galaxy
workflows in the near term are primarily created and modified
from the Galaxy workflow editor (GUI), instead of a text editor.

Tutorial Goals
--------------

-  Learn about `Galaxy <https://training.galaxyproject.org/>`__
-  Create and run a basic Galaxy workflow
-  Export the workflow to a file
-  Setup a GitHub account and repository
-  Push the workflow to GitHub
-  Make a GitHub release

Create a basic Galaxy workflow
------------------------------

Create and run your workflow in Galaxy. Here  is a tutorial for `Creating, Editing, Importing Galaxy Workflows <https://training.galaxyproject.org/training-material/topics/galaxy-interface/tutorials/workflow-editor/tutorial.html>`__

Export the workflow to a file
-----------------------------

In Galaxy:

- Click on the Galaxy UI Workflow link at the top of the page.
- Click on the workflow name to expose the drop down menu.
- Click Download

The exported JSON file with a '.ga' suffix describes the inputs,
outputs, and Galaxy Tool Shed dependencies for your workflow.


.. figure:: /assets/images/docs/galaxy_download.png
   :alt: Download

   Download

Setting up GitHub
-----------------

You will need to add the Galaxy workflow file you downloaded to a source code
repository that Dockstore knows about. GitHub is a good choice, and if you
are not familiar with GitHub you can use this
`tutorial <https://guides.github.com/activities/hello-world/>`__ to set up
an account and repository.

Upload the workflow to GitHub
-----------------------------

- Go to your repository and click on the Upload Files menu item under Add Files
- Click on the 'choose your files' link
- Select your '.ga' Galaxy workflow file
- Click on 'Commit changes'

These steps are outlined `here. <https://docs.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository>`__

Releasing on GitHub
-------------------

Now that we've successfully created our workflow in Galaxy and tested it the
workflow is ready to share with others. Making a release on GitHub will tag
your GitHub repository with a version tag so you can always get back to
this particular release. Follow the steps outlined `here <https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository>`__
to create a release.

Next Steps
----------

Now that you have a git repository that includes a Galaxy workflow, and you
have tested it and are satisfied that it works the next step is to
register it on Dockstore.

If you haven't set up a Dockstore account follow the :doc:`next tutorial <register-on-dockstore/>` to create an
account on Dockstore and link third party services, which includes GitHub.
Otherwise follow the instructions for :doc:`workflow registration. <dockstore-workflows>`

See Also
--------
- :doc:`CWL <getting-started-with-cwl>`
- :doc:`WDL <getting-started-with-wdl>`
- :doc:`Nextflow <getting-started-with-nextflow>`
- :doc:`Language Support <../end-user-topics/language-support>`

