Introduction to Workflows, Tools, and Services
==============================================

What is a workflow?
-------------------

In general terms, a workflow is a chain of commands that has several steps linked together, which create some sort of final output. For example, a simple two-step workflow that converts a VCF into a GDS file may conceptually look like this:

vcf file --> convert to GDS file --> give each variant a unique ID --> a GDS file with unique IDs

In this case, the output of the conversion step is the input of the step that generates unique IDs, and the unique IDs step's output is the final output of the workflow: A GDS file with unique IDs. 

Managing workflows can be complicated, as you may be chaining together many steps, each with different computational requirements. This is where workflow languages step in, allowing us to create formal "tasks" which can each have their own computational settings or Docker container, and chaining the output of one task into the input of another task.

What is a tool?
---------------
How Dockstore defines a tool is changing, but our aim is to align our tool definition with that of the languages we support.
For the sake of simplicity, Dockstore only recommends registering a Dockstore tool when your work is a CWL CommandLineTool.

If you want a deeper understanding of the history of Dockstore tools and where we plan on going, read :doc:`Dockstore Tools Overhaul </../advanced-topics/dockstore-tools-overhaul>`.


What is a service?
------------------

Services are meant to be long running processes, usually web services or interactive applications, that can be launched by a user. 

