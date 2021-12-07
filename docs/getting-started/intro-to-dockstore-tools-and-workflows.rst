Introduction to Dockstore Tools and Workflows
=============================================


Comparison of Tools and Workflows Across Descriptor Languages
-------------------------------------------------------------

When Dockstore was created, CWL was the first descriptor language we supported. CWL has a very clear distinction between a tool and a
workflow. And while other descriptor languages, like WDL and Nextflow, do not have separate concepts for tools and workflows,
Dockstore has chosen to treat the two differently. However, our defintion for each does not strictly align with the language's specification.
Instead, Dockstore tools are more associated with creating/owning Docker images that are used in conjunction with a descriptor language, and
Dockstore workflows are closely tied with the descriptor files themselves.


+------------------------+------------------------------------------+-------------------------------------------------+
| Support                | Tool                                     | Workflow                                        |
+========================+==========================================+=================================================+
| CWL                    | - Class: CommandLineTool                 | - Class: Workflow                               |
+------------------------+------------------------------------------+-------------------------------------------------+
| WDL                    | - A single task with Docker image        | - >1 task                                       |
|                        | - A workflow section that runs the task  | - A workflow section that connects the tasks    |
|                        | - An associated Docker image             |                                                 |
+------------------------+------------------------------------------+-------------------------------------------------+
| Nextflow               | - N/A                                    | - Any valid Nextflow workflow                   |
+------------------------+------------------------------------------+-------------------------------------------------+
| Galaxy                 | - N/A*                                   | - Any valid Galaxy workflow                     |
+------------------------+------------------------------------------+-------------------------------------------------+
| Versioning             | - Based off of image's tags              | - Based off of branches/tags from Git repository|
+------------------------+------------------------------------------+-------------------------------------------------+

\* There are tools that make up Galaxy workflows from the Galaxy toolbox or ToolShed.
Dockstore does not support registration of these tools.



Tools
-----

Dockstore tool registration is meant for users who have created or have access/permissions to a Docker image registered to one of our supported container registries, and have
written tool descriptor files (in CWL/WDL) that use it. At a basic level, the Docker image describes the tool environment and the descriptor files describe how the tool is run.
If you are unfamiliar with Docker or how to write descriptor files, check out our following tutorials:

- :doc:`Docker <getting-started-with-docker>`
- :doc:`CWL <getting-started-with-cwl>`
- :doc:`WDL <getting-started-with-wdl>`

Dockstore:

- has varying levels of support for images registered on Quay.io, DockerHub, GitLab, Amazon ECR, and Seven Bridges
- supports descriptor files hosted on GitHub, BitBucket, GitLab, or written on Dockstore
- supports descriptor files written in CWL or WDL
- offers three different tool registration paths

The most convenient way to register your tool and manage it on Dockstore is to have your image registered on Quay.io, your descriptor files hosted on GitHub, and choose our quick registration path.
This gives Docktore the ability to automatically recognize the image's tags on Quay, link them back to the appropriate version on GitHub, and create the existing versions for you on Dockstore once you hit "Refresh".
If your image is registered on one of our other supported registries, you will have to register your tool manually. This means each version you want put on Dockstore must be added manually.
To learn more about our different registration options, read our following tutorials:

- :doc:`Tools <dockstore-tools>`
- :doc:`Hosted Tools <hosted-tools-and-workflows>`

.. note::
  Dockstore tool versions are based on the image's tags, not the tags/branches from the git repository where the descriptor files are hosted.


Workflows
---------

Dockstore workflow registration is meant for users who have created or have access to descriptor files (in CWL, WDL, Galaxy, Nextflow). As mentioned above in the Tools section,
CWL and Galaxy classify tools and workflows differently, so only descriptor files written that follow language's respective specification for a workflow will be valid on Dockstore.

Dockstore:

- has varying levels of support for descriptor files registered on GitHub, BitBucket, and GitLab, or written on Dockstore
- supports descriptor files written in CWL, WDL, Galaxy, and Nextflow
- offers four different workflow registration paths

The most convenient way to register your workflow is to push your descriptor files to a GitHub repository and choose our GitHub App installation registration path. Choosing this
option allows Dockstore to automatically create and update versions on Dockstore every time a push is made or tag created. To learn more about this and our other registration options, read the following tutorials:

- :doc:`GitHub Apps </getting-started/github-apps/github-apps-landing-page>`
- :doc:`Workflows <dockstore-workflows>`
- :doc:`Hosted Workflows <hosted-tools-and-workflows>`





