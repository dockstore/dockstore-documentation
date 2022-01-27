Introduction to Workflows, Tools, and Services
==============================================

What is a workflow?
-------------------

In general terms, a workflow is a chain of commands that has several steps linked together, which create some sort of final output. For example, a simple two-step workflow that converts a VCF into a GDS file may conceptually look like this:

vcf file --> convert to GDS file --> give each variant a unique ID --> a GDS file with unique IDs

In this case, the output of the conversion step is the input of the step that generates unique IDs, and the unique IDs step's output is the final output of the workflow: A GDS file with unique IDs. 

Managing workflows can be complicated, as you may be chaining together many steps, each with different computational requirements. This where workflow languages step in, allowing us to create formal "tasks" which can each have their own computational settings or Docker container, and chaining the output of one task into the input of another task.


What is a tool?
---------------

In a very broad sense, we define a tool on Dockstore as a CWL or WDL program that performs a single task in a unique Docker container. 

The distinction between a tool and a workflow is very clear in CWL, because they are seperate classes (CommandLineTool vs Workflow). In WDL, things are a little fuzzier, but think of them as single-task workflows associated with a unique Docker image. Tools do not exist in the context of Nextflow or Galaxy.

Generally speaking, if you care more about the Docker image than the description file, you are dealing with a tool. If you care more about the description file, you are dealing with a workflow. Dockstore tool versions are based on the image's tags, while Dockstore workflow versions are based on the tags/branches from the git repository that hosts the descriptor file. For more information, you can read :doc:`a detailed breakdown on tools and services here </advanced-topics/tools-vs-workflows>`.

.. tip::
  Although Terra requires that each task in a WDL workflow runs in a Docker container, Terra does not support WDL tools. If you are writing a WDL with the intent of it being run in the Terra ecosystem, we recommend writing it as a workflow.


What is a service?
------------------

Services are meant to be long running processes, usually web services or interactive applications, that can be launched by a user. 

