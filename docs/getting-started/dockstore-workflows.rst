.. note::
    This tutorial is a continuation of :doc:`Getting Started with Dockstore Tools </getting-started/dockstore-tools>`.
    Please complete the tutorial prior to doing this one.

Workflows
=========

Tutorial Goals
--------------


-  Learn the differences between tools and workflows across Descriptor
   Languages
-  Discover how to register a workflow on Dockstore
-  Publish your workflow

This tutorial walks through the process of registering and sharing more
complex workflows which are comprised of multiple tools, strung together in some
sort of order (often a directed acyclic graph (DAG)). Workflows also
differ from tools since they are not required to define their own
environment, instead a workflow engine like
`Arvados <https://arvados.org/>`__ or
`Cromwell <https://github.com/broadinstitute/cromwell>`__ will provide
the ability to execute a CWL or WDL workflow respectively.

This tutorial does not go through the creation of a workflow and its
registration to GitHub, Bitbucket or GitLab. It assumes that you already
have a repository which contains a workflow and are now trying to register
it in Dockstore.

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

Register Your Workflow in Dockstore
-----------------------------------
There are a variety of ways to get your workflows into Dockstore. Users can either
use GitHub App registration or traditional registration. GitHub App registration is the
recommended way to register for all new workflows on Dockstore using GitHub. The traditional registration
is the legacy registration process which is less automated, and used for Bitbucket and GitLab.

.. note:: To register content on Dockstore, you must have an account on Dockstore and
   link the necessary third-party accounts. Once this is done you can register
   workflows from the My Workflows page.

.. _Registration With GitHub Apps:

Registration With GitHub Apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the newest way of getting content onto Dockstore and is by far the most automated. Using
GitHub Apps, Dockstore can react to changes on GitHub as they are made, keeping Dockstore synced
with GitHub automatically.

To install our GitHub App on either a repository or organization,
navigate to the ``/my-workflows`` page and click add workflow. Follow the steps for GitHub Apps and
you will be redirected to GitHub where you can select which repositories to install the Dockstore
GitHub app on. The process is shown in the following images.

.. figure:: /assets/images/docs/gh-app-reg-1.png
   :alt: GitHub App Registration on Dockstore

   Select Register Using GitHub Apps to get a link to our installation page

.. figure:: /assets/images/docs/gh-app-reg-2.png
   :alt: GitHub App Organizations Page

   Select an organization

.. figure:: /assets/images/docs/gh-app-reg-3.png
   :alt: GitHub App Organization Install Page

   Install our GitHub App on either all repositories in an organization or on specific repositories

Once you've installed our GitHub app on a repository or organization, you'll need to add a ``/.dockstore.yml`` file to
the root directory of a branch of the repository that contains your workflow. This file contains information like
workflow path, test parameter file, workflow name, etc. When a push is made on GitHub to a branch
with a ``/.dockstore.yml``, Dockstore will add that branch to the corresponding workflow on Dockstore. If the
workflow doesn't already exist on Dockstore, one will be created.

Below is a simple example of a ``/.dockstore.yml`` file
for an alignment workflow to show you how easy it is to use. If you are interested in using this method, please see the 
complete documentation at the :doc:`Dockstore GitHub Apps <github-apps/github-apps>` page. All paths in the file must be absolute.

.. code:: yaml

   version: 1.2
   workflows:
      - subclass: CWL
        primaryDescriptorPath: /aligner.cwl
        testParameterFiles:
        - /test/aligner.cwl.json

If you had our GitHub App installed on the repository ``myorg/alignments`` and then add the above ``/.dockstore.yml`` to the **develop** branch,
the following would occur.

* A **CWL** workflow with the ID ``github.com/myorg/alignments`` will be created on Dockstore
* The version **develop** is added to the workflow ``github.com/myorg/alignments``
* The version has the primary descriptor file set to ``/aligner.cwl``
* The version has one test parameter file: ``/test/aligner.cwl.json``

