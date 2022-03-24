Templates
=========

* :doc:`.dockstore.yml templates for registering services </assets/templates/services/services>`
* :doc:`.dockstore.yml templates for registering tools </assets/templates/tools/tools>`
* :doc:`.dockstore.yml templates for registering workflows </assets/templates/workflows/workflows>`

Not sure if you are working with a workflow, a tool, or a service? :doc:`Check out our introduction on the main differences between them. </getting-started/intro-to-dockstore-tools-and-workflows>`

Tips and tricks
---------------
* Make sure your file is saved as ``.dockstore.yml``, not ``dockstore.yml`` or ``.dockstore.yaml``
* Put the ``.dockstore.yml`` file in the top of your repo or inside ``.github``
* You can use a single ``.dockstore.yml`` file to register multiple tools and workflows, provided they are all in the same repo as the ``.dockstore.yml`` file
* A workflow registered with via a ``.dockstore.yml`` file is not fundamentally different than a workflow registered in another method, other than the fact that the ``.dockstore.yml`` version will be kept up-to-date automatically -- but a ``.dockstore.yml`` registered tool is different from tools registered in other methods (:ref:`see this table for more information <dockstore yml tools vs old school tools>`)
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

    .dockstore.yml templates for registering services </assets/templates/services/services>
    .dockstore.yml templates for registering tools </assets/templates/tools/tools>
    .dockstore.yml templates for registering workflows </assets/templates/workflows/workflows>