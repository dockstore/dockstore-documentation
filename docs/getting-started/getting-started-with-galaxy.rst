.. note:: This tutorial is a continuation of :doc:`Getting Started With Docker </getting-started/getting-started-with-docker>`. Please complete that tutorial prior to doing this one.

Getting Started with Galaxy workflows
=====================================

Tutorial Goals
--------------

-  Learn about `Galaxy <https://training.galaxyproject.org/>`__
-  Create and run a basic Galaxy workflow
-  Export the workflow to a file
-  Push the workflow to GitHub

Create a basic Galaxy workflow
------------------------------

Create and run your workflow in Galaxy. Here  is a tutorial for `creating, editing, running and importing Galaxy workflows <https://training.galaxyproject.org/training-material/topics/galaxy-interface/tutorials/workflow-editor/tutorial.html>`__

Export the workflow to a file
-----------------------------

- Click on the Galaxy UI Workflow link at the top of the page.
- Click on the History Options gear at the top right of the page.
- Under Downloads select Export History to File

The exported YAML (Or JSON) file describes the inputs, outputs, and Galaxy Tool Shed
dependencies for your workflow.

Releasing on GitHub
-------------------

.. include:: github-apps.rst

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

