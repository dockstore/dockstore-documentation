=================================================================
Automatic Syncing with GitHub Apps and .dockstore.yml -- Overview
=================================================================
..
    TODO: update error handling section with info about checking lambda errors in UI https://github.com/dockstore/dockstore/issues/3530

.. include:: /getting-started/github-apps/note--gha-summary.rst

This document gives a high level overview of how Dockstore uses GitHub apps.
For extra details on configuring and using the Dockstore
GitHub App, :doc:`see our other docs on the here </getting-started/github-apps/github-apps-landing-page>`.

With the Dockstore GitHub App installed, authors do not need to manually refresh their
workflows, tools, or services on Dockstore to get the latest changes from GitHub. Dockstore will
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

Without a GitHub App, Dockstore does not know when you have modified a GitHub
repository.

When you first add a workflow to Dockstore from GitHub, Dockstore indexes the 
repository -- it reads the the relevant repository content, branches, and releases
from GitHub. But, without the Dockstore GitHub app, when you subsequently
make changes to your GitHub repo, such as pushing new commits, creating new branches
and/or publishing new releases, Dockstore is unaware of those changes. You are
responsible for going to Dockstore, finding the tool/workflow that corresponds
to the GitHub repo, and manually refreshing the tool/workflow by either clicking
the Refresh button or making an API call to the Dockstore API.

Due to the manual nature of this process, it is easy for Dockstore to get out of
sync with the linked GitHub repository if the Dockstore GitHub App is not being used.

The Dockstore GitHub App also makes it easy to register multiple workflows in the same repository quickly, as well as set up their metadata (test parameter files, authors, readmes, etc). You can even publish a workflow or set a default branch from the .dockstore.yml which can be useful for both automated systems and users registering workflows in bulk. 

How the Dockstore GitHub App works
----------------------------------

With the Dockstore GitHub App installed, the synchronization is done automatically. When
you add a new branch or release of a workflow on GitHub, Dockstore is notified,
and Dockstore updates its copy of the workflow. For example, after publishing a new release
of a workflow on GitHub, a new version of the workflow will be present in Dockstore shortly afterwards. For this to work, a .dockstore.yml file is **required** in the root directory (or inside the ``.github`` directory) of each GitHub repository you want
to associate with a workflow/tool/service on Dockstore. It should not be inside any subfolder (except ``.github``).

Simple templates for tools, workflows, and services are shown below,
as well as links to more advanced explanations of every field. For every branch/release on GitHub that has one of these files, a corresponding entry will be made on Dockstore.

Error Handling
----------------------------------
An invalid .dockstore.yml will cause errors. If we cannot read the 
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
For a workflow, the .dockstore.yml has the following general structure:

.. include:: /assets/templates/workflows/template-small.dockstore.yml
  :code: yaml

As an example, here is a filled-out .dockstore.yml for a single WDL workflow which happens to have more than one test parameter file.  Note that the name is not present since the name field is optional when only a single workflow is involved.

.. include:: /assets/templates/workflows/example-1-noname.yml
  :code: yaml

.. important:: Though the **name** field is optional when a .dockstore.yml has one workflow in it,
    it must be used when a .dockstore.yml has multiple workflows in it. Each entry within a .dockstore.yml
    file corresponds to a unique entry on Dockstore.

For more examples, including multi-workflow examples and a complete breakdown of all possible fields, please see :doc:`our .dockstore.yml templates and examples for workflows</assets/templates/workflows/workflows>`.

Tool YML File
+++++++++++++
The .dockstore.yml file for a tool is very similiar in structure to that of a workflow.

.. include:: /assets/templates/tools/template-small.dockstore.yml
  :code: yaml

See Also
--------

- :doc:`Getting Started with Services </getting-started/getting-started-with-services>`
- :doc:`Getting Started with Workflows </getting-started/dockstore-workflows>`
- :doc:`Getting Started with Tools </getting-started/dockstore-tools>`
- :doc:`Getting Started with Notebooks </getting-started/getting-started-with-notebooks>`
- :doc:`Other docs involving the Dockstore GitHub App </getting-started/github-apps/github-apps>`

.. discourse::
       :topic_identifier: 2240
