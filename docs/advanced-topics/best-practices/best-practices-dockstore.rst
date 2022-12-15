Dockstore Best Practices
========================

This document is intended for tool and workflow developers and the users who register them on Dockstore. Following these best practices will help make
your repositories more organized, findable, and usable for others on Dockstore.


Structuring and Organizing Your Git Repositories
----------------------------------------------------------------
Unless you're writing your tool/workflow directly on Dockstore, your entry will be hosted on a Git repository (we currently support integration with GitHub, Bitbucket, and GitLab).
Whichever repository service you use, we recommend that your tool and workflow repositories are put under a non-personal organization, if possible.
This allows for better organization and collaboration, and also provides a fallback for others if you become inactive on the git repository site.

We generally advise against git repositories that contain multiple tools or workflows. But we recognize that it's a common way to share code, so we do support it.
However, there are two benefits for having only one tool or workflow per repository. First, your Dockstore entries can have shorter names because an extra name is required
to distinguish between the entries during registration. The other plus is that there will be less clutter on the Versions tab of each entry.
Let's say you have a repo that contains three different workflows on separate branches and there are many tags/releases related to each one.
Depending on how you register the workflows on Dockstore, each entry could have the other two branches and every single tag/release
on its Versions tab. All of this clutter can be overwhelming or confusing for users to see.

One exception to this rule is when you describe the same tool or workflow with multiple descriptor languages. For example, we describe the same bamstats tool
in our :doc:`Getting Started with CWL <../../getting-started/getting-started-with-cwl>` and :doc:`Getting Started with WDL <../../getting-started/getting-started-with-wdl>` tutorials.
A single tool on Dockstore can have CWL and WDL descriptor files. Users will be able to see you've provided both and can easily switch between the descriptors in the UI.
Unfortunately, you cannot have a single workflow entry on Dockstore contain multiple descriptor types. You will have to register them as separate workflows by using the Workflow Name field during registration.


Improving Your Entries On Dockstore
-----------------------------------

Making It Easier to Find
^^^^^^^^^^^^^^^^^^^^^^^^
There are a few things you can do to make your tool/workflow easier to find on our site.

Let's start with making your entry easier to find on our `search <https://dockstore.org/search>`_ page. One way is to add author and description metadata to your descriptor file.
Adding an author will make it selectable on the Author facet and a description helps because the text search uses it as one of the fields to sift through.
For more detailed information on these metadata fields, check out the following info for each language:

- :doc:`WDL Best Practices <./wdl-best-practices>`
- :doc:`CWL Best Practices <./cwl-best-practices>`
- :doc:`Nextflow Best Practices <./nfl-best-practices>` and `Nextflow manifest documentation <https://www.nextflow.io/docs/latest/config.html#scope-manifest>`_

.. note:: In CWL descriptors, you can include information about your input and output files and our search will understand it. This information will be visible on the facets ``Input File Formats`` and ``Output File Formats``. Read CWL's guide on `file formats <https://www.commonwl.org/user_guide/16-file-formats/index.html>`_ to learn how.

You can also provide a description by writing a README.md file instead. If you do not provide description metadata in your descriptor, then we will try to pull the README.md file as a fallback.

Another tip was already mentioned above; host your repositories on a non-personal organization. Similarly, try to use a non-personal namespace to register your Docker images.
Doing this will group your tools/workflows together under our ``Tool: Namespace`` and ``Workflow: Organization`` facets. This also helps by letting you add other developers
that can manage your content on and off Dockstore if you ever become unavailable.

You should also consider adding labels to your entry since ``Labels`` is another facet on the search page. You can do this by going to `My Tools <https://www.dockstore.org/my-tools>`_ or `My Workflows <https://www.dockstore.org/my-workflows>`_ page.
On the right hand side, above the tabs, you will see the text ``Manage labels``.

.. image:: /assets/images/docs/manage-labels.png

Once you click the text, you'll be able to add or remove labels for your entry. To get ideas for what to use as labels, look at what others are using on the search page.
Also note that each label cannot have spaces and must be all lowercase. If you want a label be multiple words, separate them by hypen instead of spaces.

You can also add a checker workflow to your tools and workflows to make use of our ``Has Checker Workflows`` facet. Checker workflows also guarantee that your entry,
given some input, produces the expected output on a platform different from the one where you are developing. Read our :doc:`Checker Workflows <../checker-workflows>` tutorial to learn more.

Another option for making your work more visible is using our :doc:`Organization and Collection <../organizations-and-collections>` pages.
An Organization is a landing page for your collaborations, institutions, consortiums, companies, etc. Here you can explain the work and goals your group has,
and highlight your tools and workflows by adding them to a Collection.

Making It Easier to Understand
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once a user has found your entry, they need to understand what it does and how to use it! The most important thing you can do so others understand your work is to provide a thorough description.
You can do this by filling out the metadata field as explained in the best practices tutorials linked above. If no description is found in the descriptor file, we will use the README.md file.
Your description, using either method, can be formatted using markdown. Once registered, it will be parsed by Dockstore and made available on the Info tab of an entry.
Because it will be one the of first things a user will see when looking at your entry, you should make it as detailed as possible. Here is a list of items to write about:

* About Section.

   * What does your tool or workflow do?
   * Are you part of a bigger organization? What are some of their goals?

* How to Use Section.

   * What are the system requirements? Minimum and recommended
   * Describe the input and output files (Can also be included in CWL descriptor files. See blue ``! Note`` box above.)

      * What are their names?
      * What data do they contain?
      * What is the format?

   * Can you provide time and/or cloud cost estimations for running your tool/workflow with a given input?
   * If available, link to tutorials using your entry.
   * If available, link to a sample or complete dataset to use.

* Related To Section

   * Does your tool/workflow work together with other entries? If so, describe how they can be used together and provide links.
   * Link out to other similar entries you think could be useful to others.

* Contact Section (Can be included in other metadata fields as mentioned in the Making it Easier to Find section.)
* Citations

   * Does your workflow employ packages that should be cited?

Making It Easier to Use
^^^^^^^^^^^^^^^^^^^^^^^
Although it's not always possible, you should provide input data needed to run the entry. You can do this a few different ways:

* Provide links to the data needed in your description.
* Have your entry download the input files using a link. You can do this by putting them in a test parameter file (recommended) or directly in the descriptor files.
* Have the files within the Docker image being used. If you do this, make sure you provide a description of the structure and expected files in the description above.

.. note:: You can learn more about test parameter files by reading any of the Testing Locally Sections for :ref:`CWL <Testing CWL Locally>`, :ref:`WDL <Testing WDL Locally>`, or :ref:`Nextflow <Testing Nextflow Locally>`.


.. discourse::
    :topic_identifier: 6278
