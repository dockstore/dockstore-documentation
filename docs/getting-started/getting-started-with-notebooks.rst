Notebooks
=========

.. contents::
   :local:
   :depth: 2

Tutorial Goals
--------------

- Create a notebook
- Save a notebook to GitHub
- Register a notebook on Dockstore
- Publish a notebook on Dockstore

Notebooks are documents that include code, text, images, and other media resources, typically in subsections called "cells".  You can create, modify, and execute notebooks in browser-based, interactive environments like Google Colab and JupyterLab.  This document outlines how to create, save, register, update, and publish a notebook on Dockstore.

Overview
--------

In this tutorial, you will create a notebook, save it to GitHub, and register your notebook on Dockstore using our GitHub App, which updates it when your repository changes.  More information about the Dockstore GitHub App can be found :doc:`here </getting-started/github-apps/github-apps-landing-page>`.

To create your notebook, you'll use `Google Colab <https://colab.research.google.com/>`_, a popular online notebook service.  Of course, you can author notebooks in other environments, such as `GitHub Codespaces <https://github.com/features/codespaces>`_, `MyBinder <https://mybinder.org/>`_, or `Jupyter <https://jupyter.org/try-jupyter/lab/>`_, but Colab is a clean, easy-to-use option that's perfect for beginners.

.. note:: If you've already created a notebook, but it's not on GitHub, start at :ref:`Save Your Notebook to GitHub <save-your-notebook-to-github>`.  If your notebook is on GitHub, skip to :ref:`Create Your .dockstore.yml File <create-your-dockstore-yml-file>`.

Create a Notebook
-----------------

To create a notebook, first navigate to the `Google Colab site <https://colab.research.google.com/>`_, create a Google account if you don't already have one (click the *Sign In* button at upper right, and then *Create account*), and log into it.  Then, click on *File > New* to open a new notebook.
After a few seconds, the main notebook environment appears, with a cursor blinking in a code cell:

.. figure:: /assets/images/docs/google-colab-new-notebook.png

Type a line or two of Python into the cell, then execute it by clicking the *Run* "play" icon to the left.  Colab will run your code (behind the scenes, somewhere in the "cloud") and display the output below.  Take a look, and if it's not right, edit your code and re-run it until you're happy.  Click *+ Code* to add another code cell, or *+ Text* to add a text cell that explains how it works.  Move the cells around with the arrows.  Then, repeat, over and over again, until it's done.

Voilà, you've created a notebook!

.. _save-your-notebook-to-github:

Save Your Notebook to GitHub
----------------------------

To allow Dockstore to read your notebook, you must save it to a GitHub repository.

First, log into your GitHub account and create a repository for your notebook.  Pick a good repository name, because it will be part of your notebook's name on Dockstore.

Then, link your notebook environment to your GitHub account and save your notebook to the repository.  To save a notebook to GitHub from Google Colab, link to your GitHub account by clicking on the *Settings* gear icon in the upper right corner and selecting GitHub in the dialog box. Then, click on *Authorise with GitHub* and authorize Google Colab to access your GitHub account.

.. figure:: /assets/images/docs/google-colab-authorize-with-github.png
    :width: 60 %

Next, click on *File > Save a copy in GitHub* to save your notebook to the repository.

.. figure:: /assets/images/docs/google-colab-save-on-github.png
    :width: 35 %

Configure where on GitHub you want to save the notebook to, then click *OK*. Google Colab will push a notebook commit to your repository.

.. figure:: /assets/images/docs/google-colab-save-on-github-dialog.png
    :width: 60 %

Congratulations!  You've saved your notebook to GitHub and are ready to tell Dockstore about it.

.. _create-your-dockstore-yml-file:

Create Your .dockstore.yml File
-------------------------------

To describe your notebook to Dockstore, create a YAML file named ``.dockstore.yml`` in the root directory of your repository.  When you register your notebook, Dockstore will read the ``.dockstore.yml`` file to determine the path to your notebook file (and other information about it).
For example, a ``.dockstore.yml`` for a simple "hello world" Jupyter notebook might look like:

.. include:: /assets/templates/notebooks/example-1-name-default-format-language.yml
  :code:

Line 1 specifies the ``.dockstore.yml`` version. You should use the latest version, which is version 1.2.

Next is the ``notebooks`` field, which specifies details about your notebook.  Although this field can by used to describe multiple notebooks, we're only including one here.

Within, the ``path`` field specifies the absolute path to the notebook file in the Git repository, and the ``topic`` field, which provides a short description (150 characters or less) of the notebook.

You can specify additional details in your ``.dockstore.yml``, such as the notebook's authors and description.  For more information about the file format and supported fields, see :doc:`here </assets/templates/notebooks/notebooks>`.

Register Your Notebook
----------------------

.. include:: /getting-started/github-apps/note--registration.rst

To register your Notebook on Dockstore, install our Dockstore GitHub App on the repository that contains your notebook and ``.dockstore.yml`` file.  After installation, Dockstore will read your repository, automatically register your notebook, and update the notebook whenever the repository changes.

.. include:: /getting-started/github-apps/note--vocabulary.rst

Install the Dockstore GitHub App
--------------------------------
.. include:: /getting-started/github-apps/snippet--installation.rst

Publish Your Notebook
---------------------
After you register your notebook, you have the option to publish it.  To publish your notebook, navigate to its page, and then click the *Publish* button at upper right.

When you publish your notebook, it becomes visible to the general public via a new "public" page, and other users can :doc:`star <../end-user-topics/starring>` it, add it to a :doc:`collection <../advanced-topics/organizations-and-collections>`, and :ref:`launch <launch-your-notebook>` it on various platforms:

.. figure:: /assets/images/docs/notebooks-public-page.png

Published notebooks also appear in :doc:`Search <../end-user-topics/faceted-search>`.

.. note:: After you publish your notebook, although you can archive or unpublish it, you'll no longer be able to delete it from Dockstore.

.. _launch-your-notebook:

Launch Your Notebook
--------------------

You can launch published Dockstore notebooks to the following environments:

* :doc:`Google Colab <../launch-with/google-colab-launch-with>`
* :doc:`GitHub Codespaces <../launch-with/github-codespaces-launch-with>`
* :doc:`MyBinder <../launch-with/mybinder-launch-with>`

.. note:: Some of these environments have requirements and quirks that could affect if and how well your notebook will run.  For more details, click the above links.

For example, to launch a notebook in Google Colab, navigate to its public page on Dockstore, and click on the *Google Colab* button on the *Launch with* panel at upper right:

.. figure:: /assets/images/docs/launch-with-google-colab.png

In a new window, the notebook will open in Google Colab.  Now, you can edit and run your notebook.  If you modify it and want to keep the changes, :ref:`save it<save-your-notebook-to-github>` to GitHub, and a few minutes later, the updates will appear on Dockstore.

.. discourse::
    :topic_identifier: 7984