Now that your workflow has been added, any time there is a push to a branch on GitHub for this repository that has a ``/.dockstore.yml``,
it is automatically updated on Dockstore! Anytime there is a deletion of a branch on GitHub that has a ``/.dockstore.yml``, the version is
removed from Dockstore.

.. tip:: Since the workflows field is an array, this file supports multiple workflows on Dockstore stemming from
   the same repository on GitHub. This is useful if you store a lot of your workflows in the same GitHub
   repository. This is achieved setting a different value for the name field for each entry.

.. note:: The GitHub user who first adds a workflow onto Dockstore must correspond to a user on Dockstore.

.. seealso::
    - :doc:`Migrating Your Existing Workflows <github-apps/migrating-workflows-to-github-apps>` - a tutorial on converting already registered workflows
    - :doc:`Troubleshooting and FAQ <github-apps/github-apps-troubleshooting-tips>` - tips on resolving Dockstore Github App issues.

Traditional Registration
~~~~~~~~~~~~~~~~~~~~~~~~
When using Bitbucket and GitLab for you workflows, use the traditional registration.
There are two types of traditional registration: quick registration and manual registration.

There are some ways to make the traditional registration process more seamless.

- For your primary workflow descriptor, use the filename ``Dockstore.cwl``,
  ``Dockstore.wdl`` or ``nextflow.config`` depending on the descriptor language
  at the root of your repository
- For your test parameter files, use the filename ``test.json`` at the root
  of your repository
- There should be one workflow per repository

By default, Dockstore will search the root of your repository for workflow
related files. Following the above tips will help streamline the registration
process, though you can still register workflows with non-standard format by
using manual registration.

Quick Register
^^^^^^^^^^^^^^^
Quick register provides a flow that lets you browse the repositories you
have access to and quickly create workflows. You can access 
quick register by clicking the plus button on the My Workflows page. You'll
see a modal that looks like the following.

.. figure:: /assets/images/docs/quick-register-step-2.png
   :alt: Quick Register

   Use dropdowns to browse for repositories and use sliders to add as workflows

Once you've selected a Git registry and organization, you can see a list of all
available repositories that you can add to Dockstore. There are three states
the sliders can be in.

- Off - There is no matching workflow on Dockstore. One can be created.
- On - This repository already exists on Dockstore and can be deleted.
- Disabled - This repository exists on Dockstore and cannot be deleted.

If sliders are in the off state then you can turn them on to quickly register
a workflow for the repository. Once registered you can customize the workflow
path, test parameter path, descriptor language, etc. The workflow will then need to
be refreshed to get it synced up with Bitbucket/GitLab.

.. note:: Some users have multiple workflows within one Git repository, however each
   workflow entry on Dockstore only contains a single workflow. This is
   a problem as the Git path is used to uniquely identify a Dockstore workflow.
   The solution is to use manual register, defined below, which allows you to append
   a workflow name to the path.

Manual Registration of Workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In certain cases, you may wish to register workflows in a different
source code structure, especially when working with complex project
structures. For example, if you want to register two workflows from the
same repository, you can use custom workflow names. This can be seen in the form below.

You can access manual register by clicking the plus button on the My
Workflows page and selecting the custom registration. 

.. figure:: /assets/images/docs/register_workflow_manual2.png
   :alt: Manual register

   Fill out form to register a workflow

Upon successful submission of the workflow, a
synchronization call will be made to fetch all available data from the
given sources. This can be verified by going to the 'Versions' or 'Files'
tab to see what content has been found.

Sharing Your Workflow
----------------------
After you have successfully added your workflow onto Dockstore and have it
synced with GitHub, Bitbucket, or GitLab, you are now ready to share your
workflow with the public! Assuming that your workflow has at least one valid
version, you can publish your workflow for everyone to use. Simply select the
workflow on the ``/my-workflows`` page and click publish.

Next Steps
----------

You may not want to store your files directly with a service like
GitHub. Perhaps you want your descriptor files to not be public. The
solution is to use :doc:`Hosted Tools and
Workflows </getting-started/hosted-tools-and-workflows/>`.

.. discourse::
    :topic_identifier: 1292