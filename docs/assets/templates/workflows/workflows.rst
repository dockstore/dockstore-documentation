.dockstore.yml for Workflows Templates (version 1.2)
====================================================
Several templates and examples are provided here for you to reference for your own .dockstore.yml files. The last example provides a complete explanation of the possible fields and values you can use.

..
  filled-out examples based on DataBiosphere/analysis_pipeline_wdl

Simple generic template for a workflow
--------------------------------------
.. include:: /assets/templates/workflows/template-small.dockstore.yml
  :code:

Always use :ref:`absolute paths <dict absolute path>` to specify the :ref:`primary descriptor <dict primary descriptor file>`, :ref:`test parameter <dict parameter file>`, and readMePath files.

Filled-out example of a single workflow without a name
------------------------------------------------------
In this example, the workflow author is identified with an orcid. When an orcid is specified, there is no need to specify an author's name and email as that information will be pulled from the orcid. There are also three test parameter files given for the workflow. Since no readMePath is specified, Dockstore will show the top-level readme (if one is present), eg, ``./readme.md``

.. include:: /assets/templates/workflows/example-1-noname.yml
  :code:

Filled-out example of a single workflow with a name
---------------------------------------------------
This example is identical to the one above, but the workflow in question now is identified with the ``name`` field, a user-defined string that can contain letters, numbers, internal hyphens, and internal underscores, but no spaces or other characters. :doc:`See here for more information on naming workflows </advanced-topics/naming-workflows>`.

.. include:: /assets/templates/workflows/example-2-name.yml
  :code:

Filled-out example of multiple workflows in the same repository
---------------------------------------------------------------
First, you will notice that we swapped the order of the ``name`` and ``author`` fields for assoc-aggregate-wdl compared to the examples above, to demonstrate that the order is arbitrary. Next, we added a new section for pc-air-wdl, which has a different author and its own test parameter files and descriptor file. We have also added the optional ``readMePath`` value to these workflows so that each entry gets its own workflow-specific readme.

This .dockstore.yml will result in the creation of two entries on Dockstore -- one for assoc-aggregate-wdl, and one for pc-air-wdl. assoc-aggregate-wdl's entry will show the readme located at ``/assoc-aggreate/readme.md``, while pc-air-wdl's entry will show the readme located at ``/pc-air/README.md``. Although ``readMePath`` is optional, if we did not add it to these entries, both entries would instead show the same top-level readme.md (or README.md) of the git repo.

.. include:: /assets/templates/workflows/example-3-multiworkflow-multiauthor.dockstore.yml
  :code:

Full template with explanation of all available fields
------------------------------------------------------
.. include:: /assets/templates/workflows/template-big.dockstore.yml
  :code:
  



See Also
--------

* :doc:`.dockstore.yml templates for registering services </assets/templates/services/services>`
* :doc:`.dockstore.yml templates for registering workflows </assets/templates/workflows/workflows>`
* :doc:`Other documentation regarding the GitHub App </getting-started/github-apps/github-apps-landing-page>`
