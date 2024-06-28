Seqera Platform
===============

Dockstore integrates with the `Seqera Platform <https://seqera.io/>`__,
allowing you to launch Nextflow-based workflows from Dockstore in a variety of
cloud environments.

Exporting into Seqera Platform
------------------------------

When browsing Nextflow workflows from within Dockstore, there is a
"Launch with Seqera" button on the right.

.. figure:: /assets/images/docs/seqera_launch_with.png
   :alt: Nextflow workflow in Dockstore
   

Select the version of the workflow you want to run in Seqera Platform, then click on the Seqera
button. This will redirect you to Seqera Platform in a new browser tab.

If not already logged into Seqera Platform, you will be prompted to login.

You will then be prompted to configure your pipeline for launching. The pipeline and
the revision number values will have already been filled in with values supplied
by Dockstore. Please follow the Seqera Platform instructions for configuring the other values and launching
your pipeline.

.. figure:: /assets/images/docs/seqera_platform_from_dockstore.png
   :alt: Seqera Platform workflow launch interface

.. _nextflow-limitations:

Limitations
-----------

Seqera Platform runs a workflow by cloning its git repository and checking out the specified branch. Unlike other launch-with partners, it does not
fetch the workflow content directly from Dockstore. The Nextflow version on Dockstore can be out of sync with the version on GitHub, Bitbucket, or GitLab.
When determining the exact workflow contents being run on Seqera Platform, refer to the git repository.


.. discourse::
    :topic_identifier: 4406
