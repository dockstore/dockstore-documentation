A Note on Naming Workflows on Dockstore
---------------------------------------
Workflow paths are unique, descriptive identifiers for a workflow. In other words,
each workflow on Dockstore has a unique identifier in the form of a path. This path is based on
the Git repository that the workflow comes from. There are four components to a path, but only
three are required. It has the following structure:

``<sourceControl>/<organization name>/<repository name>/<optional workflow name>:<version name>``

Why not simply use a number to identify the workflow? With a path like that shown above, users
can quickly understand the purpose of a workflow along with where it came from.

Ex. If I had a GitHub repository called BAMstats that existed in the OICR organization, and I did not give the workflow an optional name, the path of the workflow created from that repository would be the following:

``github.com/OICR/BAMstats``

The final optional component for the workflow path is the workflow name. This is a user defined
string that will be appended to the end of the required workflow path. It is useful in two situations:

1) The name of the repository doesn't represent the workflow, or
2) The repository contains multiple workflows

Using the previous example, we could set the workflow name to ``coverage``. Our path would now be:

``github.com/OICR/BAMstats/coverage``

If we set the workflow name, we must include it in our path when referencing the workflow. You also should be aware of a workflow's name when it comes to migrating a workflow registered via legacy methods to GitHub App registration methods. During the migration process, be sure to include the workflow's name as a field on your .dockstore.yml file.