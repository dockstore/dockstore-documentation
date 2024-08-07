Google Colab
============

Dockstore integrates with the Google's `Colaboratory <https://colab.research.google.com/>`_ platform (usually referred to by its nickname "Colab"),
allowing you to launch notebooks from Dockstore to Colab.

Launching to Colab
------------------

On each notebook's public Dockstore page, you will see a
"Launch with Google Colab" button on the right. When you press it, the
currently selected version of the notebook will be launched.

.. figure:: /assets/images/docs/notebook-info-page.png
   :alt: Public notebook page

See our :doc:`Getting started with notebooks <../getting-started/getting-started-with-notebooks>` tutorial for more details about launching to Google Colab.

Limitations
-----------

1. When Dockstore launches a notebook to Google Colab, Colab reads the notebook file from the source GitHub repository.  However, unlike some other environments, it doesn't give the notebook access to the files in the repository.  See our :doc:`Notebook Portability <../advanced-topics/best-practices/notebook-portability>` page for more information.

See Also
--------

-  :doc:`GitHub Codespaces <../launch-with/github-codespaces-launch-with/>`
-  :doc:`MyBinder <../launch-with/mybinder-launch-with/>`

.. discourse::
    :topic_identifier: 8141
