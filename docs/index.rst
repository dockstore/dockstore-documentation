Welcome to Dockstore Documentation!
===================================

.. note:: Our code lives on GitHub at `dockstore/dockstore <https://github.com/dockstore/dockstore>`_ and `dockstore/dockstore-ui2 <https://github.com/dockstore/dockstore-ui2>`_.

Dockstore is an open platform used by the `GA4GH <https://www.ga4gh.org/>`__ for sharing reproducible and interoperable tools, workflows, and services. For tools and workflows, we support Common Workflow Language (CWL), Workflow Description Language (WDL), Nextflow (NFL), and Galaxy.

If this is your first time learning about Dockstore, we recommend starting with the :doc:`Getting Started Guide <getting-started/getting-started>`. This will introduce you to the core concepts of Dockstore, leaving you with a good understanding of the platform. However, if you are simply looking to launch tools and workflows, we recommend going straight to the :doc:`End User Topics <end-user-topics/end-user-topics>` or our `quickstart guide <https://dockstore.org/quick-start>`_.

.. toctree::
   :maxdepth: 1

   Go to Dockstore <https://dockstore.org>
   systemstatus

.. toctree::
   :caption: About
   :maxdepth: 1

   dockstore-introduction
   Dockstore Blog <https://medium.com/dockstore>
   changelog
   faq
   news
   roadmap
   dictionary
   /assets/templates/template.rst

Getting Started
---------------
* :doc:`Intro to Dockstore Tools and Workflows </getting-started/intro-to-dockstore-tools-and-workflows>`
* Getting started tutorial -- designed for people totally new to writing workflows and working with Docker

    1. :doc:`Intro </getting-started/getting-started>`
    2. :doc:`Docker <getting-started/getting-started-with-docker>`
    3. Language-specific introductions

        * :doc:`Common Workflow Language (CWL) <getting-started/getting-started-with-cwl>`
        * :doc:`Workflow Description Language (WDL) <getting-started/getting-started-with-wdl>`
        * :doc:`Nextflow (NFL) <getting-started/getting-started-with-nextflow>`
        * :doc:`Galaxy <getting-started/getting-started-with-galaxy>`

    4. :doc:`Creating a Dockstore Account <getting-started/register-on-dockstore>`
    5. :doc:`Register a tool on Dockstore <getting-started/dockstore-tools>`
    6. :doc:`Register a workflow on Dockstore <getting-started/dockstore-workflows>`
    7. :doc:`Delete a entry on Dockstore <getting-started/delete-on-dockstore>`
    8. :doc:`Hosted tools and workflows <getting-started/hosted-tools-and-workflows>`
* :doc:`Notebooks <getting-started/getting-started-with-notebooks>`
* :doc:`Services (preview) <getting-started/getting-started-with-services>`
* :doc:`Registering tools, workflows, notebooks, and services with the Dockstore GitHub App <getting-started/github-apps/github-apps-landing-page>`

.. toctree::
   :caption: Getting Started (Tutorial)
   :maxdepth: 1
   :hidden:

   getting-started/getting-started
   getting-started/intro-to-dockstore-tools-and-workflows
   getting-started/getting-started-with-docker
   getting-started/getting-started-with-cwl
   getting-started/getting-started-with-wdl
   getting-started/getting-started-with-nextflow
   getting-started/getting-started-with-galaxy
   getting-started/register-on-dockstore
   getting-started/dockstore-tools
   getting-started/dockstore-workflows
   getting-started/delete-on-dockstore
   getting-started/hosted-tools-and-workflows
   getting-started/getting-started-with-services
   getting-started/getting-started-with-notebooks
   getting-started/github-apps/github-apps-landing-page

Launching tools and workflows from Dockstore
--------------------------------------------
Dockstore partners with several compute platforms, allowing you to export workflows into these platforms with the click of a button. We also provide a CLI to run tools and workflows locally. Click on the links below for more information.

Cloud Partners
^^^^^^^^^^^^^^

.. centered:: |AnVILLaunchWith|_ |CavaticaLaunchWith|_ |CGCLaunchWith|_ |DnanexusLaunchWith|_ |GalaxyLaunchWith|_ |NextflowtowerLaunchWith|_ |TerraLaunchWith|_

.. |AnVILLaunchWith| image:: /assets/images/square/anvil_text.png
    :alt: go to launch with AnVIL page
    :height: 140px
.. _AnVILLaunchWith: launch-with/anvil-launch-with.html

.. |CavaticaLaunchWith| image:: /assets/images/square/cavatica_text.png
    :alt: go to launch with Cavatica page
    :height: 140px
.. _CavaticaLaunchWith: launch-with/cavatica-launch-with.html

