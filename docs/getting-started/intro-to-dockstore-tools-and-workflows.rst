Introduction to Workflows and Tools
==============================================

Tools and workflows hosted on Dockstore are computational programs described in languages that make it easy for their reuse in different compute environments. Generally, descriptor languages leverage a containerized compute environment (such as a Docker image) that packages up all of the code and dependencies needed to complete the computational step.

Not all descriptor languages make a distinction between a tool and a workflow. Most users will register workflows on Dockstore. 

What is a workflow?
-------------------

In general terms, a workflow describes a chain of commands. For example, a simple two-step workflow that converts a VCF into a GDS file may conceptually look like this:

VCF file --> convert to GDS file --> give each variant a unique ID --> a GDS file with unique IDs

In this case, the output of the conversion step is the input of the step that generates unique IDs, and the unique IDs step's output is the final output of the workflow: A GDS file with unique IDs. 

Managing workflows can be complex, as you may be chaining together many steps, each with different computational requirements. This is where workflow languages step in, allowing us to create formal "tasks" which can each have their own computational settings or Docker container, and chaining the output of one task into the input of another task.

What is a tool?
---------------
A tool represents a single command line tool wrapped in a descriptor language.  Languages that formally describe tools (such as CWL) may chain them together into a workflow.


Introduction to Services
==============================================

Services are containerized programs that are meant to be long running processes, usually web services or interactive applications, and that can be launched by a user into different environments. Dockstore services are currently in beta. 

