MyBinder.org
============

Dockstore integrates with `MyBinder <https://mybinder.org/>`_, an online notebook environment based on `BinderHub <https://github.com/jupyterhub/binderhub>`_,
allowing you to launch notebooks from Dockstore to mybinder.org. Here is some information on
what that looks like from a user point of view in a mini tutorial.

Launching to MyBinder
---------------------

When browsing notebooks from within Dockstore, you will see a
"Launch with mybinder.org" button on the right. When you press it, the
currently selected version of the notebook will be launched.

.. figure:: /assets/images/docs/notebook-info-page.png
   :alt: Public notebook page

When Dockstore launches a notebook to MyBinder, MyBinder reads `certain <https://repo2docker.readthedocs.io/en/latest/specification.html>`_ configuration files from the source GitHub repository and uses them to build a kernel image.  This kernel image contains the specified software dependencies, is used to back the notebook environment, and is cached, making subsequent launches faster.

.. figure:: /assets/images/docs/mybinder/starting-repository.png
   :alt: Starting repository

.. note: MyBinder is a non-profit, and its computational resources vary, causing launches to `sometimes fail <https://discourse.jupyter.org/t/binder-startup-stuck-at-pulling-image/22298/2>`_ during periods of high load.  In the event of a failure, you might retry later, or donate more compute to MyBinder.

After MyBinder builds the kernel image, it displays the notebook within a Jupyter-based UI:

.. figure:: /assets/images/docs/mybinder/notebook-in-mybinder.png
   :alt: Notebook in MyBinder

Limitations
-----------

1. You cannot save to GitHub using The MyBinder interface.  To commit a modified notebook to a repository, you must use the MyBinder UI to save the files locally, and then commit them to the repo using ``git``, GitHub, or similar.

See Also
--------

-  :doc:`GitHub Codespaces <../launch-with/github-codespaces-launch-with/>`
-  :doc:`MyBinder <../launch-with/mybinder-launch-with/>`
