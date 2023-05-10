Notebooks
=========

.. contents::
   :local:
   :depth: 2

.. note:: Dockstore Notebooks is currently in preview mode. Also note that the screenshots below were taken on our staging site.

Tutorial Goals
--------------

- Get familiarized with the concept of notebooks on Dockstore
- Learn the basics of creating a notebook using a .dockstore.yml file
- Learn how to register a notebook
- Publish your notebook to Dockstore

Notebooks are documents that can include code, text, images, and other media resources. They can be executed in notebook environments like Google Colab and JupyterLab.
This document will outline what is needed to register, update, and publish a notebook onto Dockstore. Please keep in mind that notebook functionality is currently in preview mode.

Overview
--------

In this tutorial, you will register a notebook using the Dockstore GitHub App, which automatically syncs your notebook from GitHub to Dockstore. More information about the Dockstore GitHub App can be found :doc:`here </getting-started/github-apps/github-apps-landing-page>`.

Dockstore Notebooks takes advantage of Google Colab's integration with GitHub. The integration allows you to develop your notebook in Google Colab and push your changes to GitHub from Google Colab. With the Dockstore GitHub App installed on your repository, any edits made to your notebook from Google Colab will automatically be synced to Dockstore.

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

The first step is to create a file named ``.dockstore.yml`` which acts as a configuration file used to describe your notebook. We will cover an example .dockstore.yml written for a simple hello world Jupyter notebook.
You can also view template .dockstore.yml files :doc:`here </assets/templates/notebooks/notebooks>` that describe the possible fields and values you can use to configure your notebook.

.. include:: /assets/templates/notebooks/example-1-name.yml
  :code:

Line 1 specifies the ``.dockstore.yml`` version. You should use the latest version, which is version 1.2.

Next is a required key named ``notebooks`` where your notebooks will be configured.

Within this, you need to specify the ``format`` and ``language`` of the notebook. Currently, we only support ``JUPYTER`` notebooks. For a list of all the languages supported, view the :doc:`notebook template files </assets/templates/notebooks/notebooks>`.

Next, you need to specify the absolute path to the notebook file in the Git repository using the ``path`` key.

Finally, you must set ``publish: true`` to publish your notebook in order for you to be able to view your notebook in preview mode. In the future, we will implement a My Notebooks page where you can view your unpublished notebooks.


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

Configure where you want to save the notebook to on GitHub then click OK. Google Colab will push a commit to your repository with the notebook.

.. figure:: /assets/images/docs/google-colab-save-on-github-dialog.png
    :width: 60 %

Dockstore will detect the new commit and automatically sync your notebook from GitHub to Dockstore.

Launch With Google Colab
------------------------

When viewing a public notebook on Dockstore, you can launch the notebook into Google Colab by clicking on the Google Colab link on the Launch With panel located on the right side of the page. This will open the notebook in Google Colab.

.. figure:: /assets/images/docs/launch-with-google-colab.png

Using the Notebooks Feature Flag
--------------------------------

There is a ``notebooks`` feature flag that can be used to explore Dockstore Notebooks features that are in development.

.. warning:: The features hidden behind this flag may not be fully functional, but using the flag offers you a preview of the features to come.

To use the ``notebooks`` feature flag, append ``notebooks`` to the Dockstore URL as a query parameter. You only need to do this once, unless you refresh/close your browser.

For example, if you're on the ``https://dockstore.org`` page, append ``notebooks`` such that it looks like this: ``https://dockstore.org?notebooks``.

If you're on a page that already contains query parameters, indicated by the presence of a question mark, append ``notebooks`` to the URL using an ampersand. For example, if you're on the ``https://dockstore.org/search?entryType=workflows&searchMode=files`` page, append ``notebooks`` such that it looks like ``https://dockstore.org/search?entryType=workflows&searchMode=files&notebooks``.

After applying the notebooks feature flag, Dockstore Notebooks features will appear throughout the site, marked with a warning banner.

.. figure:: /assets/images/docs/notebooks-warning-banner.png

Features that are activated with the feature flag:

- Notebooks component is displayed on the My Dashboard page for a logged-in user
- Notebooks tab is displayed on the My Starred page for a logged in user
- Notebooks tab is displayed on the Search page
- Notebooks link is displayed on the Sitemap