.. |CGCLaunchWith| image:: /assets/images/square/cgc_text.png
    :alt: go to launch with Cancer Genome Cloud (CGC) page
    :height: 140px
.. _CGCLaunchWith: launch-with/cgc-launch-with.html

.. |DnanexusLaunchWith| image:: /assets/images/square/dnanexus_text.png
    :alt: go to launch with DNA Nexus page
    :height: 140px
.. _DnanexusLaunchWith: launch-with/dnanexus-launch-with.html

.. |GalaxyLaunchWith| image:: /assets/images/square/galaxy_text.png
    :alt: go to launch with Galaxy page
    :height: 140px
.. _GalaxyLaunchWith: launch-with/galaxy-launch-with.html

.. |NextflowtowerLaunchWith| image:: /assets/images/square/nextflowtower_text.png
    :alt: go to launch with Nextflow Tower page
    :height: 140px
.. _NextflowtowerLaunchWith: launch-with/nextflow-tower-launch-with.html

.. |TerraLaunchWith| image:: /assets/images/square/terra_text.png
    :alt: go to launch with Terra page
    :height: 140px
.. _TerraLaunchWith: launch-with/terra-launch-with.html

In addition to the above cloud partners, you can also launch workflows with :doc:`BioData Catalyst <launch-with/bdcat-launch-with>` or the :doc:`Dockstore CLI <launch-with/launch>`.

.. toctree::
   :caption: Launch Tools and Workflows
   :maxdepth: 1
   :hidden:

   launch-with/launch
   launch-with/anvil-launch-with
   launch-with/bdcat-launch-with
   launch-with/cavatica-launch-with
   launch-with/cgc-launch-with
   launch-with/dnanexus-launch-with
   launch-with/galaxy-launch-with
   launch-with/nextflow-tower-launch-with
   launch-with/terra-launch-with

.. toctree::
   :caption: End user topics
   :maxdepth: 1

   end-user-topics/end-user-topics
   end-user-topics/faceted-search
   end-user-topics/starring
   end-user-topics/language-support
   end-user-topics/ORCID

.. toctree::
   :caption: Videos (tutorials & presentations)
   :maxdepth: 1

   videos

Best practices guidelines
-------------------------

* Language-specific: :doc:`CWL <advanced-topics/best-practices/cwl-best-practices>` | :doc:`Nextflow <advanced-topics/best-practices/nfl-best-practices>` | :doc:`WDL <advanced-topics/best-practices/wdl-best-practices>`
* :doc:`Best practices on Dockstore <advanced-topics/best-practices/best-practices-dockstore>`
* :doc:`Best practices for secure and FAIR workflows <advanced-topics/best-practices/best-practices-secure-fair-workflows>`

.. toctree::
   :caption: Best Practices
   :maxdepth: 1
   :hidden:

   advanced-topics/best-practices/cwl-best-practices
   advanced-topics/best-practices/wdl-best-practices
   advanced-topics/best-practices/nfl-best-practices
   advanced-topics/best-practices/best-practices-dockstore
   advanced-topics/best-practices/best-practices-secure-fair-workflows

.. toctree::
   :caption: Dockstore CLI
   :maxdepth: 1

   Installing the Dockstore CLI <https://dockstore.org/quick-start>
   advanced-topics/dockstore-cli/overview
   advanced-topics/dockstore-cli/dockstore-cli-faq
   advanced-topics/dockstore-cli/local-cromwell-config
   advanced-topics/dockstore-cli/set-up-file-provisioning-plugins
   advanced-topics/dockstore-cli/developing-file-provisioning-plugins
   advanced-topics/dockstore-cli/advanced-features
   advanced-topics/dockstore-cli/yaml-command-line-validator-tool

Advanced developer topics
-------------------------
.. include:: advanced-topics/advanced-topics.rst

.. To get the above to format nicely, I made changes to advanced-topics/advanced-topics that make it no longer compatible with the Table of Contents, so advanced-topics/advanced-topics will no longer show in the sidebar. I feel that is a fair trade off.

* :doc:`Dockstore Tools Overhaul <advanced-topics/dockstore-tools-overhaul>`
* :doc:`Detailed comparison of tools and workflows <advanced-topics/tools-vs-workflows>`
* :doc:`Legacy features <advanced-topics/legacy/legacy>`
* :doc:`Docker registries <advanced-topics/docker-registries>`
* :doc:`Public and private tools <advanced-topics/public-and-private-tools>`
* :doc:`Checker workflows <advanced-topics/checker-workflows>`, and :doc:`how to run them using TRS <advanced-topics/checker-workflow-trs>`
* :doc:`Sharing workflows <advanced-topics/sharing-workflows>`
* :doc:`Aliases <advanced-topics/guid-alias>`
* :doc:`Docker alternatives <advanced-topics/docker-alternatives>`
* Maximizing reproducibility

    * :doc:`Creating snapshots and requesting DOIs <advanced-topics/snapshot-and-doi>`
    * :doc:`Checksum for files and Docker Images <advanced-topics/checksum-support>`
