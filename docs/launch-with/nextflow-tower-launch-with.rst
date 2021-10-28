Nextflow Tower
==============

Dockstore integrates with the `Nextflow Tower <https://tower.nf>`__ platform,
allowing you to launch Nextflow-based workflows from Dockstore in Nextflow Tower.

Exporting into Nextflow Tower
-----------------------------

When browsing Nextflow workflows from within Dockstore, there is a
"Launch with Nextflow Tower" button on the right.

.. figure:: /assets/images/docs/nextflow_tower_launch_with.png
   :alt: Nextflow workflow
   

Select the version of the workflow you want to run in Nextflow Tower, then click on the Nextflow Tower
button. This will redirect you to Nextflow Tower in a new browser tab.

If not already logged into Nextflow Tower, you will be prompted to login.

You will then be prompted to configure your pipeline for launching. The pipeline and
the revision number values will have already been filled in with values supplied
by Dockstore. Please follow the Nextflow Tower instructions for configuring the other values and launching
your pipeline.

.. figure:: /assets/images/docs/nextflow_tower_from_dockstore.png
   :alt: Nextflow Tower

.. _nextflow-limitations:

Limitations
-----------

Nextflow Tower runs a workflow by cloning its git repository and checking out the specified branch. Unlike other launch-with partners, it does not
fetch the workflow content directly from Dockstore. The Nextflow version on Dockstore can be out of sync with the version on GitHub, Bitbucket, or GitLab.
When determining the exact workflow contents being run on Nextflow Tower, refer to the git repository.


.. discourse::
    :topic_identifier: 4406
