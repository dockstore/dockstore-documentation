.. note::
    This tutorial is a continuation of :doc:`Getting Started with Dockstore Tools </getting-started/dockstore-tools>`.
    Please complete the tutorial prior to doing this one.

Workflows
=========

Tutorial Goals
--------------


-  Learn the differences between tools and workflows across Descriptor
   Languages
-  Register a workflow on Dockstore
-  Publish your workflow

This tutorial walks through the process of registering and sharing more
complex workflows which are comprised of multiple tools (whether they
are registered on Dockstore or not). Workflows as defined via the
Dockstore are a composition of multiple tools, strung together in some
sort of order (often a directed acyclic graph (DAG)). Workflows also are
different from tools since they are not required to define their own
environment, instead a workflow engine like
`Arvados <https://arvados.org/>`__ or
`Cromwell <https://github.com/broadinstitute/cromwell>`__ will provide
the ability to execute a CWL or WDL workflow respectively.

Comparison of Tools and Workflows Across Descriptor Languages
-------------------------------------------------------------

When Dockstore was created, CWL was the first descriptor language we
supported. It had a very clear distinction between a Tool and a
Workflow. Descriptor languages like WDL and Nextflow are less clear
about this distinction so we briefly describe our working definitions
below:

+------------------------+------------------------------------------+-----------------------------------------------+
| Language               | Tool                                     | Workflow                                      |
+========================+==========================================+===============================================+
| CWL                    | - Class: CommandLineTool                 | - Class: Workflow                             |
+------------------------+------------------------------------------+-----------------------------------------------+
| WDL                    | - A single task with Docker image        | - >1 task                                     |
|                        | - A workflow section that runs the task  | - A workflow section that connects the tasks  |
|                        | - An associated Docker image             |                                               |
+------------------------+------------------------------------------+-----------------------------------------------+
| Nextflow               | - N/A                                    | - Any valid nextflow workflow                 |
|                        |                                          |                                               |
+------------------------+------------------------------------------+-----------------------------------------------+


Prepare Your Workflow for Dockstore
-----------------------------------
This tutorial does not go through the creation of a workflow and its
registration to GitHub, Bitbucket or GitLab. It assumes that you already
have a repository which contains a workflow and are now trying to register
it in Dockstore. There are some ways to make the registration process more
seamless.

- For your primary workflow descriptor, use the filename ``Dockstore.<ext>``
  at the root of your repository
- For your test parameter files, use the filename ``test.json`` at the root
  of your repository
- There should be one workflow per repository

By default, Dockstore will search the root of your repository for workflow
related files. Following the above tips will help streamline the registration
process, though you can still register workflows with non-standard format.

Register Your Workflow in Dockstore
-----------------------------------
There are a variety of ways to get your workflows into Dockstore. There are two
types of quick registration and one type of manual registration. These quick
methods create workflow stubs, which are simply workflows that have not yet
been confirmed to be real workflows. You can individually refresh a workflow
stub that you identify as a real workflow in order to start pulling in workflow
files and other data.

To register content on Dockstore, you must have an account on Dockstore and
link the necessary third-party accounts. Once this is done you can register
workflows from the My Workflows page.

Quick Registration via the Web UI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quick registration is best used for workflows that follow the simple format
that Dockstore suggests. It can still be used if your workflows are
non-standard format, however there can be some drawbacks.

Some users have multiple workflows within one Git repository, however each
workflow entry on Dockstore only contains a single workflow. This is
a problem as the Git path is used to uniquely identify a Dockstore workflow.
The solution to this is to allow users to specify a workflow name that is
appended to the Dockstore path. This would allow them to have multiple
Dockstore workflows with the same Git repository. Quick registration does
not allow you to create workflows with workflow names.
To do that you must do manual registration, which is described later.

Refresh All
^^^^^^^^^^^
Refresh all will look at all of your third-party accounts and do the following:

- Create stub workflows for all git repositories which do not exist on
  Dockstore
- Refersh all workflows that have been converted from stub to full workflows
- Add user to any workflows that exist on Dockstore that they should have
  access to

To refresh all, select the refresh all icon button on the left side of the
page.

.. note:: For existing organizations, you can select `Refresh Organization`
          to perform a refresh all on a specific organization.

