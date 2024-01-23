Notebooks
=========

.. contents::
   :local:
   :depth: 2

Tutorial Goals
--------------

- Get familiarized with the concept of notebooks on Dockstore
- Learn the basics of creating a notebook using a .dockstore.yml file
- Learn how to register a notebook
- Publish your notebook to Dockstore

Notebooks are documents that can include code, text, images, and other media resources. They can be executed in notebook environments like Google Colab and JupyterLab.
This document outlines how to register, update, and publish a notebook on Dockstore.

Overview
--------

In this tutorial, you will register a notebook using the Dockstore GitHub App, which automatically syncs your notebook from GitHub to Dockstore. More information about the Dockstore GitHub App can be found :doc:`here </getting-started/github-apps/github-apps-landing-page>`.

Dockstore Notebooks takes advantage of Google Colab's integration with GitHub. The integration allows you to develop your notebook in Google Colab and push your changes to GitHub from Google Colab. With the Dockstore GitHub App installed on your repository, any edits saved to your notebook from Google Colab will automatically be synced to Dockstore.

Setting up the Google Colab and GitHub integration
--------------------------------------------------

To get started, you will need a Google Colab account and a GitHub account.

In your Google Colab account, link your Google Colab account to your GitHub account. Click on the Settings gear icon in the upper right corner, then select GitHub in the dialog box. Click on Authorise with GitHub and authorize Google Colab to access your GitHub account.

.. figure:: /assets/images/docs/google-colab-authorize-with-github.png
    :width: 60 %

Next, we will set up a notebook on Google Colab so that it's also stored in one of your GitHub repositories. If you already have a notebook in Google Colab that's saved to a GitHub repository, you may proceed to :ref:`create the .dockstore.yml file for your repository<create-dockstore-yml>`.

We will cover two scenarios:

1. :ref:`You don't have a notebook in GitHub<no-notebook-in-github>`. You may or may not have a notebook in Google Colab.
2. :ref:`You have a notebook in GitHub, but it's not in Google Colab<no-notebook-in-google-colab>`

.. _no-notebook-in-github:

You don't have a notebook in GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't have a notebook in GitHub *nor* Google Colab, navigate to Google Colab and create a new notebook by clicking on File > New notebook. Edit your new notebook if you like.

If you already have a notebook in Google Colab, proceed to the next step.

Click on File > Save a copy in GitHub to save your notebook to a GitHub repository. You may want to create a new repository for your notebook if you don't already have a repository that you want to save the notebook to.

.. figure:: /assets/images/docs/google-colab-save-on-github.png
    :width: 35 %

Configure where you want to save the notebook to on GitHub then click OK. Google Colab will push a commit to your repository with the notebook.

.. figure:: /assets/images/docs/google-colab-save-on-github-dialog.png
    :width: 60 %

.. _no-notebook-in-google-colab:

You have a notebook in GitHub, but it's not in Google Colab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on File > Open notebook then select the GitHub tab in the dialog box. Select the notebook that you want to import from GitHub. This will open the notebook in Google Colab.

.. figure:: /assets/images/docs/google-colab-open-notebook-github.png
    :width: 60 %

.. _create-dockstore-yml:

Create Your .dockstore.yml File
-------------------------------

The first step is to create a file named ``.dockstore.yml`` which acts as a configuration file used to describe your notebook. This file should be created in the GitHub repository containing your notebook. We will cover an example .dockstore.yml written for a simple hello world Jupyter notebook written in Python. You can also view template .dockstore.yml files :doc:`here </assets/templates/notebooks/notebooks>` that describe the possible fields and values you can use to configure your notebook.

.. include:: /assets/templates/notebooks/example-1-name-default-format-language.yml
  :code:

Line 1 specifies the ``.dockstore.yml`` version. You should use the latest version, which is version 1.2.

Next is a required key named ``notebooks`` where your notebooks will be configured.

Within this, you can to specify the ``format`` and ``language`` of the notebook. These are optional keys and if left out, like in the example above, default to ``Jupyter`` and ``Python`` respectively. Currently, we only support ``Jupyter`` notebooks. For a list of all the languages supported, view the :doc:`notebook template files </assets/templates/notebooks/notebooks>`.

Next, you need to specify the absolute path to the notebook file in the Git repository using the ``path`` key.

Registering Your Notebook
-------------------------
.. include:: /getting-started/github-apps/note--registration.rst

To register your Notebook on Dockstore, you need to install our Dockstore GitHub application on the repository containing your notebook and .dockstore.yml file. By doing so, Dockstore will automatically register the notebooks and update your notebooks whenever your repository is updated on GitHub.

.. include:: /getting-started/github-apps/note--vocabulary.rst

Install the Dockstore GitHub App
--------------------------------
.. include:: /getting-started/github-apps/snippet--installation.rst

Publishing Your Notebook
------------------------
In this release, you are only able to publish your notebook using the ``publish`` key in the .dockstore.yml file, and your notebook must be published in order for you to view it on Dockstore.

Publishing will create a public page that is very similar to the ones we have for tools and workflows.

.. figure:: /assets/images/docs/notebooks-public-page.png

Now other users can view and :doc:`star <../end-user-topics/starring>` your notebook. You will also have the option to add published notebooks to a :doc:`collection <../advanced-topics/organizations-and-collections>`.

Saving Changes to Your Notebook on Google Colab to GitHub
---------------------------------------------------------

At this point, your Google Colab and GitHub integration should be set up, you have installed the Dockstore GitHub App to your GitHub repository containing your notebook, and the published notebook appears on Dockstore. 

You may wish to continue developing your notebook on Google Colab by modifying and re-running it. In order for the changes to your notebook to appear on Dockstore, you must click on File > Save a copy in GitHub to save your notebook to your GitHub repository.

.. figure:: /assets/images/docs/google-colab-save-on-github.png
    :width: 35 %

Configure the GitHub repository and branch that you want to save the notebook to. This should be the repository and branch that contains your .dockstore.yml describing the notebook you have on Dockstore. Once configured, click OK. Google Colab will push a commit to your repository with the notebook.

.. figure:: /assets/images/docs/google-colab-save-on-github-dialog.png
    :width: 60 %

Dockstore will detect the new commit and automatically sync your notebook from GitHub to Dockstore.

Launch With Google Colab
------------------------

When viewing a public notebook on Dockstore, you can launch the notebook into Google Colab by clicking on the Google Colab link on the Launch With panel located on the right side of the page. This will open the notebook in Google Colab.

.. figure:: /assets/images/docs/launch-with-google-colab.png

