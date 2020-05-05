Automatic Syncing with GitHub Apps and .dockstore.yml
======================================================

Overview
--------

This document gives a high level overview of how Dockstore uses GitHub apps.
For extra details on configuring and using the Dockstore
GitHub App with workflows or services, please see either
:doc:`Getting Started with Workflow <./dockstore-workflows>` or
:doc:`Getting Started with Services <./getting-started-with-services>`.

With the Dockstore GitHub App installed, authors do not need to manually refresh their
workflows/services on Dockstore to get the latest changes from GitHub. Dockstore will
automatically update whenever the corresponding repository is updated on GitHub.

What are GitHub Apps?
---------------------

`GitHub apps <https://developer.github.com/apps>`_ are a GitHub feature used to
improve the interaction between external applications and GitHub. Users can
grant a GitHub app specific permissions on the repos and/or
organizations of their choosing. When events occur on the GitHub repos, e.g.,
creating a new release, the GitHub App issues notifications.

Why have a Dockstore GitHub App?
--------------------------------

Without a GitHub App, Dockstore does not know when you have modified a GitHub
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
Dockstore shortly afterwards.

For this to work, a ``/.dockstore.yml`` file is required in the root directory of each GitHub repository you want
to associate with a workflow on Dockstore. A template for both workflows and services are shown below,
along with explanations for each field. For every branch/release on GitHub that has one of these files, a corresponding entry
will be made on Dockstore.

Workflow YML File
++++++++++++++++++
For a workflow, the ``/.dockstore.yml`` has the following general structure

.. code:: yaml

   version: 1.2
   workflows:
      - name: <String>
        subclass: <CWL | WDL | NFL | GALAXY>
        primaryDescriptorPath: <String>
        testParameterFiles: <String Array>

version
    The version of the .dockstore.yml schema. Currently at 1.2.
workflows
    An array of workflows. Each element corresponds to a workflow on Dockstore.
name (optional)
    The optional workflow name that is used to uniquely identify workflows in repositories with multiple workflows.
    **Each workflow listed must have a unique name.**
subclass
    The descriptor language used for the workflow. Supported values include CWL, WDL, NFL (Nextflow), and GALAXY.
primaryDescriptorPath
    The absolute path to the primary descriptor file in the Git repository
testParameterFiles (optional)
    An array of absolute paths to test parameter files in the Git repository.

Ex. .dockstore.yml with a single workflow

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test/dockstore.cwl.json

The above ``.dockstore.yml`` is for a single workflow. Note that the name is not present since it is optional.

Ex. .dockstore.yml with multiple workflows

.. important:: The **name** field is an optional field used when a repository has multiple workflows in it that a user wants to register
    as separate entries on Dockstore. Each entry within a ``.dockstore.yml`` file corresponds to a unique entry on Dockstore.

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

A common pattern seen on Dockstore is GitHub repositories that store many workflows. The above ``.dockstore.yml``
has two entries for workflows. Notice that each entry uses a different name. Names are required if you want 
multiple workflows registered on Dockstore from a single GitHub repository. The names must be unique between
entries of the `workflows` array. For each unique name present, an entry will be created on Dockstore.

Service YML File
+++++++++++++++++
TODO

Migrating Existing Workflows to use GitHub Apps
-------------------------------------------------
If you have already registered GitHub workflows on Dockstore using our old method which required you to refresh, you are still able to use GitHub Apps!
The migration process is fairly straightforward. First, make sure to install our GitHub App onto the repository for the workflow that you want to migrate.
Next, create a ``/.dockstore.yml`` file and push it to a branch on your GitHub repo, making sure that the name field matches the existing workflowname.
If your workflow did not have a workflowname set, simply exclude the field. It is very important that these names match, or else Dockstore won't know which
workflow to associate the ``/.dockstore.yml`` with.

The pushing of a branch with a valid ``/.dockstore.yml`` should trigger Dockstore to convert your workflow into a GitHub App workflow! New versions will be added/updated/deleted
as if the workflow was originally added using GitHub Apps.  Existing branches will persist, and you can even individually refresh them on the versions tab of the workflow.
You can convert these existing workflows to use GitHub Apps by adding a valid ``/.dockstore.yml`` to the corresponding branches on GitHub.

Error Handling
----------------------------------
Since Dockstore relies on GitHub to tell us when changes have been made on GitHub, there are chances that the message gets lost or delayed.
Typically, Dockstore reacts within seconds of a change being made on GitHub, however service disruptions can delay this to a few minutes.
If a message were to get lost, unfortunately you will need to push to GitHub again. Currently, there is no way to tell on Dockstore whether
a GitHub message was delayed or lost. We recommend waiting a few minutes and then trying to push again. This will hopefully be changed in the near future.

Another error that could occur is that we received the message from GitHub, however the ``/.dockstore.yml`` is invalid. If we cannot read the 
file, then we do not know which workflow or service to associate the error with. For now, please ensure that your file is a valid YAML file and
compare it with our examples/documentation to confirm that you filled it in correctly. In the future we plan to have a system in place where
users can keep track of these GitHub events and resulting action taken by Dockstore, even if the message was succesfully handled.

Another possible issue is that we received the message from GitHub, but the user who triggered the message event is not registered on Dockstore with
the corresponding GitHub account. This is only an issue if the workflow or service does not already exist on Dockstore. When creating new workflows and
services, we need to be able to associate them with a user. If the workflow or service already exists on Dockstore, then this error will not occur and the 
version will be properly added/updated/deleted on Dockstore.

As always, you can reach out to our team on our `discussion forum <https://discuss.dockstore.org/>`_ to discuss any issues you are facing.

See Also
--------

- :doc:`Getting Started with Services <./getting-started-with-services>`
- :doc:`Getting Started with Workflows <./dockstore-workflows>`

.. discourse::
       :topic_identifier: 2240
