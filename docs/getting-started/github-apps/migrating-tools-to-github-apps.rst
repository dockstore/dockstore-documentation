Migrating Your Existing Tools to Use GitHub Apps
======================================================

.. include:: /getting-started/github-apps/note--vocabulary.rst

Dockstore 1.12 provides users with a way to keep their tools automatically updated (instead of needing to manually refresh) by using GitHub apps. Registering a new tool with GitHub Apps is very similar to registering a new workflow with GitHub Apps.

.. _dockstore yml tools vs old school tools:

Before deciding to migrate your existing tools, consider the following differences between an existing Dockstore tool and a GitHub App tool:

+------------------------+------------------------------------------+-------------------------------------------------+
| Differences            | Legacy Tool                              | GitHub App Tool                                 |
+========================+==========================================+=================================================+
| Use case               |   - User owns the image                  | - User doesn't need to own the image            |
|                        |   - Dockerfile required                  | - Dockerfile not required                       |
+------------------------+------------------------------------------+-------------------------------------------------+
| Versioning             | Based on image's tags                    | Based on GitHub repository's branches/tags      |
+------------------------+------------------------------------------+-------------------------------------------------+
| Tool Path              | Docker image location                    | GitHub repository location                      |
+------------------------+------------------------------------------+-------------------------------------------------+
| Languages              | Supports CWL and WDL tools               | Only supports CWL                               |
+------------------------+------------------------------------------+-------------------------------------------------+

If you're familiar with the process of :doc:`migrating your existing workflows to use GitHub Apps <migrating-workflows-to-github-apps>`, note that the migration process for tools is different 
because of these fundamental differences between existing tools and GitHub App tools. The migration process for tools will not convert your existing tool into a GitHub App tool.
Instead, you will be creating a new GitHub App tool, then either deleting your existing tool or providing a link to your new GitHub App tool from your old tool. You may wish to consider
the latter if you have users that have bookmarked it or if you have papers that link to the old tool. :ref:`More information on that here <keeping old tool around>`.

Install the Dockstore GitHub App
--------------------------------
.. include:: /getting-started/github-apps/snippet--installation.rst

Creating a .dockstore.yml File
-------------------------------

The next step is to create a .dockstore.yml file. We'll cover a very straightforward example
first, but depending on how you configured the tool during registration and whether your GitHub repository houses multiple tools published on Dockstore,
there will be additional steps to writing your .dockstore.yml file.

Let's say we have the following CWL tool registered on Dockstore that came from this `repository <https://github.com/kathy-t/dockstore-tool-helloworld>`__ and you would like to convert the master branch.

.. figure:: /assets/images/docs/single-tool-to-migrate.png
   :alt: Tool to Migrate

As noted in our other documentation, create a .dockstore.yml file in the root directory of the branch you want to migrate (in this example, it's the master branch) in your repository. The file should look like the following:

.. include:: /assets/templates/tools/example-1-noname.yml
  :code:

The information above was filled out using the following:

- ``subclass`` is based on the descriptor language your tool is described in. In this case, the tool is described in CWL.
- ``primaryDescriptorPath`` is the path to the CWL descriptor file.
- ``testParameterFiles`` is the path to any test parameter files.

The ``name`` Field
~~~~~~~~~~~~~~~~~~

If you have more than one tool in the same repository, the ``name`` field must be filled out for each individual tool's section in your .dockstore.yml file. This is to ensure that the tool paths are unique -- as mentioned in the table above, tool paths are based upon the GitHub repository, so tools without a name in the same repository would have the same path, which we want to avoid. (Strictly speaking, you can leave one of the tools' name fields blank if you would like, but make sure that all other tools in your repository have a name.)

If you registered your tool using the Web UI, you may have filled out the ``Tool Name`` field shown in the picture below.

.. figure:: /assets/images/docs/tool-name-field.png
   :alt: Tool name field
   :width: 60 %

