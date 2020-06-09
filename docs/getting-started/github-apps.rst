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

For this to work, a ``/.dockstore.yml`` file is **required in the root directory of each GitHub repository** you want
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
        subclass: <CWL | WDL | NFL | GXFORMAT2>
        primaryDescriptorPath: <String>
        testParameterFiles: <String Array>

version
    The version of the .dockstore.yml schema. Currently at 1.2.
workflows
    An array of workflows. Each element corresponds to a workflow on Dockstore.
name (optional)
    The optional workflow name for a workflow. If using a ``/.dockstore.yml`` with multiple workflows,
    this field is required to uniquely identify workflows in the repository.
    **Each workflow listed must have a unique (or no) name.**
subclass
    The descriptor language used for the workflow. Supported values include CWL, WDL, NFL (Nextflow), and GXFORMAT2 (Galaxy).
primaryDescriptorPath
    The absolute path to the primary descriptor file in the Git repository.
testParameterFiles (optional)
    An array of absolute paths to test parameter files in the Git repository.

Ex. /.dockstore.yml with a single workflow

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /Dockstore.cwl
        testParameterFiles:
            - /test/dockstore.cwl.json

The above ``/.dockstore.yml`` is for a single workflow. Note that the name is not present since it is optional.

Ex. /.dockstore.yml with multiple workflows

.. important:: Though the **name** field is optional when a ``.dockstore.yml`` has one workflow in it,
    it must be used when a ``.dockstore.yml`` has multiple workflows in it. Each entry within a ``.dockstore.yml``
    file corresponds to a unique entry on Dockstore.

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
For a service, the ``/.dockstore.yml`` has this general structure for version 1.2:

.. code:: yaml

    version: 1.2
    service:
      subclass: <DOCKER_COMPOSE | KUBERNETES | HELM | SWARM | NOT_APPLICABLE>
      name: <String>
      author: <String>
      description: <String>

      files: <String Array>

      scripts:
        start: <String>
        postprovision: <String>
        port: <String>
        stop: <String>

      environment:
        <environmentVariableName>:
            default: <String | Integer>
            description: <String>

      data:
        <datasetName>:
            targetDirectory: <String>
            files:
                <name>:
                    description: <String>

version
    The version of the .dockstore.yml schema which is currently at 1.2.
service
    Used to describe a single service.
subclass
    Indicates which container system will be used for your service.
name
    Optional name for your service.
author
    Optional author for your service.
description
    Optional description for your service
files
    An array of files Dockstore will index from your GitHub repo. Wildcards are not supported.
scripts
    This section description the scripts that the service launcher will execute. Can only be used with the following keys: preprovision, prestart, start, postprovision, port, healthcheck, and stop. They can filled with either the name of the script file or the commands that need to be ran for each portion.
preprovision
    (Optional) Invoked before any data has been downloaded and some initialization is required.
prestart
    (Optional) Executed after data has been downloaded locally, but before service has started (see the data section)
start
    Starts up the service.
postprovision
    (Optional) After the service has been started. This might be invoked multiple times, e.g., if the user decides to load multiple sets of data.
port
    (Optional) Which port the service is exposing. This provides a generic way for the tool to know which port is being exposed, e.g., to reverse proxy it.
healthcheck
    (Optional) exit code of 0 if service is running normally, non-0 otherwise.
stop
    (Optional) stops the service
environment
    This section describes environment variables that the launcher is responsible for passing to any scripts that it invokes. The names must be valid environment variable names. Users can specify the values of the parameters in the input parameter JSON (see below). These variables are service-specific, i.e., the service creator decides what values, if any, to expose as environment variables. For every environment variable, you must give it a name and you can optionally give them a default value and description.
data
    This section describes data that should be provisioned locally for use by the service. The service launcher is responsible for provisioning the data. You can create as many keys as you need where each key is the name of a dataset. For every key you create, you must give a target directory (path will be relative) to indicate where the files should be downloaded to. You must also give an array of files as a key and provide the name of each file. You can optionally provide a description of each file.

It's important to note that we originally released our services tutorial using version 1.1 of the ``/.dockstore.yml`` file. For more info on
services and registering them, check out our :doc:`Getting Started with Services <./getting-started-with-services>` which has been updated to use 1.2.


Error Handling
----------------------------------
Since Dockstore relies on GitHub to tell us when changes have been made on GitHub, there are chances that the message gets lost or delayed.
Typically, Dockstore reacts within seconds of a change being made on GitHub, however service disruptions can delay this to a few minutes.
If a message were to get lost, unfortunately you will need to push to GitHub again. Currently, there is no way to tell on Dockstore whether
a GitHub message was delayed or lost. We recommend waiting a few minutes and then trying to push again. This will be changed in the future.

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
