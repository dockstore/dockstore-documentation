.dockstore.yml for Workflows Templates (version 1.2)
====================================================
Several templates and examples are provided here for you to reference for your own .dockstore.yml files. The last example provides a complete explanation of the possible fields and values you can use.

.. filled-out examples based on DataBiosphere/analysis_pipeline_wdl

Simple generic template for a workflow
--------------------------------------
.. include:: /assets/templates/workflows/template-minimum.dockstore.yml
  :code:

Filled-out example of a single workflow without a name
------------------------------------------------------
In this example, the workflow author is identified with an orcid. When an orcid is specified, there is no need to specify an author's name and email as that information will be pulled from the orcid. There are also three test parameter files given for the workflow.

.. include:: /assets/templates/workflows/example-1-noname.yml
  :code:

Filled-out example of a single workflow with a name
---------------------------------------------------
This example is identical to the one above, but the workflow in question now is identified with the ``name`` field. :doc:`See here for more information on naming workflows </advanced-topics/naming-workflows>`.

.. include:: /assets/templates/workflows/example-2-name.yml
  :code:

Filled-out example of multiple workflows in the same repository
---------------------------------------------------------------
First, you will notice that we swapped the order of the ``name`` and ``author`` fields for association-aggregate-wdl compared to the examples above, to demonstrate that the order is arbitrary. Next, we added a new section for pc-air-wdl, which has a different author and its own test parameter files and descriptor file. 

This .dockstore.yml will result in the creation of two entries on Dockstore -- one for association-aggregate-wdl, and one for pc-air-wdl.

.. include:: /assets/templates/workflows/example-3-multiworkflow-multiauthor.dockstore.yml
  :code:

Full template with explanation of all available fields
------------------------------------------------------
.. include:: /assets/templates/workflows/template-maximum.dockstore.yml
  :code:
  



See Also
--------

* :doc:`.dockstore.yml templates for registering services </assets/templates/services/services>`
* :doc:`.dockstore.yml templates for registering workflows </assets/templates/workflows/workflows>`
* :doc:`Other documentation regarding the GitHub App </getting-started/github-apps/github-apps-landing-page>`