This field is required when you want to register multiple tools from the same repo or provide multiple languages for your tool, but you may have filled it out for other reasons. 
To check if the tool you want to migrate has a tool name, select the tool's entry on Dockstore and look at the title on top. The title consists of:
``<image registry>/<organization name>/<repository name>/<optional tool name>:<version name>``

If you see a tool name inserted, you must include the name field in your .dockstore.yml file for the transfer to work correctly.

.. include:: /assets/templates/tools/example-2-name.yml
  :code:

If you have multiple tools registered on Dockstore that stem from the same GitHub repo, a single .dockstore.yml can be used to convert them. For examples of this, check out our :doc:`template .dockstore.yml files </assets/templates/tools/tools>`

.. decided to remove /assets/images/docs/github-apps-multiple-tools.png and /assets/images/docs/github-apps-multiple-tools-with-name.png as the filenames within them are a little confusing; may be worth doing something like that but with globalAligner and localAligner later

Your New Entry in Dockstore
---------------------------

Once you've adding a .dockstore.yml to the desired branch of your repository and installed the app, you should see a new tool appear on your ``/my-tools`` page. The tool path will start with ``github.com`` and 
you should see that the ``Tool Information`` section looks a bit different from your existing tool.

.. figure:: /assets/images/docs/github-app-tool.png
   :alt: New GitHub App tool

The mode is ``Automatically synced via GitHub App`` instead of one of our three build modes, and information about paths and your Docker Image is no longer included.
You are also not able to refresh or restub the new GitHub App tool. Since you can't refresh the entire tool anymore, **new** versions from GitHub (releases/branches) that you want to add to Dockstore must have a .dockstore.yml file.

.. _keeping old tool around:

Archiving or Deleting Your Existing Tool
----------------------------------------

If you look on the left hand side bar, you should see that your old tool still exists. Your new GitHub App tool will start with ``github.com``, and your old tool will start with
the Docker registry, which is ``quay.io`` in this case.

.. figure:: /assets/images/docs/old-and-new-tool.png
   :alt: Old and new tools
   :width: 50 %

At this point, you must decide whether you want to keep your old tool around. You may want to keep it if you want to preserve the link to the tool. For example, you may choose to keep the tool if this tool was linked in a research paper
and other people might visit the tool's page.

If you need to keep your old tool, then we recommend that you link to your new entry. You could do this in multiple ways:

* Add a short description to your GitHub repository's README indicating where the new GitHub App tool can be found on Dockstore.  You may also indicate whether your old tool will be kept up to date on Dockstore through refresh. Once a short description has been added, navigate to your old tool's page and click ``Refresh`` to update your tool's description with the new information. Reverting that commit and then not Refreshing the old tool from then on will keep that notice in the tool's description on Dockstore.
* Create a new version/branch that has the new link in the readme and hide that version in the new Dockstore entry so that it only appears in the old entry
* Set "topic" to "manual" in your old entry and include the URL of your new entry within the text field.

.. figure:: /assets/images/docs/edit_topic_to_link_to_new_entry.png
   :alt: Screenshot of an old tool's entry topic field linking to a new one, with the topic field circled in red

If you do not need to keep your old tool, you can simply delete it. 

To delete your old tool, navigate to the tool on your ``My Tools`` page. Published tools cannot be deleted. If your tool is published, press the ``Unpublish`` button in the upper right corner.

.. figure:: /assets/images/docs/unpublish-tool-button.png
   :alt: Unpublish tool button

Once your tool is unpublished, you should see that the ``Delete`` button is enabled. Press the ``Delete`` button to delete your tool.

.. figure:: /assets/images/docs/delete-tool-button.png
   :alt: Delete tool button

.. seealso::
    :doc:`Troubleshooting and FAQ <github-apps-troubleshooting-tips>` - tips on resolving Dockstore GitHub App issues.

.. discourse::
    :topic_identifier: 6486
