.dockstore.yml for Tools Templates (version 1.2)
================================================
Several templates and examples are provided here for you to reference for your own .dockstore.yml files. The last example provides a complete explanation of the possible fields and values you can use.

.. The globalAligner/localAligner example does not seem to correspond to any entry on Dockstore. It's been on github-apps.rst since 2020 (commit 2ee9fb2b10d7b68fbf1481d066651cb8dad855ae).

Simple generic template for a tool
----------------------------------
.. include:: /assets/templates/tools/template-minimum.dockstore.yml
  :code:

Filled-out example of a single tool without a name
--------------------------------------------------
Although the author has a name, the tool itself is not identified with one.

.. include:: /assets/templates/tools/example-1-noname.yml
  :code:

Filled-out example of a single tool with a name
-----------------------------------------------
Same as the example above, but we explictly name the tool globalAligner.

.. include:: /assets/templates/tools/example-2-name.yml
  :code:

Filled-out example of multiple tools in the same repository
-----------------------------------------------------------
This .dockstore.yml will result in the creation of two entries on Dockstore: One for globalAligner, and one for localAligner.

You will note that localAligner has three authors. The first two are identified with orcids. The third author is instead identified with their name and email address.

.. include:: /assets/templates/tools/example-3-multitool-multiauthor.dockstore.yml
  :code:

Full template with explanation of all available fields
------------------------------------------------------
.. include:: /assets/templates/tools/template-maximum.dockstore.yml
  :code:
  



See Also
--------
  
* :doc:`.dockstore.yml templates for registering services </assets/templates/services/services>`
* :doc:`.dockstore.yml templates for registering workflows </assets/templates/workflows/workflows>`
* :doc:`Other documentation regarding the GitHub App </getting-started/github-apps/github-apps-landing-page>`