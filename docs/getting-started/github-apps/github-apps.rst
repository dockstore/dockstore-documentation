=================================================================
Automatic Syncing with GitHub Apps and .dockstore.yml -- Overview
=================================================================
..
    TODO: update error handling section with info about checking lambda errors in UI https://github.com/dockstore/dockstore/issues/3530

.. note::
  Summary of GitHub App usage:

  #. :ref:`Install Dockstore GitHub App <Registration With GitHub Apps>`
  #. Put a valid .dockstore.yml file into the top level of your repository
  #. Push a new commit with a .dockstore.yml file present
  #. Wait up to 5 minutes for Dockstore to process the new version
  #. See workflow on Dockstore

This document gives a high level overview of how Dockstore uses GitHub apps.
For extra details on configuring and using the Dockstore
GitHub App with workflows or services, please see either
:ref:`Registration with GitHub Apps <Registration With GitHub Apps>` or
:doc:`Getting Started with Services </getting-started/getting-started-with-services>`.

With the Dockstore GitHub App installed, authors do not need to manually refresh their
workflows/services/tools on Dockstore to get the latest changes from GitHub. Dockstore will
automatically update whenever the corresponding repository is updated on GitHub.

What are GitHub Apps?
---------------------

`GitHub apps <https://developer.github.com/apps>`_ are a GitHub feature used to
improve the interaction between external applications and GitHub. Users can
grant a GitHub app specific permissions on the repos and/or
organizations of their choosing. When events occur on the GitHub repos, e.g.,
creating a new release, the GitHub app issues notifications.

Why have a Dockstore GitHub App?
--------------------------------

Without a GitHub app, Dockstore does not know when you have modified a GitHub
repository.

For example, take the case when you first add a workflow to Dockstore
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

With the Dockstore GitHub App installed, the synchronization is done automatically. When
you add a new branch or release of a workflow on GitHub, Dockstore is notified,
and Dockstore updates its copy of the workflow. For example, After publishing a new release
of a workflow on GitHub, a new version of the workflow will be present in
Dockstore shortly afterwards. For this to work, a ``/.dockstore.yml`` file is **required in the root directory of each GitHub repository** you want
to associate with a workflow/tool/service on Dockstore.

Simple templates for tools, workflows, and services are shown below,
as well as links to more advanced explanations of every field. For every branch/release on GitHub that has one of these files, a corresponding entry
will be made on Dockstore.

Error Handling
----------------------------------
It is possible for an invalid ``/.dockstore.yml`` to cause an errors. If we cannot read the 
file, then we do not know which workflow or service to associate the error with. For now, please ensure that your file is a valid YML file and
compare it with our examples/documentation to confirm that you filled it in correctly. If the file is at least present, an error will generally appear in the GitHub App logs (see `our FAQ document <https://docs.dockstore.org/en/develop/getting-started/github-apps/github-apps-troubleshooting-tips.html>`_).

Another possible issue is that we received the message from GitHub, but the user who triggered the message event is not registered on Dockstore with
the corresponding GitHub account. This is only an issue if the workflow or service does not already exist on Dockstore. When creating new workflows and
services, we need to be able to associate them with a user. If the workflow or service already exists on Dockstore, then this error will not occur and the 
version will be properly added/updated/deleted on Dockstore.

See `our FAQ document <https://docs.dockstore.org/en/develop/getting-started/github-apps/github-apps-troubleshooting-tips.html>`_ for assistance in troubleshooting, including how to interpret GitHub App logs.

As always, you can reach out to our team on our `discussion forum <https://discuss.dockstore.org/>`_ to discuss any issues you are facing.

Example YML Files
------------------

Workflow YML File
++++++++++++++++++
For a workflow, the ``/.dockstore.yml`` has the following general structure

.. include:: /assets/templates/workflows/barebones-.dockstore.yml

As an example, here is a filled-out ``/.dockstore.yml`` for a single workflow.  Note that the name is not present since the name field is optional when only a single workflow is involved.

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test/dockstore.cwl.json

A common pattern seen on Dockstore is GitHub repositories that store many workflows. The below ``.dockstore.yml``
has two entries for workflows. Notice that each entry uses a different name. Names are required if you want 
multiple workflows registered on Dockstore from a single GitHub repository. The names must be unique between
entries of the `workflows` array. For each unique name present, an entry will be created on Dockstore.

.. important:: Though the **name** field is optional when a ``.dockstore.yml`` has one workflow in it,
    it must be used when a ``.dockstore.yml`` has multiple workflows in it. Each entry within a ``.dockstore.yml``
    file corresponds to a unique entry on Dockstore.

.. include:: /assets/templates/workflows/barebones-multiple.dockstore.yml

For more examples, please see :doc:`our .dockstore.yml templates and examples for workflows</assets/templates/workflows/workflows>`

Tool YML File
+++++++++++++
The /.dockstore.yml file for a tool is very similiar in structure to that of a workflow. Here's a simple example:

.. code:: yaml

   version: 1.2
   tools:
      - subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test.json

For more examples, please see :doc:`our .dockstore.yml templates and examples for tools</assets/templates/tools/tools>`

Service YML File
+++++++++++++++++
A template .dockstore.yml file for registering services, with explanations in the comments, can be found in our :doc:`Service 1.2 Template </assets/templates/template>`. For more info on services and registering them, check out our :doc:`Getting Started with Services </getting-started/getting-started-with-services>`.

See Also
--------

- :doc:`Getting Started with Services </getting-started/getting-started-with-services>`
- :doc:`Getting Started with Workflows </getting-started/dockstore-workflows>`
- :doc:`Getting Started with Tools </getting-started/dockstore-tools>`
- :doc:`Other docs involving the Dockstore GitHub App </getting-started/github-apps/github-apps>`

.. discourse::
       :topic_identifier: 2240
