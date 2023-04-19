Templates
=========

* :doc:`.dockstore.yml templates for registering services </assets/templates/services/services>`
* :doc:`.dockstore.yml templates for registering tools </assets/templates/tools/tools>`
* :doc:`.dockstore.yml templates for registering workflows </assets/templates/workflows/workflows>`

Not sure if you are working with a workflow, a tool, or a service? :doc:`Check out our introduction on the main differences between them. </getting-started/intro-to-dockstore-tools-and-workflows>`

Tips and tricks
---------------
* This form of registration is only available to workflows, tools, and services that are hosted on GitHub
* Make sure your file is saved as ``.dockstore.yml``, not ``dockstore.yml`` or ``.dockstore.yaml``
* Put the .dockstore.yml file in the top of your repo or inside ``.github/``
* If you have multiple workflows/tools/services in a single GitHub repository, each one needs a unique ``name``, and it's a good idea (but not strictly required) to give each one a unique ``readMePath`` too. 
* The first line of a .dockstore.yml file references the version of .dockstore.yml syntax being used, not the version/tag of the workflow/tool/service it describes
* You can use a single .dockstore.yml file to register multiple tools and workflows, provided they are all in the same repo as the .dockstore.yml file
* A **workflow** registered with via a .dockstore.yml file is not fundamentally different than a workflow registered in another method, other than the fact that the .dockstore.yml version will be kept up-to-date automatically -- but a .dockstore.yml registered **tool** is different from tools registered in other methods (:ref:`see this table for more information <dockstore yml tools vs old school tools>`)

Examples of the filters field
-----------------------------
* The ``filters:`` field allows for limiting which GitHub `tags <https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-commits/managing-tags>`_ and `branches <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches>`_ appear on a Dockstore entry. Regex can be used here.
* You can use this regex pattern to include all tags but no branches:

.. code:: yaml

    filters:
        tags:
            - /.*/

* You can use this regex pattern to include tags that only start with ``localaligner`` and the branches named ``develop`` and ``master``:

.. code:: yaml
    
    filters:
        branches:
            - develop
            - master
        tags:
            - /localaligner\/.*/

.. toctree::
    :hidden:

    .dockstore.yml templates for registering tools </assets/templates/tools/tools>
    .dockstore.yml templates for registering workflows </assets/templates/workflows/workflows>
    .dockstore.yml templates for registering services </assets/templates/services/services>

.. discourse::
    :topic_identifier: 6490