One drawback of refresh all is that it creates a stub for every single
repository that you have access to, whether or not it contains a workflow.
The following approach is a bit less automated but allows for more control.

Quick Register
^^^^^^^^^^^^^^
Quick register provides a flow that lets you browse the repositories you
have access to an quickly create standard stub workflows. The benefit of
this approach is that you get some automation without having lots of
stubs created.

You can access quick register by clicking the plus button on the My
Workflows page. The flow of this process is shown in the screenshots
below.

.. figure:: /assets/images/docs/quick-register-step-1.png
   :alt: Quick Register step 1

   Choose the quick register option in the Register workflow wizard

.. figure:: /assets/images/docs/quick-register-step-2.png
   :alt: Quick Register step 2

   Use dropdowns to browse for repositories and use sliders to add as workflows

Once you've selected a git registry and organization, you can see a list of all
available repositories that you can add to Dockstore. There are three states
the sliders can be in.

- Off - There is no matching workflow on Dockstore.
- On - This repository already exists on Dockstore and can be deleted.
- Disabled - This repository exists on Dockstore and cannot be deleted.

If sliders are in the off state then you can turn them on to quickly register
a stub workflow for the repository.

Manual Registration of Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In certain cases, you may wish to register workflows in a different
source code structure, especially when working with complex project
structures. For example, if you want to register two workflows from the
same repository.

You can access manual register by clicking the plus button on the My
Workflows page. The flow of this process is shown in the screenshots
below.

.. figure:: /assets/images/docs/quick-register-step-1.png
   :alt: Manual register step 1

   Choose the manual register option in the Register workflow wizard


.. figure:: /assets/images/docs/register_workflow_manual2.png
   :alt: Manual register step 2

   Fill out form to register a workflow

Source Code Provider allows you to choose between GitHub, BitBucket, and
GitLab (your respective accounts for these third party repositories need
to be linked to your Dockstore account). The Source Code Repository
field must be filled out and is in the format ``namespace/name`` (the
two paths may differ). The Workflow (descriptor) path and test parameter
path are relative to the root of the Source Code Repository (and must
begin with '/'). These will be the default locations to find their
corresponding files, unless specified otherwise in the tags. The
Workflow Name is an optional 'suffix' appended to the Dockstore path. It
allows for two workflows to share the same Git paths; the Workflow Name
uniquely distinguishes workflow repositories in Dockstore.

Upon successful submission and publishing of the workflow, a
resynchronization call will be made to fetch all available data from the
given sources.

The user may then browse to the 'Versions' tab of the new container,
where tags (corresponding to GitHub/Bitbucket/GitLab tag names) may be
edited.

The fields in the form should correspond to the actual values on
GitHub/Bitbucket/GitLab in order for the information to be useful to
other users. Selecting ``Hidden`` will prevent the tag from appearing in
the public listing of tags for the workflow.

CLI Client
~~~~~~~~~~

The ``dockstore`` command line has several options. When working with
workflows, use ``dockstore workflow`` to get a full list of options. We
recommend you first use ``dockstore workflow refresh`` to ensure the
latest GitHub, Bitbucket, and GitLab information is indexed properly.

You can then use ``dockstore workflow publish`` to see the list of
available workflows you can register with Dockstore and then register
them. This is for you to publish workflows with the simplest structure.
For now, use manual registration if your workflow has a different
structure. The key is that workflows you wish to (simply) publish have
the following qualities:

1. public
2. at least one valid tag. In order to be valid, a tag has to:

   -  have the reference be linked a corresponding ``Dockstore.cwl`` or
      ``Dockstore.wdl`` hosted at the root of the repository

The ``dockstore workflow manual_publish`` command can be used to
manually register a workflow on GitHub, Bitbucket or GitLab. Its usage
is outlined in the manual\_publish help menu.

Find Other Workflows
--------------------

You can find tools on the Dockstore website or also through the
``dockstore workflow search`` command line option.

Next Steps
----------

You may not want to store your files directly with a service like
GitHub. Perhaps you want your descriptor files to not be public. The
solution is to use :doc:`Hosted Tools and
Workflows </getting-started/hosted-tools-and-workflows/>`.

.. discourse::
    :topic_identifier: 1292