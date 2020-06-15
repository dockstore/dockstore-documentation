Dockstore Best Practices
========================

This document is intended for tool and workflow developers and the users who register them on Dockstore. Following these best practices will help make
your repositories more organized, findable, and usable for others on Dockstore.


Structuring and Organizing Your Git Repositories
----------------------------------------------------------------
Unless you're writing your tool/workflow directly on Dockstore, your entry will be hosted on a Git repository (we currently support integration with GitHub, BitBucket, and Gitlab).
Whichever repository service you use, we recommend that your tool and workflow repositories are put under a non-personal organization, if possible.
This allows for better organization and collaboration, and also provides a fallback for others if you become inactive on the git repository site.

We also highly recommend that you do NOT host different tools and workflows on a single repo by putting them on different branches.
Our reasoning is that branches are supposed to be used when working on a new feature or bug fix. That means they should eventually be merged with the repository's main branch.
Another reason why we are against this practice is because it can lead to a lot of clutter on the Dockstore entries themselves.
Let's say you have three workflows in a single repo on separate branches and there are many tags/releases related to each one.
Depending on how you register the workflows on Dockstore, each entry could have the other two branches and every single tag/release
on its Versions tab. All of this clutter can be overwhelming or confusing for users to see.

Likewise, we don't recommend using even a single branch to hosts multiple entries. A repository should essentially represent one project, but that practice can be a grey area.
If a lot of different workflows or tools work together or are closely related, it can be argued that they're all part of a single project.
If that is the case, and you want to keep them tied together this way, make sure to give the descriptor files helpful file names.
It can also help to keep them organized using different, well-named folders for each entry.

One exception to this rule is when you describe the same tool or workflow with multiple descriptor languages. For example, we describe the same bamstats tool
in our :doc:`Getting Started with CWL <../../getting-started/getting-started-with-cwl>` and :doc:`Getting Started with WDL <../../getting-started/getting-started-with-wdl>` tutorials.
A single tool on Dockstore can have CWL and WDL descriptor files. Users will be able to see you've provided both and can easily switch between the descriptors in the UI.
Unfortunately, you cannot have a single workflow entry on Dockstore contain multiple descriptor types. You will have to register them as separate workflows.


Improving Your Entries On Dockstore
-----------------------------------

Making It Easier to Find
^^^^^^^^^^^^^^^^^^^^^^^^
There are a few things you can do to make your tool/workflow easier to find on our site.

Let's start with making your entry easier to find on our `search <https://dockstore.org/search>`_ page. One way is to add author and description metadata to your descriptor file.
Adding an author will make it selectable on the Author facet and a description helps because doing a text search sifts through the text of your descriptor files.
For more detailed information on these metadata fields, check out the following info for each language:

- :doc:`WDL Best Practices <./wdl-best-practices>`
- :doc:`CWL Best Practices <./best-practices>`
- :doc:`Nextflow Best Practices <./nfl-best-practices>` and `Nextflow manifest documentation <https://www.nextflow.io/docs/latest/config.html#scope-manifest>`_

Another tip was already mentioned above; host your repositories on a non-personal organization. Similarly, try to use a non-personal namespace to register your Docker images.
Doing this will group your tools/workflows together under our ``Tool: Namespace`` and ``Workflow: Organization`` facets.

You should also consider adding labels to your entry since ``Labels`` is another facet on the search page. You can do this by going to `My Tools <https://www.dockstore.org/my-tools>`_ or `My Workflows <https://www.dockstore.org/my-workflows>`_ page.
On the right hand side, above the tabs, you will see the text``Manage labels``.

.. image:: /assets/images/docs/manage-labels.png

Once you click the text, you'll be able to add or remove labels for your entry. To get ideas for what to use as labels, look at what others are using on the search page.
Also note that each label cannot have spaces and must be all lowercase. If you want a label to be two words, use a hyphen.

Another option for making your work more visible is using our :doc:`Organization and Collection <../organizations-and-collections>` pages.
An Organization is a landing page for your collaborations, institutions, consortiums, companies, etc. Here you can explain the work and goals your group has,
and highlight your tools and workflows by adding them to a Collection.

Making It Easier to Understand
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once a user has found your entry, they need to understand what it does and how to use it! The most important thing you can do so others understand your work is to provide a thorough description.
You can do this by filling out the metadata field as explained in the best practices tutorials linked above, or you can write one in the README file.
Your description can be formatted using markdown. Once registered, it will be parsed by Dockstore and made available on the Info tab of an entry.
Because it will be on the of first things a user will see when looking at your entry, you should make it as detailed as possible. Here is a list of items to write about:

* About section.

   * What does your tool or workflow do?
   * Are you part of a bigger organization? What are some of their goals

* How to Use Section.

   * What are the system requirements? Minimum and recommended
   * Describe the input and output files

      * What are their names?
      * What data do they contain?
      * What is the format?

   * Can you provide time and/or cloud cost estimations for running your tool/workflow with a given input?
   * If available, link to tutorials using your entry.
   * If available, link to a sample or complete dataset to use.

* Related To Section

  * Does your tool/workflow work together with other entries? If so, describe how they can be used together and provide links.
  * Link out to other similar entries you think could be useful to others.

* Contact Section
* Citations

   * Does your workflow employ packages that should be cited?

Making It Easier to Use
^^^^^^^^^^^^^^^^^^^^^^^
Although it's not always possible, you should provide the input data needed to run the entry. You can do this a few different ways:

* Provide links to the data needed in your description.
* Have your entry download the input files using a link. You can do this directly in the descriptor files or by putting them in a test parameter file.
* Have the files within the Docker image being used. If you do this, make sure you provide a description of the structure and expected files in the description above.

.. note:: You can learn more about test parameter files by reading any of the Testing Locally Sections for :ref:`CWL <Testing CWL Locally>`, :ref:`WDL <Testing WDL Locally>`, or :ref:`Nextflow <Testing Nextflow Locally>`.


