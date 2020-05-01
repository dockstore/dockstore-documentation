Dockstore GitHub App
====================

Overview
--------

This document gives a high level overview of the GitHub Apps and the Dockstore
GitHub App in particular. For details on configuring and using the Dockstore
GitHub App with workflows or services, please see either
:doc:`Getting Started with Workflow <./dockstore-workflows>` or
:doc:`Getting Started with Services <./getting-started-with-services>`,
respectively.

With the Dockstore GitHub App, authors do not need to manually refresh their
workflows/services on Dockstore to get the latest changes from GitHub. Dockstore will
automatically update whenever the corresponding repository is updated on GitHub.

GitHub Apps
-----------

`GitHub apps <https://developer.github.com/apps>`_ are a GitHub feature used to
improve the interaction between external applications and GitHub. Users can
grant a GitHub app specific permissions on the repos and/or
organizations of their choosing. When events occur on the GitHub repos, e.g.,
creating a new release, the GitHub App issues notifications.

Why have a Dockstore GitHub App?
--------------------------------

Without a GitHub App, Dockstore does not know when you have modified a GitHub
repository.

For example, take the case when you first add a tool or workflow to Dockstore
from GitHub.  Dockstore indexes the repository -- it reads the the relevant
repository content, branches, and releases from GitHub. When you subsequently
make changes to your GitHub repo, such as push new commits, create new branches
and/or publish new releases, Dockstore is unaware of those changes. You are
responsible for going to Dockstore, finding the tool/workflow that corresponds
to the GitHub repo, and manually refreshing the tool/workflow by either clicking
the Refresh button or making an API call to the Dockstore API.

Due to the manual nature of this process, it is easy for Dockstore to get out of
sync with the linked GitHub repository.

How the Dockstore GitHub App works
----------------------------------

With the Dockstore GitHub App, the synchronization is done automatically. When
you add a new branch or release of a workflow on GitHub, Dockstore is notified,
and Dockstore updates its copy of the workflow. For example, After publishing a new release
of a workflow on GitHub, a new version of the workflow will be present in
Dockstore shortly afterwards.

For this to work, a ``/.dockstore.yml`` file is required in the root directory of each GitHub repository you want
to associate with a workflow on Dockstore. A template for both workflows and services are shown below,
along with explanations for each field. For every branch on GitHub that has one of these files, a corresponding entry
will be made on Dockstore.

Workflow YML File
++++++++++++++++++
Ex. .dockstore.yml with a single workflow

.. code:: yaml

   version: 1.2
   workflows:
      - name: aligner
        subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test/dockstore.cwl.json

version
    The version of the .dockstore.yml schema. Currently at 1.2.
workflows
    An array of workflows. Each element corresponds to a workflow on Dockstore.
name (optional)
    The optional workflow name that is used to uniquely identify workflows in repositories with multiple workflows.
    **Each element must have a unique name.**
subclass
    The descriptor language used for the workflow. Supported values include CWL, WDL, and NFL.
primaryDescriptorPath
    The path to the primary descriptor file in the Git repository
testParameterFiles (optional)
    An array of paths to test parameter files in the Git repository.

Ex. .dockstore.yml with multiple workflows

.. important:: The **name** field is an optional field used when a repository has multiple workflows in it that a user wants to register
    as separate entries on Dockstore. Each entry within a .dockstore.yml file corresponds to a unique entry on Dockstore.

.. code:: yaml

   version: 1.2
   workflows:
      - name: globalAligner
        subclass: CWL
        primaryDescriptorPath: /runGlobalAligner.cwl
        testParameterFiles:
            - /test/globalAligner.cwl.json
      - name: localAligner
        subclass: CWL
        primaryDescriptorPath: /runLocalAligner.cwl
        testParameterFiles:
            - /test/localAligner.cwl.json

A common pattern seen on Dockstore are GitHub repositories that store many workflows. The above .dockstore.yml
has two entries for workflows. Notice that each entry uses a different name. Names are required if you want 
multiple workflows registered on Dockstore from a single GitHub repository. The names must be unique between
entries of the `workflows` array. For each unique name present, an entry will be created on Dockstore.

Service YML File
+++++++++++++++++
TODO

See Also
--------

- :doc:`Getting Started with Services <./getting-started-with-services>`
- :doc:`Getting Started with Workflows <./dockstore-workflows>`

.. discourse::
       :topic_identifier: 2240
