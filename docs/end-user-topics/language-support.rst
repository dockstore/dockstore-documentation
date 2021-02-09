Language Support
================

Ideally, all features in Dockstore would be available in all languages.
However, due to time constraints and gaps in our knowledge of different
workflows, some features of Dockstore are not available in all
languages.

To help lay out what parts of Dockstore are available in which
languages, we cover the following guide for what features are available
on the Dockstore site and in the Dockstore command-line utility.

.. raw:: html
    :file: ../_static/language-support.html

[0] Available in both classic and CWL Viewer modes

[1] Available in both classic and WDL EPAM Pipeline Builder

[2] Does not support http(s) based imports. See :ref:`CGC
Limitations <cgc-limitations>` for limitations.

[3] Does not support file-path based imports. See :ref:`Terra
Limitations <terra-limitations>` for limitations.

[4] Does not support file-path or http(s) based imports. See :ref:`DNAstack
Limitations <dnastack-limitations>` for limitations.

[5] All verified Dockstore WDL tools/workflows were tested successfully. However, we anticipate that more testing is needed for WDL workflows that use language features not contained within that dataset.

[6] Does not support file-path based imports. See :ref:`AnVIL
Limitations <anvil-limitations>` for limitations.

[7] Use the Dockstore CLI optional parameter --wdl-output-target which allows you to specify a remote path to provision output files to ex: s3://oicr.temp/testing-launcher/


.. _converting-file-path-based-imports-to-public-http-s-based-imports-for-wdl:

Converting File-path Based Imports to Public http(s) Based Imports for WDL
--------------------------------------------------------------------------

See https://cromwell.readthedocs.io/en/develop/Imports/ for general
knowledge on imports.

Imports allow you to reference other files in your workflow. There are
two types of resources that are supported in imports: http(s) and
file-path based. Any public http(s) based URL can be used as the
resource for an import, such as a website, GitHub, GA4GH compliant TRS
endpoint, etc.

There are times when you may want to convert file-path based imports to
public http(s) imports. One such reason is to ensure compatibility with
Terra since it currently does not support file-path based imports.
There are many different ways to convert to a public http(s) based
import, the following are two examples.

You can host your file on GitHub and import it in the workflow
descriptor like this:

::

    import "https://raw.githubusercontent.com/DataBiosphere/topmed-workflows/1.11.0/variant-caller/variant-caller-wdl/topmed_freeze3_calling.wdl" as TopMed_variantcaller
    import "https://raw.githubusercontent.com/DataBiosphere/topmed-workflows/1.11.0/variant-caller/variant-caller-wdl-checker/topmed-variantcaller-checker.wdl" as checker
    ...

Similarly, you can also host your file on a public google bucket and
import it in the workflow descriptor like this:

::

    import "http://storage.googleapis.com/..."
    ...

.. discourse::
    :topic_identifier: 1311