* :doc:`GA4GH Write API (intended as a proof-of-concept and for developers with a large number of tools) <advanced-topics/conversions>`
* :doc:`Using batch services (AWS, Azure, Google, and Consonance) <advanced-topics/batch-services>`
* :doc:`Verified workflows and tools <advanced-topics/verification>`
* :doc:`Workflow metrics <advanced-topics/metrics>`
* :doc:`Organizations and collections <advanced-topics/organizations-and-collections>`

.. Purposely not including the AWS and Azure batch links as the batch-services one links to them and is pretty short so they are easy to find. I would even argue for removing them from the sidebar or making them a subfolder of batch-services.
.. Purposely not including "posting zips" as it is depreciated, but it is still in the sidebar

.. toctree::
   :caption: Advanced Developer Topics
   :maxdepth: 1
   :hidden:

   advanced-topics/dockstore-tools-overhaul
   advanced-topics/tools-vs-workflows
   advanced-topics/legacy/legacy
   advanced-topics/docker-registries
   advanced-topics/public-and-private-tools
   advanced-topics/checker-workflows
   advanced-topics/checker-workflow-trs
   advanced-topics/sharing-workflows
   advanced-topics/guid-alias
   advanced-topics/docker-alternatives
   advanced-topics/snapshot-and-doi
   advanced-topics/checksum-support
   advanced-topics/conversions
   advanced-topics/batch-services
   advanced-topics/aws-batch
   advanced-topics/azure-batch
   advanced-topics/posting-zips
   advanced-topics/verification
   advanced-topics/metrics
   advanced-topics/organizations-and-collections
   advanced-topics/wes/cli-wes-tutorial

.. toctree::
   :caption: Extras
   :maxdepth: 1

   BCC 2020 Docker Training </docker_instructions>
   BCC 2020 WDL Training </wdl_instructions>
   posters-and-talks
   user-created
   Dockstore Logo Usage Guidelines </dockstore-logo-usage-guidelines>

.. centered:: In Affiliation with

.. centered:: |CollabLink|_ |imagespace| |OicrLink|_ |imagespace| |Ga4ghLink|_ |imagespace| |UcscLink|_

.. |CollabLink| image:: /assets/images/affiliations/collaboratory.png
    :alt: collaboratory
    :height: 55px
.. _CollabLink: https://cancercollaboratory.org

.. |OicrLink| image:: /assets/images/affiliations/oicr.png
    :alt: oicr
    :height: 55px
.. _OicrLink: https://oicr.on.ca/

.. |Ga4ghLink| image:: /assets/images/affiliations/ga4gh.png
    :alt: ga4gh
    :height: 55px
.. _Ga4ghLink: https://www.ga4gh.org

.. |UcscLink| image:: /assets/images/affiliations/ucsc.png
    :alt: ucsc
    :height: 55px
.. _UcscLink: https://genomics.ucsc.edu/

.. centered:: Workflow Languages

.. centered:: |CwlLink|_ |imagespace| |WdlLink|_ |imagespace| |NflLink|_ |imagespace| |GalaxyLink|_

.. |CwlLink| image:: /assets/images/affiliations/cwl.png
    :alt: cwl
    :height: 65px
.. _CwlLink: https://www.commonwl.org/

.. |WdlLink| image:: /assets/images/affiliations/wdl.png
    :alt: wdl
    :height: 45px
.. _WdlLink: https://openwdl.org/

.. |NflLink| image:: /assets/images/affiliations/nfl.png
    :alt: nextflow
    :height: 45px
.. _NflLink: https://www.nextflow.io/

.. |GalaxyLink| image:: /assets/images/affiliations/galaxy.png
    :alt: galaxy
    :height: 55 px
.. _GalaxyLink: https://galaxyproject.org/

.. centered:: Works With

.. centered:: |SevenBridgesLink|_ |imagespace| |TerraLink|_

.. |SevenBridgesLink| image:: /assets/images/affiliations/sevenbridges.png
    :alt: sevenbridges
    :height: 45px
.. _SevenBridgesLink: https://www.sevenbridges.com/

.. |TerraLink| image:: /assets/images/affiliations/terra.png
    :alt: terra
    :height: 75px
.. _TerraLink: https://terra.bio/

.. |imagespace| unicode:: U+00A0 U+00A0 U+00A0 U+00A0 U+00A0 .. non-breaking spaces between logo images

.. centered:: |horizontalline|

.. |horizontalline| image:: /assets/images/hori_line.png
    :alt: line
    :height: 25 px
