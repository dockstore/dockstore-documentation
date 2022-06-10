About Dockstore
===============

The Dockstore concept is simple: provide a place where users can share tools encapsulated in Docker and described with the workflow languages. This enables scientists to share analytical tools in a way that makes them machine readable and runnable in a variety of environments. While Dockstore is focused on serving researchers in the biosciences, the combination of Docker and workflow languages can be used by anyone to describe the tools and services in their `Docker images <https://docs.docker.com/get-started/overview/#docker-objects>`__ in a standardized, machine-readable way. 

By providing an environment where scientific tools can easily be created, maintained, browsed, and launched, Dockstore aligns itself with several trends supporting open science. But it is more than just an open ecosystem to facilitate open science -- we're involved in shaping what open science looks like. Dockstore works closely with the `GA4GH <https://www.ga4gh.org>`__, and accordingly, Dockstore supports the languages commonly used by GA4GH's `Cloud Work Stream <http://ga4gh.cloud/>`__ members and APIs: `Common Workflow Language <https://www.commonwl.org/>`__ (CWL), `Workflow Description Language <https://openwdl.org/>`__ (WDL), `Nextflow <https://www.nextflow.io/>`__ (NFL), and `Galaxy <https://github.com/galaxyproject/gxformat2>`. We also work on the `GA4GH Tool Registry <https://github.com/ga4gh/tool-registry-service-schemas>`__ standard as a way of sharing data with workflow platforms and partners, in addition contributing to the development of workflow execution and data transfer standards at the GA4GH. 

Building off Docker and Git
---------------------------

There are existing repositories for Docker images, such as  `Docker Hub <https://hub.docker.com/>`__, `Quay.io <https://quay.io/>`__, and `GitLab <https://about.gitlab.com>`__ which allow users to build, publish, and share both public and private Docker images. There are also source control repositories like `GitHub <https://github.com>`__, `Bitbucket <https://bitbucket.org/>`__, and `GitLab <https://about.gitlab.com>`__, which are based on the `git <https://git-scm.com/>`__ approach to source control. This infrastructure is important, and indeed, Dockstore can link to those services for multiple tasks. However, the services on their own lack standardized ways of describing how to invoke tools contained within Docker containers. This is where Dockstore and workflow description language step in, providing standardized ways to define the inputs, parameterizations, and outputs of tools in a controlled way. The Dockstore website and CLI additionally implement GA4GH standards and APIs to make the execution of workflows and tools, whether that be on your local computer or on the cloud, easier and more standardized. Together, these resources provide the necessary tools to share analytical tools in a highly portable and reproducible way, a key concern for the scientific community.

Promoting Standards
-------------------

Dockstore provides a reference implementation for sharing computational analysis procedures in the sciences. It is essentially a living and evolving proof-of-concept designed as a starting point for three activities that we hope will result in community standards within the GA4GH: 

-  a best practices guide for describing tools in Docker containers with descriptor languages
-  a web service standard for registering, searching, and
   describing annotated Docker images that can be federated and
   indexed by multiple websites
-  a CLI tool to interact with both the Dockstore webservice and local workflow executors such as
   Cromwell or cwltool

We also implement certain utilities such as file provisioning plugins that support the GA4GH DRS (Data Repository Service) standard or command-line launchers that present a common interface across CWL and WDL as a living and evolving example of what we wish to use over time natively.

Building a Community
--------------------

Several large projects in the biosciences have registered workflows on Dockstore, including cancer sequencing projects such as PCAWG, PrecisionFDA, the Broad Institute, the University of California at Santa Cruz, and Cancer IT at Sanger. Dockstore is also a component of several NIH-funded cloud ecosystems including BioData Catalyst, the AnVIL Project, and eLwazi. We hope this work will aid the community and promote the registration of a large number of high-quality workflows in the system.

You can browse workflows uploaded by such projects in `our organizations page <https://dockstore.org/organizations>`__.

Future Plans
------------

Dockstore is continuously evolving, and as an open-source project, you can get involved too! Please see our `issues page <https://github.com/dockstore/dockstore/issues>`__ for details and discussions. For longer term plans, please see our `roadmap page <https://github.com/dockstore/dockstore/wiki/Dockstore-Roadmap>`__.


Ready to get started?
---------------------

See our :doc:`Getting Started series </getting-started/getting-started>` for a walkthrough of creating your first workflow and uploading it to Dockstore!


.. discourse::
    :topic_identifier: 1269
