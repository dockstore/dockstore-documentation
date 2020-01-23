AnVIL
=====

Dockstore integrates with the AnVIL, the Analysis, Visualization, and Informatics Lab-space platform,
allowing you to launch WDL-based workflows from Dockstore in AnVIL. Here is some information on
what that looks like from a user point of view in a mini-tutorial.

Exporting into AnVIL
--------------------

When browsing WDL workflows from within Dockstore, you will see a
"Launch with AnVIL" button on the right. The currently selected version
of the workflow will be exported.

.. figure:: /assets/images/docs/wdl_launch_with.png
   :alt: WDL workflow

   WDL workflow

If not logged into AnVIL, you will be prompted to login. Otherwise, or
after login, you will be presented with the following screen.

.. figure:: /assets/images/docs/terra/terra_from_dockstore2.png
   :alt: WDL workflow import

   WDL workflow import

You will need to pick a workspace to export it into. You can either
select an existing workspace or create a new one.

Then hit the "Import" button and continue from within the Terra
interface to configure and run your workflow.

Note that you may want to double-check that the workflow specifies a
runtime environment (docker, cpu, memory, and disks) to avoid using
limiting defaults on AnVIL. See more
`here <https://cromwell.readthedocs.io/en/stable/wf_options/Overview>`__.

Limitations
-----------

1. While we support launching of WDL workflows, tools as listed in
   Dockstore are currently not supported.
2. AnVIL does not currently support file-path based imports. Importing a
   workflow with file-based imports will result in error. See the
   `converting file-based imports
   doc <../end-user-topics/language-support.html#converting-file-path-based-imports-to-public-http-s-based-imports-for-wdl>`__
   for more info.
3. Only the WDL language is supported.

See Also
--------

-  :doc:`CGC Launch With <../launch-with/cgc-launch-with/>`
-  :doc:`DNAnexus Launch With <../launch-with/dnanexus-launch-with/>`
-  :doc:`DNAstack Launch With <../launch-with/dnastack-launch-with/>`
-  :doc:`Terra Launch With <../launch-with/terra-launch-with/>`

.. discourse::
    :topic_identifier: 1841

