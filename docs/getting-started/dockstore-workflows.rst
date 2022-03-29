Register a Workflow on Dockstore
================================

.. contents::
   :local:
   :depth: 2

Tutorial Goals
--------------

-  Discover how to register a workflow on Dockstore
-  Publish your workflow

This tutorial walks through the process of registering and sharing more
complex workflows which are usually comprised of multiple tools, strung together in some
sort of order (often a directed acyclic graph (DAG)). Workflows also
differ from tools since they are not required to define their own
environment. Instead, a workflow engine like
`Arvados <https://arvados.org/>`__ or
`Cromwell <https://github.com/broadinstitute/cromwell>`__, or
an infrastructure like `Galaxy <https://usegalaxy.org/>`__ will provide
the ability to execute a CWL, WDL, or Galaxy workflow respectively.

This tutorial does not go through the creation of a workflow and its
registration to GitHub, Bitbucket or GitLab. It assumes that you already
have a repository which contains a workflow and are now trying to register
it in Dockstore.

A Note on Naming Workflows on Dockstore
---------------------------------------
Workflow paths are unique, descriptive identifiers for a workflow. In other words,
each workflow on Dockstore has a unique identifier in the form of a path. This path is based on
the Git repository that the workflow comes from. There are four components to a path, but only
three are required. In most cases these three required components are all you need.

First we will look at the required components. This is the Git registry, the organization, and
the repository. They are joined together by forward slashes, which can be seen below:

``Git Registry/Organization/Repository``

Ex. If I had a GitHub repository called BAMstats that existed in the OICR organization, the path of
the workflow created from that repository would be the following:

``github.com/OICR/BAMstats``

Why not simply use a number to identify the workflow? With a path like that shown above, users
can quickly understand the purpose of a workflow along with where it came from.

The final optional component for the workflow path is the workflow name. This is a user defined
string that will be appended to the end of the required workflow path. It is useful in two situations:

1) The name of the repository doesn't represent the workflow, or
2) The repository contains multiple workflows

Using the previous example, we could set the workflow name to ``coverage``. Our path would now be:

``github.com/OICR/BAMstats/coverage``

If we set the workflow name, we must include it in our path when referencing the workflow.

Register Your Workflow in Dockstore
-----------------------------------
.. include:: /getting-started/github-apps/note--registration.rst

There are a variety of ways to get your workflows into Dockstore. GitHub App registration is the
recommended way to register for all new workflows on Dockstore using GitHub. The legacy registration process is used for Bitbucket and GitLab.

Register Your Workflow to Automatically Sync with GitHub (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the newest way of getting content onto Dockstore and is by far the most automated. Using
GitHub Apps, Dockstore can react to changes on GitHub as they are made, keeping Dockstore synced
with GitHub automatically.

.. include:: /getting-started/github-apps/note--registration.rst

.. include:: /getting-started/github-apps/installation.rst

Once you've installed our GitHub app on a repository or organization, you'll need to add a dockstore.yml file to
the root directory of a branch of the repository that contains your workflow. This file contains information like
workflow path, test parameter file, workflow name, etc. When a push is made on GitHub to a branch
with a .dockstore.yml, Dockstore will add that branch to the corresponding workflow on Dockstore. If the
workflow doesn't already exist on Dockstore, one will be created (but will not automatically be published publically). Note that a single dockstore.yml file can describe multiple workflows, if all of those workflows are in the same repository.

Below is a simple example of a .dockstore.yml file
for an alignment workflow to show you how easy it is to use. Note that all file paths in the file must be absolute.

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /aligner.cwl
        testParameterFiles:
        - /test/aligner.cwl.json

If you had our GitHub App installed on the repository ``myorg/alignments`` and then add the above .dockstore.yml to the **develop** branch,
the following would occur:

* A **CWL** workflow with the ID ``github.com/myorg/alignments`` will be created on Dockstore
* The version **develop** is added to the workflow ``github.com/myorg/alignments``
* The version has the primary descriptor file set to ``/aligner.cwl``
* The version has one test parameter file: ``/test/aligner.cwl.json``

Now that your workflow has been added, any time there is a push to a branch on GitHub for this repository that has a .dockstore.yml,
it is automatically updated on Dockstore! Anytime there is a deletion of a branch on GitHub that has a .dockstore.yml, the version is
removed from Dockstore.

For more information on this method, as well as general troubleshooting advice, please check our :doc:`Dockstore GitHub Apps Overview </getting-started/github-apps/github-apps>` page.

Legacy Registration Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /getting-started/github-apps/note--legacy-dont-sync.rst

If you are using BitBucket or GitLab and would prefer not to use GitHub, or if you are using GitHub but do not wish to install our app, our legacy registration methods have you covered. Several options are available to you and described in our :doc:`legacy registration methods documentation </advanced-topics/legacy/wf-legacy-registration>`.

Sharing Your Workflow
----------------------
.. include:: /getting-started/snippet--publish-workflow.rst

Next Steps
----------

You may not want to store your files directly with a service like
GitHub. Perhaps you want your descriptor files to not be public. The
solution is to use :doc:`Hosted Tools and
Workflows </getting-started/hosted-tools-and-workflows/>`.

.. discourse::
    :topic_identifier: 1292
