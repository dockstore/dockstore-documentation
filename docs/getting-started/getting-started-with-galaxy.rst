
Getting Started with Galaxy
===========================

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

Create and run your workflow in Galaxy. Here  is a tutorial for `creating, editing, running and importing Galaxy workflows <https://training.galaxyproject.org/training-material/topics/galaxy-interface/tutorials/workflow-editor/tutorial.html>`__

Export the workflow to a file
-----------------------------

- Click on the Galaxy UI Workflow link at the top of the page.
- Click on the workflow name to expose the drop down menu.
- Click Download

The exported YAML (Or JSON) file with a '.ga' suffix describes the inputs,
outputs, and Galaxy Tool Shed dependencies for your workflow.

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

These steps are outlined `here <https://docs.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository>`__

Releasing on GitHub
-------------------

.. include:: releasing-on-github.rst


Next Steps
----------

Now that you have a git repository that includes a Galaxy workflow, and you
have tested it and are satisfied that it works the next step is to
register it on Dockstore.

Follow the :doc:`next tutorial </getting-started/register-on-dockstore/>` to create an
account on Dockstore and link third party services.

See Also
--------
- :doc:`CWL <getting-started-with-cwl>`
- :doc:`WDL <getting-started-with-wdl>`
- :doc:`Nextflow <getting-started-with-nextflow>`
- :doc:`Language Support <../end-user-topics/language-support>`

