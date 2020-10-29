DNAstack
========

Dockstore integrates with the DNAstack Workflows platform, allowing you
to launch WDL-based workflows from Dockstore in DNAstack. This works
both from within the Dockstore interface and from within the DNAstack
interface. Read more about the background for this feature at their
`blog <https://blog.dnastack.com/introducing-workflows-the-new-standard-in-cloud-bioinformatics-787a59b1d5c6>`__
but here we also offer some information on what that looks like from a
user point of view in a mini tutorial.

While browsing DNAstack
-----------------------

While working within a project within the DNAstack interface, you can
see an icon to manage the workflows associated with your project.

.. figure:: /assets/images/docs/dnastack/dnastack_projects_0.png
   :alt: dnastack project0

   dnastack project0

After clicking on that, you can see a list of the workflows associated
with your project. Click on the button on the upper right to create a
new workflow.

.. figure:: /assets/images/docs/dnastack/dnastack_projects_1.png
   :alt: dnastack project1

   dnastack project1

When creating a workflow, you can work from scratch or import a workflow
from Dockstore.

|dnastack project2| |dnastack project3|

After selecting the workflow and selecting a version, you will see the
contents of the workflow. You will need to make sure that runtime steps
specify cpu, memory, and possibly disk requirements (highlighted in an
example below) in order to successfully import into DNAstack. Note that
you may also get an error if the workflow has already been imported into
DNAstack.

.. figure:: /assets/images/docs/dnastack/dnastack_projects_4.png
   :alt: dnastack project4

   dnastack project4

If the import was successful after hitting the "Import" button you will
see the regular DNAstack interface which will let you specify inputs and
other parameters in order to run the workflow just like any other
workflow in DNAstack.

.. figure:: /assets/images/docs/dnastack/dnastack_projects_5.png
   :alt: dnastack project5

   dnastack project5

While browsing Dockstore
------------------------

When browsing WDL workflows from within Dockstore, you will see a
"Launch-With" icon on the right.

.. figure:: /assets/images/docs/wdl_launch_with.png
   :alt: WDL workflow

   WDL workflow

If not logged into DNAstack, you will be prompted to login. Otherwise or
after login, you will be presented with the following screen.

.. figure:: /assets/images/docs/dnastack/dnastack_from_dockstore2.png
   :alt: WDL workflow import

   WDL workflow import

You will need to pick a version of your workflow to import and a project
to import it into. Then hit the button to "Import" and continue from
within the DNAstack interface to run your workflow. Note that as with
the above approach, you will want to double-check that the workflow
specifies a runtime environment (docker, cpu, memory, and disks) if you
have trouble importing the workflow and that the workflow has not been
imported before.

.. _dnastack-limitations:

Limitations
-----------

1. While we support launching of WDL workflows, tools as listed in
   Dockstore are currently not supported.
2. DNAstack does not currently support HTTP(S) or file-path based
   imports. Importing a workflow with those imports will result in an
   error. See `cromwell imports
   docs <https://cromwell.readthedocs.io/en/develop/Imports/>`__ for
   more info about imports.

See Also
--------

-  :doc:`AnVIL Launch With</launch-with/anvil-launch-with>`
-  :doc:`CGC Launch With</launch-with/cgc-launch-with>`
-  :doc:`DNAnexus Launch With </launch-with/dnanexus-launch-with>`
-  :doc:`Terra Launch With </launch-with/terra-launch-with>`

.. discourse::
    :topic_identifier: 1309

.. |dnastack project2| image:: /assets/images/docs/dnastack/dnastack_projects_2.png
.. |dnastack project3| image:: /assets/images/docs/dnastack/dnastack_projects_3.png
