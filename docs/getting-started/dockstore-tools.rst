Register a Tool on Dockstore
############################

.. contents::
   :local:
   :depth: 2

Tutorial Goals
==============

-  Discover how to register a tool on Dockstore
-  Publish your tool

Assumptions
-----------
This document assumes you have already have a tool ready to register. You do not need to have a Dockerfile associated with it unless you are using one our legacy registration methods (more on that below).

If you followed :doc:`Getting Started With CWL </getting-started/getting-started-with-cwl>` to create a CWL tool, you will now have your ``Dockerfile`` and ``Dockstore.cwl`` in GitHub, have setup Quay.io to automatically build your Docker image, and have linked your accounts to Dockstore. This will allow you to use any of our registration methods, including legacy methods. Of course, you can always follow along with your own unique tools too, which may or may not be associated with an autobuilding Docker image.

Regardless of how you made your tool, this tutorial will assume you are using CWL. For all other languages, :doc:`please see our documentation on workflows instead </getting-started/dockstore-workflows>`.

.. note:: The WDL community does not explicitly differentiate :doc:`tools versus workflows </getting-started/intro-to-dockstore-tools-and-workflows>`. However, Dockstore allows the registration of "WDL tools" using legacy registration methods. We encourage people to :doc:`register WDLs as workflows </getting-started/dockstore-workflows>` instead.

Register Your Tool in Dockstore
-------------------------------
.. include:: /getting-started/github-apps/note--registration.rst

There are a variety of ways to get your tools into Dockstore. Users can either use GitHub App registration or our legacy registration methods.
GitHub App registration is the recommended way to register all new tools on Dockstore. GitHub App tools and tools registered using our other methods (legacy tools) are
very different from one another. Use the following questions to determine which method to use:

.. include:: /getting-started/how-to-register-work.rst

If you must use the legacy tool registration methods, then you may want to read :doc:`Dockstore Tools Overhaul </../advanced-topics/dockstore-tools-overhaul>` before continuing
to the legacy methods described below.

.. _Tool Registration With GitHub Apps:

Register Your Tool to Automatically Sync with GitHub (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. include:: /getting-started/github-apps/note--registration.rst

Dockstore has added GitHub App support for registering tools. Using GitHub Apps, Dockstore can react to changes on GitHub as they are made,
keeping Dockstore synced with GitHub automatically. You can read more about it :doc:`in our docs about the Dockstore GitHub App </getting-started/github-apps/github-apps>`, but a summary is present below.

.. include:: /getting-started/github-apps/snippet--installation.rst

Once you've installed our GitHub app on a repository or organization, you'll need to add a .dockstore.yml file to
the root directory of a branch of the repository that contains your tool. This file contains information like
tool path, test parameter file, tool name, etc. When a push is made or a tag is created on GitHub
with a .dockstore.yml, Dockstore will add that branch to the corresponding tool on Dockstore. If the
tool doesn't already exist on Dockstore, one will be created (but will not automatically be published publically). Note that a single .dockstore.yml file can describe multiple tools, if all of those tools are in the same repository.

Below is a simple example of a .dockstore.yml file
for an alignment tool to show you how easy it is to use. Note that all file paths in the file must be absolute.

.. code:: yaml

   version: 1.2
   tools:
      - subclass: CWL
        primaryDescriptorPath: /aligner.cwl
        testParameterFiles:
        - /test/aligner.cwl.json

If you had our GitHub App installed on the repository ``myorg/alignments`` and then add the above .dockstore.yml to the **develop** branch,
the following would occur.

* A **CWL** tool with the ID ``github.com/myorg/alignments`` will be created on Dockstore
* The version **develop** is added to the tool ``github.com/myorg/alignments``
* The version has the primary descriptor file set to ``/aligner.cwl``
* The version has one test parameter file: ``/test/aligner.cwl.json``

Now that your tool has been added, any time there is a push to a branch on GitHub for this repository that has a .dockstore.yml,
it is automatically updated on Dockstore! Anytime there is a deletion of a branch on GitHub that has a .dockstore.yml, the version is
removed from Dockstore.

.. include:: /getting-started/github-apps/note--addl-commit.rst

For more information on this method, as well as general troubleshooting advice, please check our :doc:`Dockstore GitHub Apps Overview </getting-started/github-apps/github-apps>` page.

Legacy Tool Registration
~~~~~~~~~~~~~~~~~~~~~~~~

.. important:: The following methods are NOT recommended and should only be used if your tool descriptor files are registered on BitBucket or GitLab.

.. include:: /getting-started/github-apps/note--legacy-dont-sync.rst

If you are using BitBucket or GitLab and would prefer not to use GitHub, or if you are using GitHub but do not wish to install our app, our legacy registration methods have you covered. Several options are available to you and described in our :doc:`legacy registration methods documentation </advanced-topics/legacy/tool-legacy-registration>`.

Sharing Your Tool
-----------------

.. this section is purposely not symmetric with its equivalent in tool-legacy-registration.rst

After you have successfully added your tool onto Dockstore and have it
synced with GitHub, Bitbucket, or GitLab, you are now ready to share your
tool with the public! Assuming that your tool has at least one valid
version, you can publish your tool for everyone to use. Simply select the
tool on the ``/my-tool`` page and click publish.

Find Other Tools
----------------

You can find tools on the Dockstore website or also through the
``dockstore tool search`` command line option.

Next Steps
----------

You can follow this basic pattern for each of your Docker-based tools.
Once registered, you can send links to your tools on Dockstore to
colleagues and use it as a public platform for sharing your tools.

Learn about :doc:`Workflows <dockstore-workflows/>` and how they differ from tools.

.. discourse::
    :topic_identifier: 1272
