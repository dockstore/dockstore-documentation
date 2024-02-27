MyBinder
========

Dockstore integrates with `MyBinder <https://mybinder.org/>`_, an online notebook environment based on `BinderHub <https://github.com/jupyterhub/binderhub>`_,
allowing you to launch notebooks from Dockstore to `mybinder.org <https://mybinder.org/>`_. Here is some information on
what that looks like from a user point of view in a mini tutorial.

Launching to MyBinder
---------------------

On each notebook's public Dockstore page, you will see a
"Launch with mybinder.org" button on the right. When you press it, the
currently selected version of the notebook will be launched.

.. figure:: /assets/images/docs/notebook-info-page.png
   :alt: Public notebook page

When a notebook is launched, MyBinder reads `requirements.txt` and `other configuration files <https://repo2docker.readthedocs.io/en/latest/specification.html>`_ from the source GitHub repository and uses them to build a kernel image.  This kernel image contains the specified software packages, backs the notebook environment, and is cached, making subsequent launches faster.

.. figure:: /assets/images/docs/mybinder/starting-repository.png
   :alt: Starting repository

.. note:: MyBinder is a non-profit, and its compute resources vary over time, causing launches to `sometimes fail <https://discourse.jupyter.org/t/binder-startup-stuck-at-pulling-image/22298/2>`_ during periods of high load.  In the event of a failure, you might retry later, or donate more servers to MyBinder.

After MyBinder builds the kernel image, it loads the notebook into a Jupyter-based interface:

.. figure:: /assets/images/docs/mybinder/notebook-in-mybinder.png
   :alt: Notebook in MyBinder

Limitations
-----------

1. You cannot save to GitHub using the MyBinder interface.  To commit a notebook to a repository, you must use the *File > Download* feature to save the files locally, then commit them to the repo using ``git``, GitHub, or a similar tool.

See Also
--------

-  :doc:`Google Colab <../launch-with/google-colab-launch-with/>`
-  :doc:`GitHub Codespaces <../launch-with/github-codespaces-launch-with/>`

.. discourse::
    :topic_identifier: 8142
