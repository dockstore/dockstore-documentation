DNAnexus
========

Dockstore integrates with the DNAnexus platform, allowing you to launch
WDL-based workflows from Dockstore in DNAnexus. Here is some information
on what that looks like from a user point of view in a mini tutorial.

Exporting into DNAnexus
-----------------------

When browsing WDL workflows from within Dockstore, you will see a
"Launch with DNAnexus" button on the right. The currently selected
version of the workflow will be exported.

.. figure:: /assets/images/docs/wdl_launch_with.png
   :alt: WDL workflow

   WDL workflow

If not logged into DNAnexus, you will be prompted to login. Otherwise,
or after login, you will be presented with the following screen.

.. figure:: /assets/images/docs/dnanexus/dnanexus_from_dockstore2.png
   :alt: WDL workflow import

   WDL workflow import

You will need to pick a folder to export it into. You can either select
a folder from an existing project, or you can create a new project.

Then hit the "Submit" button and continue from within the DNAnexus
interface to configure and run your workflow.

Limitations
-----------

1. While we support launching of WDL workflows, tools as listed in
   Dockstore are currently not supported.
2. Only the WDL language is supported.

See Also
--------

-  :doc:`AnVIL Launch With</launch-with/anvil-launch-with>`
-  :doc:`CGC Launch With</launch-with/cgc-launch-with>`
-  :doc:`DNAstack Launch With </launch-with/dnastack-launch-with>`
-  :doc:`Terra Launch With </launch-with/terra-launch-with>`

.. discourse::
    :topic_identifier: 1535
