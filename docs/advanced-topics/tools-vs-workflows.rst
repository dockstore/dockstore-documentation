Tools vs Workflows: Detailed Comparison
=======================================

.. tip::
  Generally speaking, if you care more about the Docker image than the description file, and are using CWL, you are dealing with a tool. If you care more about the description file, you are dealing with a workflow.

History
-------
When Dockstore was created, CWL was the first descriptor language we supported. CWL has a very clear distinction between a tool and a workflow. However, our definition for each does not completely align with the language's specification -- strictly speaking, a CWL CommandLineTool does not require a Docker image, but we require tools to be associated with a Docker image on Dockerstore. Furthermore, while other descriptor languages do not have separate concepts for tools and workflows, we still maintain a distinction between a tool and a workflow for WDL for legacy reasons.


Should I write a tool or a workflow?
------------------------------------
.. hint::
    We generally **discourage** people from writing/registering WDL tools and may depreciate them in the future.

Dockstore tools are more associated with creating/owning Docker images that are used in conjunction with a descriptor language, and Dockstore workflows are more closely tied to the descriptor files themselves. If you control the Docker image being used by your CWL program, and want verisoning to be based upon that images tags, you should probably write a tool. If you do not control the Docker image being used, and/or are not writing in CWL, you should probably write a workflow. Of course, everyone's use case is different. We encourage you to look around Dockstore for inspiration for your next bioinformatics project.

Overview
--------

+------------------------+------------------------------------------+-------------------------------------------------+
| Language               | Tool                                     | Workflow                                        |
+========================+==========================================+=================================================+
| CWL                    |  - Class: CommandLineTool                |  - Class: Workflow                              |
|                        |  - Dockerfile for the tool's image       |  - No Dockerfile required                       |
+------------------------+------------------------------------------+-------------------------------------------------+
| WDL                    |  - One task that runs in a Docker image  |  - ≥1 task, which could run in Docker image     |
|                        |  - A workflow section that runs the task |  - A workflow section that runs the task(s)     |
|                        |  - The Dockerfile for the task's image   |  - No Dockerfile required                       |
+------------------------+------------------------------------------+-------------------------------------------------+
| Nextflow               | N/A                                      | Any valid Nextflow workflow                     |
+------------------------+------------------------------------------+-------------------------------------------------+
| Galaxy                 | N/A*                                     | Any valid Galaxy workflow                       |
+------------------------+------------------------------------------+-------------------------------------------------+

\* There are tools that make up Galaxy workflows from the Galaxy toolbox or ToolShed.
Dockstore does not support registration of these tools.


+------------------------+------------------------------------------+-------------------------------------------------+
| Dockstore Support      | Tool                                     | Workflow                                        |
+========================+==========================================+=================================================+
| "Launch with" support  |  Only via Dockstore CLI                  |  Dockstore CLI & "launch with" buttons on entry |
+------------------------+------------------------------------------+-------------------------------------------------+
| Versioning             |  Based off of image's tags               |  Based off of branches/tags from Git repository,|
|                        |                                          |                                                 |
|                        |                                          |  even if one of the tasks executes in a Docker  |
|                        |                                          |  image.                                         |
+------------------------+------------------------------------------+-------------------------------------------------+

What about workflows that run in Docker containers?
---------------------------------------------------

Workflow descriptor files do not require a Docker container. That being said, you can still specify external Docker images
within the descriptor files. Each task (WDL) or step (CWL) can specify a Docker image, which might be totally different from the Docker image used by a previous task/step in the workflow. Because of this, workflows registered on Dockstore that reference Docker image(s) will still follow versioning from GitHub, instead of versioning based on the tags of the Docker image(s).

.. hint::
    The Cromwell execution engine requires that WDL task specify a Docker image when running on GCP or AWS backends, including Terra. Therefore, if your WDL workflow needs to run on Terra, make sure that each task uses the Docker runtime attribute. For more information see the `Cromwell docs <https://cromwell.readthedocs.io/en/stable/RuntimeAttributes/#docker>`_.


Tools
-----

Dockstore tool registration is meant for users who have created or have access/permissions to a Docker image registered on one of our supported container registries, and have
written descriptor files (in CWL/WDL) that use it. At a basic level, the Docker image describes the tool environment and the descriptor files describe how the tool is run.
If you are unfamiliar with Docker or how to write descriptor files, check out the following tutorials:

- :doc:`Docker </getting-started/getting-started-with-docker>`
- :doc:`CWL </getting-started/getting-started-with-cwl>`
- :doc:`WDL </getting-started/getting-started-with-wdl>`

Dockstore:

- has varying levels of support for images registered on Quay.io, DockerHub, GitLab, Amazon ECR, GitHub Container Registry, and Seven Bridges
- supports descriptor files hosted on GitHub, BitBucket, GitLab, or written on Dockstore
- supports descriptor files written in CWL or WDL
- offers three different tool registration paths

The most convenient way to register your tool and manage it on Dockstore is to have your image registered on Quay.io, your descriptor files hosted on GitHub, and choose our quick registration path.
This gives Docktore the ability to automatically recognize the image's tags on Quay, link them back to the appropriate version on GitHub, and create the existing versions for you on Dockstore once you hit "Refresh".
If your image is registered on one of our other supported registries, you will have to register your tool manually. This means each version you want put on Dockstore must be added manually.
To learn more about our different registration options, read the following tutorials:

- :doc:`Tools </getting-started/dockstore-tools>`
- :doc:`Hosted Tools </getting-started/hosted-tools-and-workflows>`

.. note::
  Dockstore tool versions are based on the image's tags, not the tags/branches from the git repository where the descriptor files are hosted.

.. tip::
  Terra does not support WDL tools. If you are writing a WDL with the intent of it being run in the Terra ecosystem, we recommend writing it as a workflow.


Workflows
---------

Dockstore workflow registration is meant for users who have created or have access to descriptor files (in CWL, WDL, Galaxy, Nextflow). As mentioned above in the Tools section,
CWL and Galaxy classify tools and workflows differently, so only descriptor files written in a manner that follows a language's respective specification for a workflow will be valid on Dockstore.

Dockstore:

- has varying levels of support for descriptor files registered on GitHub, BitBucket, and GitLab, or written on Dockstore
- supports descriptor files written in CWL, WDL, Galaxy, and Nextflow
- offers four different workflow registration paths

The most convenient way to register your workflow is to push your descriptor files to a GitHub repository and choose our GitHub App installation registration path. Choosing this
option allows Dockstore to automatically create and update versions on Dockstore every time a push is made or tag created. To learn more about this and our other registration options, read the following pages:

- :doc:`GitHub Apps </getting-started/github-apps/github-apps-landing-page>`
- :doc:`Workflows </getting-started/dockstore-workflows>`
- :doc:`Hosted Workflows </getting-started/hosted-tools-and-workflows>`





