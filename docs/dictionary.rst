.. This file was created using GreatGloss. It is highly recommended to update the
		source file that this page was generated from rather than modifying it directly.

Dockstore Dictionary
====================
.. hlist:: 
	:columns: 3

	* :ref:`dict .dockstore.yml`
	* :ref:`dict AnVIL Project`
	* :ref:`dict API`
	* :ref:`dict AWS`
	* :ref:`dict BD Catalyst`
	* :ref:`dict BDC`
	* :ref:`dict Biodata Catalyst`
	* :ref:`dict Cancer Genomics Cloud`
	* :ref:`dict categories`
	* :ref:`dict CGC`
	* :ref:`dict CLI`
	* :ref:`dict cloud computing`
	* :ref:`dict collections`
	* :ref:`dict Common Workflow Language`
	* :ref:`dict container`
	* :ref:`dict Cromwell`
	* :ref:`dict CWL`
	* :ref:`dict DAG`
	* :ref:`dict descriptor file`
	* :ref:`dict Docker`
	* :ref:`dict Docker container`
	* :ref:`dict Docker image`
	* :ref:`dict Dockerfile`
	* :ref:`dict Dockstore CLI`
	* :ref:`dict Dockstore GitHub App`
	* :ref:`dict DOI`
	* :ref:`dict DS-I Africa`
	* :ref:`dict EC2`
	* :ref:`dict egress`
	* :ref:`dict eLwazi`
	* :ref:`dict entry`
	* :ref:`dict faceted search`
	* :ref:`dict FAIR`
	* :ref:`dict GA4GH`
	* :ref:`dict Galaxy`
	* :ref:`dict Galaxy workflow`
	* :ref:`dict GCP`
	* :ref:`dict Gen3`
	* :ref:`dict GitHub App registration`
	* :ref:`dict GitHub App tool`
	* :ref:`dict GitHub App workflow`
	* :ref:`dict immutable`
	* :ref:`dict interoperable`
	* :ref:`dict JSON`
	* :ref:`dict Jupyter`
	* :ref:`dict kernel`
	* :ref:`dict Kids First`
	* :ref:`dict labels`
	* :ref:`dict launch with`
	* :ref:`dict layer`
	* :ref:`dict legacy registration`
	* :ref:`dict legacy tool`
	* :ref:`dict legacy workflow`
	* :ref:`dict NCI`
	* :ref:`dict NCPI`
	* :ref:`dict Nextflow`
	* :ref:`dict NFL`
	* :ref:`dict NHGRI`
	* :ref:`dict NHLBI`
	* :ref:`dict NIH`
	* :ref:`dict OICR`
	* :ref:`dict ORCID`
	* :ref:`dict organization`
	* :ref:`dict parameter file`
	* :ref:`dict preemptible`
	* :ref:`dict Seven Bridges`
	* :ref:`dict Spot Instance`
	* :ref:`dict Terra`
	* :ref:`dict TES`
	* :ref:`dict tool`
	* :ref:`dict UCSC`
	* :ref:`dict VM`
	* :ref:`dict WDL`
	* :ref:`dict workflow`
	* :ref:`dict Workflow Description Language`
	* :ref:`dict Workflow Execution Service`
	* :ref:`dict YAML`

.. _dict .dockstore.yml:

.dockstore.yml
--------------
	This file is part of :ref:`dict GitHub App registration`. It indexes workflows or tools within a repository, including their optional test parameter files, and the author(s) of said workflows or tools.  

Further reading: `<https://docs.dockstore.org/en/stable/assets/templates/template.html>`_  

.. updated 2022-05-16  



.. _dict AnVIL Project:

AnVIL Project
-------------
*abbreviation for* Analysis Visualization and Informatics Labspace  

	A cloud-based ecosystem funded by :ref:`dict NHGRI`, bringing together Dockstore, :ref:`dict Gen3`, :ref:`dict Terra`, :ref:`dict NCPI`, :ref:`dict Galaxy`, :ref:`dict Jupyter`, Seqr, and Bioconductor into an integrated platform. Sometimes referred to as just "the AnVIL" or "AnVIL".  

Further reading: `<https://anvilproject.org/>`_  

.. updated 2022-05-16  



.. _dict API:

API
---
*abbreviation for* Application Programmer Interface  

	A software-based intermediary used to exchange data, often between two different platforms. Communication between different cloud platforms is mediated by various APIs, such as :ref:`dict TES`.  


.. updated 2022-05-16  



.. _dict AWS:

AWS
---
*abbreviation for* Amazon Web Services  

	A provider of cloud services, most notably cloud computing and cloud storage, available on-demand and hosted by Amazon. :ref:`dict Seven Bridges` is an example of a system that is powered by AWS, and can launch workflows on :ref:`dict EC2` instances.  

see also :ref:`dict GCP`  

Further reading: `<https://docs.aws.amazon.com/index.html?nc2=h_ql_doc_do>`_  

.. updated 2022-05-16  



.. _dict BD Catalyst:

BD Catalyst
-----------
*abbreviation for* :ref:`dict BioData Catalyst`  


.. updated 2022-05-16  



.. _dict BDC:

BDC
---
pronounced "bee-dee-see"  

*abbreviation for* :ref:`dict Biodata Catalyst`  


.. updated 2022-05-16  



.. _dict Biodata Catalyst:

Biodata Catalyst
----------------
	An initiative funded by :ref:`dict NHLBI` to connect several cloud-based bioinformatics platforms together to increase reproducibility in bioinformatics. Involves Dockstore, :ref:`dict Terra`, Seven Bridges, Gen3, and PIC-SURE.  

Further reading: `<https://biodatacatalyst.nhlbi.nih.gov/>`_  

.. updated 2022-05-16  



.. _dict Cancer Genomics Cloud:

Cancer Genomics Cloud
---------------------
	A cloud platform by :ref:`dict Seven Bridges` and funded by :ref:`dict NCI` for bioinformatics analysis.  


.. updated 2022-05-16  



.. _dict categories:

categories
----------
	A group of workflows or tools on Dockstore with a similar scientific purpose.  


.. updated 2022-05-16  



.. _dict CGC:

CGC
---
*abbreviation for* :ref:`dict Cancer Genomics Cloud`  


.. updated 2022-05-16  



.. _dict CLI:

CLI
---
*abbreviation for* Command Line Interface  

	A program that can be interacted with on the command line, usually via "Terminal" on MacOS and Linux or "cmd"/Command Prompt on Windows. CLI programs generally do not have a graphical user interface.  

Further reading: `<https://en.wikipedia.org/wiki/Command-line_interface>`_  

.. updated 2022-05-16  



.. _dict cloud computing:

cloud computing
---------------
	Doing computational tasks on a remote machine that is made available on-demand without the user having to manage all aspects of it. Generally implies that the user is essentially renting computational resources from someone else. Well-known cloud providers include :ref:`dict GCP`, :ref:`dict AWS`, Microsoft Azure, and Alibaba Cloud.  

Further reading: `<https://en.wikipedia.org/wiki/Cloud_computing>`_  

.. updated 2022-05-16  



.. _dict collections:

collections
-----------
	A group of workflows or tools on Dockstore associated with a particular :ref:`dict organization`.  


.. updated 2022-05-16  



.. _dict Common Workflow Language:

Common Workflow Language
------------------------
	A workflow language that describes how to run command-line tools. CWL is based on Java and can use Java commands within its own commands. :ref:`dict WDL` and CWL are relatively similar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features.  

see also :ref:`dict CWL`  

Further reading: `<https://www.commonwl.org/user_guide/>`_  

.. updated 2022-05-16  



.. _dict container:

container
---------
	An emulated computer system that contains programs and their prerequisites, but does not contain the entire operating system. Unlike a :ref:`dict VM`, a container shares the same kernel as the host OS. A well known type of container is a :ref:`dict Docker container`.  


.. updated 2022-05-16  



.. _dict Cromwell:

Cromwell
--------
	An open-source :ref:`dict WDL` executor managed by the Broad Institute. Cromwell is the default executor for the :ref:`dict Dockstore CLI` and is the executor used by :ref:`dict Terra`.  

.. note:: This term as we define it here is associated with Broad Institute and may have different definitions in other contexts.  

Further reading: `<https://cromwell.readthedocs.io/en/stable/>`_  

.. updated 2022-05-16  



.. _dict CWL:

CWL
---
*abbreviation for* :ref:`dict Common Workflow Language`  


.. updated 2022-05-16  



.. _dict DAG:

DAG
---
*abbreviation for* Directed Acyclic Graph  

	A directional graph like a flowchart that does not have any loops. On Dockstore we use DAGs to show the steps that a workflow takes.  

Further reading: `<https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html>`_  

.. updated 2022-05-16  



.. _dict descriptor file:

descriptor file
---------------
	A file used to programmatically describe a tool or workflow. This file represents the instructions that will actually be executed. On Dockstore, we support .ga, .cwl, .wdl, and .nfl file extensions for :ref:`dict Galaxy`, :ref:`dict CWL`, :ref:`dict WDL`, and :ref:`dict Nextflow` respectively.  


.. updated 2022-05-16  



.. _dict Docker:

Docker
------
pronounced "daw-ker", rhymes with walker  

	A program that can create "images" which are somewhat similar to virtual machines, as well as run those images. In the context of bioinformatics, this technology has two main benefits: First, a :ref:`dict Docker image` bundles up everything a given piece of software needs to run, meaning that someone who wants to run (for example) samtools via Docker only needs to install Docker, not samtools. Second, an instance of a Docker image is a relatively standardized environment even when running on different backends, meaning that two people running the same software in the same Docker image on two different computers are likely to get the exact same results. In other words, Docker is good for reproducibility and ease of use.  

Further reading: `<https://docker-curriculum.com/>`_  

.. updated 2022-05-16  



.. _dict Docker container:

Docker container
----------------
	In order to actually use the software inside a :ref:`dict Docker image` using the `docker run` command, the Docker program creates a writable :ref:`dict layer` on top of the image, which leads to the creation of a :ref:`dict Docker container`. You can think of a Docker image as an unchanging template, and a Docker container as a writable instance generated from that template. A Docker image can exist on its own, but a Docker container requires a Docker image.  

Further reading: `<https://www.docker.com/resources/what-container/>`_  

.. updated 2022-05-16  



.. _dict Docker image:

Docker image
------------
	A read-only file that represents a filesystem that contains some sort of code and that code's dependencies. A Docker image can be created using the `docker build` command in conjunction with a :ref:`dict Dockerfile`. If a workflow language references a Docker image, then the workflow executor will download that Docker image (unless was already downloaded previously) and add a writable layer onto the Docker image, which results in the creation of a :ref:`dict Docker container`.  


.. updated 2022-05-16  



.. _dict Dockerfile:

Dockerfile
----------
	A file describing the creation of a :ref:`dict Docker image` by running commands that each form a :ref:`dict layer`.  

Further reading: `<https://docs.docker.com/engine/reference/builder/>`_  

.. updated 2022-05-16  



.. _dict Dockstore CLI:

Dockstore CLI
-------------
*abbreviation for* Dockstore Command Line Interface  

	A command-line program developed by Dockstore. It is not required to use Dockstore, but it has many features to make running and developing workflows easier.  

see also :ref:`dict CLI`  

Further reading: `<https://docs.dockstore.org/en/stable/advanced-topics/dockstore-cli/dockstore-cli-faq.html>`_  

.. updated 2022-05-16  



.. _dict Dockstore GitHub App:

Dockstore GitHub App
--------------------
	The GitHub App that allows for Dockstore to communicate with GitHub repositories.  

see also :ref:`dict GitHub App registration`  

.. updated 2022-05-16  



.. _dict DOI:

DOI
---
*abbreviation for* Digital Object Identifier  

	An identifier that provides a long-lasting link to some sort of :ref:`dict immutable` digital object. On Dockstore, you can use Zenodo to mint a DOI of your workflows and tools to increase reproducibility.  


.. updated 2022-05-16  



.. _dict DS-I Africa:

DS-I Africa
-----------
*abbreviation for* Data Science for health discovery and Innovation in Africa  

	An :ref:`dict NIH` initiative to leverage data science to address the African continent's public health needs.  

Further reading: `<https://commonfund.nih.gov/africadata>`_  

.. updated 2022-05-16  



.. _dict EC2:

EC2
---
*abbreviation for* Elastic Compute Cloud  

	The cloud computing side of :ref:`dict AWS`. When running workflows on these backends, disk size will scale with your workflow requirements automatically. EC2 instances allow you to make use of Amazon's :ref:`dict spot instance` feature, which may reduce the cost of running workflows.  

Further reading: `<https://docs.aws.amazon.com/ec2/index.html>`_  

.. updated 2022-05-16  



.. _dict egress:

egress
------
pronounced "ee-gress", rhymes with aggress  

	The action of leaving a place. In the context of :ref:`dict cloud computing`, an egress charge is a fee charged for downloading a file. Sometimes, the person hosting the file is charged for data egress. Other times, the person downloading the file is charged.  

.. note:: This term as we define it here is associated with cloud computing and may have different definitions in other contexts.  

.. updated 2022-05-16  



.. _dict eLwazi:

eLwazi
------
pronounced "el-woz-ee", derived from the Xhosa word for knowledge (uLwazi) and the Luganda word for rock symbolizing robustness (Olwazi)  

	An African-lead open data science platform funded as part of the :ref:`dict NIH`'s :ref:`dict DS-I Africa` program. Leverages :ref:`dict Gen3` and :ref:`dict Terra`.  

Further reading: `<https://elwazi.org/>`_  

.. updated 2022-05-16  



.. _dict entry:

entry
-----
	A :ref:`dict tool` or :ref:`dict workflow` on Dockstore. A single entry on Dockstore has a description, a link to the original source-control repository, and at least one :ref:`dict descriptor file` which does some sort of computational task using :ref:`dict CWL`, :ref:`dict WDL`, :ref:`dict Nextflow`, or :ref:`dict Galaxy workflow` syntax. An entry can optionally include a :ref:`dict parameter file` that links to open-access test data. A single entry will include all versions of the tool or workflow that has been registered, with that versioning being based upon the versioning and branches of the source-control repository the descriptor file is hosted on (with the exception of a :ref:`dict legacy tool`, which have versioning based upon their Docker image tags), and any version can be pinned as the default. Entries can be added to :ref:`dict collections` associated with a particular :ref:`dict organization`, or added to :ref:`dict categories` so they can be grouped with other entries that have a similar scientific purpose. Entries may also have :ref:`dict labels` attached to them to help them be found via Dockstore's :ref:`dict faceted search` feature. If the entry is registered using the :ref:`dict Dockstore GitHub App`, then the entry will stay in sync automatically with the source-control repository. Additionally, if an entry is a valid :ref:`dict workflow`, any user can use our :ref:`dict launch with` feature to import the workflow to one of our cloud compute partners.  

.. note:: This term as we define it here is associated with Dockstore and may have different definitions in other contexts.  

.. updated 2022-05-16  



.. _dict faceted search:

faceted search
--------------
	A type of search which allows users to narrow down their results based upon certain aspects of the things being searched. On Dockstore, our faceted search at <https://dockstore.org/search> allows users to narrow down their search to a particular workflow language, author, or other fields.  

Further reading: `<https://en.wikipedia.org/wiki/Faceted_search>`_  

.. updated 2022-05-16  



.. _dict FAIR:

FAIR
----
pronounced "fair", rhymes with pear  

*abbreviation for* Findable, Accessible, Interoperable, and Reusable  

	A set of guidelines to improve the Findability, Accessibility, Interoperability, and Reuse of digital assets. This concept is often applied to data, but can be applied to other assets such as workflows.  

Further reading: `<https://www.go-fair.org/fair-principles/>`_  

.. updated 2022-05-16  



.. _dict GA4GH:

GA4GH
-----
*abbreviation for* Global Alliance For Genomics and Health  

	A network of public and private institutions which aims to accelerate progress in genomic research and human health by cultivating a common framework of standards and harmonized approaches for effective and responsible genomic and health-related data sharing.  

Further reading: `<https://www.ga4gh.org/>`_  

.. updated 2022-05-16  



.. _dict Galaxy:

Galaxy
------
	An open-source platform that uses :ref:`dict FAIR` principles, most well-known for its web-based UI which can be used to run a variety of bioinformatics tools.  

Further reading: `<https://galaxyproject.org/>`_  

.. updated 2022-05-16  



.. _dict Galaxy workflow:

Galaxy workflow
---------------
	A type of :ref:`dict workflow` that follows the standards of the :ref:`dict Galaxy` execution system. Dockstore supports the registration of Galaxy workflows with the file extension .ga  

Further reading: `<https://galaxyproject.org/learn/advanced-workflow/>`_  

.. updated 2022-05-16  



.. _dict GCP:

GCP
---
*abbreviation for* Google Cloud Platform  

	A backend used for cloud computing and cloud storage hosted by Google. :ref:`dict Terra` is an example of a system that runs on a GCP backend. When running workflows on these backends, make sure to account for the storage needed for your workflow, as GCP compute backends do not automatically scale their storage size at runtime. GCP backends allow you to make use of Google's :ref:`dict preemptible` feature, which may reduce the cost of running workflows.  

see also :ref:`dict EC2`  

Further reading: `<https://cloud.google.com/gcp>`_  

.. updated 2022-05-16  



.. _dict Gen3:

Gen3
----
	A data science platform affiliated with the University of Chicago. Hosts phenotypic and genotypic data for the :ref:`dict BD Catalyst`, :ref:`dict AnVIL Project`, :ref:`dict Kids First`, and :ref:`dict eLwazi` grants.  

Further reading: `<https://gen3.org/>`_  

.. updated 2022-05-16  



.. _dict GitHub App registration:

GitHub App registration
-----------------------
	The recommended way to register a :ref:`dict tool` or :ref:`dict workflow` on Dockstore. This involves creating a :ref:`dict .dockstore.yml` file on the GitHub repository (other source-control methods are not supported) that hosts the tool or workflow, as well as installing the Dockstore GitHub App. This allows a Dockstore entry to remain in sync with the source-control repository automatically, including new branches, tagged commits, and releases created on GitHub after registration of the entry.  

.. note:: This term as we define it here is associated with Dockstore and may have different definitions in other contexts.  

.. updated 2022-05-16  



.. _dict GitHub App tool:

GitHub App tool
---------------
	A :ref:`dict tool` registered using the Dockstore GitHub App.  

.. note:: This term as we define it here is associated with Dockstore and may have different definitions in other contexts.  

see also :ref:`dict GitHub App registration`  

.. updated 2022-05-16  



.. _dict GitHub App workflow:

GitHub App workflow
-------------------
	A :ref:`dict workflow` registered with the Dockstore GitHub App.  

.. note:: This term as we define it here is associated with Dockstore and may have different definitions in other contexts.  

see also :ref:`dict GitHub App registration`  

.. updated 2022-05-16  



.. _dict immutable:

immutable
---------
	Unchanging, unable to be modified. Immutability implies that an object cannot be updated.  


.. updated 2022-05-16  



.. _dict interoperable:

interoperable
-------------
	The ability of data or tools from multiple resources to effectively integrate data, or operate processes, across all systems with a moderate degree of effort.  


.. updated 2022-05-16  



.. _dict JSON:

JSON
----
pronounced "jason"  

*abbreviation for* JavaScript Object Notation  

	A human-readable file format that originated in JavaScript, but is now used by a variety of applications. Dockstore supports the inclusion of JSON and :ref:`dict YAML` files in entries to provide sample inputs for workflow and tool entries. Some workflow executors, such as :ref:`dict Cromwell`, can use these files to configure their inputs rather than having to manually listing every input when calling the workflow on the command line.  

see also :ref:`dict YAML`  

Further reading: `<https://www.json.org/json-en.html>`_  

.. updated 2022-05-16  



.. _dict Jupyter:

Jupyter
-------
pronounced "Jupiter" like the planet  

	A project focused on developing "notebooks" for programming languages, most famously Python due to it starting as a splinter of iPython in the early 2010s, but including other languages as well such as R. Jupyter notebooks allow for blocks of code to be nestled between markdown text, allowing for easy documentation of the code blocks and reproducibility of analysis.  

Further reading: `<https://jupyter.org/>`_  

.. updated 2022-05-16  



.. _dict kernel:

kernel
------
	An operating system's core program that is always loaded in memory, and modulates interactions between software and physical hardware, including but not limited to managing memory access for any program currently in RAM.  

Further reading: `<https://en.wikipedia.org/wiki/Kernel_(operating_system)>`_  

.. updated 2022-05-16  



.. _dict Kids First:

Kids First
----------
*abbreviation for* Gabriella Miller Kids First Program  

	An :ref:`dict NIH` program, supported by the NIH Common Fund, relating to the influence of genomics on pediatric health, with a focus on pediatric cancer and structural birth abnormalities (such as cleft palate).  

Further reading: `<https://commonfund.nih.gov/kidsfirst/highlights>`_  

.. updated 2022-05-16  



.. _dict labels:

labels
------
	On Dockstore, we use labels to "tag" Dockstore entries with information about them. You can add labels to a Dockstore :ref:`dict entry` page that you have edit access to. Labels cannot contain spaces.  


.. updated 2022-05-16  



.. _dict launch with:

launch with
-----------
	On Dockstore, this refers to the functionality of exporting a :ref:`dict workflow` to one of our cloud execution partners.  


.. updated 2022-05-16  



.. _dict layer:

layer
-----
	In the context of Docker, a layer is a component of a Docker image. Each `RUN`, `COPY`, and `ADD` instruction in a :ref:`dict Dockerfile` will lead to the creation of a layer.  

.. note:: This term as we define it here is associated with Docker and may have different definitions in other contexts.  

Further reading: `<https://docs.docker.com/storage/storagedriver/#images-and-layers>`_  

.. updated 2022-05-16  



.. _dict legacy registration:

legacy registration
-------------------
	One of the two main ways of registering a :ref:`dict tool` or :ref:`dict workflow`. Legacy methods support a variety of source-control repositories, but new changes to the tool or workflow after registration will not be reflected on Dockstore until the maintainer of the Dockstore :ref:`dict entry` manually refreshes the tool or workflow in Dockstore's UI. For this reason, we generally recommend people use :ref:`dict GitHub App registration` instead.  

.. note:: This term as we define it here is associated with Dockstore and may have different definitions in other contexts.  

.. updated 2022-05-16  



.. _dict legacy tool:

legacy tool
-----------
	On Dockstore, we use this term to refer to a :ref:`dict tool` that is registered using a :ref:`dict legacy registration` method. Legacy tools are not automatically synchronized with their source control repository, but can be updated manually by the tool maintainer. Additionally, legacy tools require a :ref:`dict Dockerfile` to be registered, and are versioned based on the tags of their associated :ref:`dict Docker image`. A legacy tool can be converted into a :ref:`dict GitHub App tool` via the following process: <https://docs.dockstore.org/en/stable/getting-started/github-apps/migrating-tools-to-github-apps.html>  

.. note:: This term as we define it here is associated with Dockstore and may have different definitions in other contexts.  

.. updated 2022-05-16  



.. _dict legacy workflow:

legacy workflow
---------------
	On Dockstore, we use this term to refer to a :ref:`dict workflow` that is registered using a :ref:`dict legacy registration` method. Legacy workflows are not automatically synchronized with their source control repository, but can be updated manually by the workflow maintainer. A legacy workflow can be converted into a :ref:`dict GitHub App workflow` via the following process: <https://docs.dockstore.org/en/stable/getting-started/github-apps/migrating-workflows-to-github-apps.html>  

.. note:: This term as we define it here is associated with Dockstore and may have different definitions in other contexts.  

.. updated 2022-05-16  



.. _dict NCI:

NCI
---
*abbreviation for* National Cancer Institute  

	A division of the :ref:`dict NIH` focused on cancer research.  

Further reading: `<https://www.nih.gov/about-nih/what-we-do/nih-almanac/national-cancer-institute-nci>`_  

.. updated 2022-05-16  



.. _dict NCPI:

NCPI
----
*abbreviation for* NIH Cloud Platform Interoperability  

	An effort to connect five :ref:`dict NIH` cloud projects and ensure they are interoperable. The five projects covered under this are the :ref:`dict AnVIL Project`, :ref:`dict BioData Catalyst`, Cancer Research Data Commons, Kids First, and the National Center for Biotechnology Information.  

.. note:: This term as we define it here is associated with NIH and may have different definitions in other contexts.  

Further reading: `<https://datascience.nih.gov/nih-cloud-platform-interoperability-effort>`_  

.. updated 2022-05-16  



.. _dict Nextflow:

Nextflow
--------
	A Java-based computational workflow engine. Dockstore supports the hosting of Nextflow workflows.  

Further reading: `<https://www.nextflow.io/>`_  

.. updated 2022-05-16  



.. _dict NFL:

NFL
---
*abbreviation for* :ref:`dict Nextflow`  

	An uncommon acronym for :ref:`dict Nextflow`. This abbreviation is not used as frequently as :ref:`dict CWL` or :ref:`dict WDL`, but does see usage occasionally.  


.. updated 2022-05-16  



.. _dict NHGRI:

NHGRI
-----
*abbreviation for* National Human Genome Research Institute  

	A division of the :ref:`dict NIH` that focus on genomics research. Funds the :ref:`dict AnVIL Project`.  

Further reading: `<https://www.genome.gov/>`_  

.. updated 2022-05-16  



.. _dict NHLBI:

NHLBI
-----
*abbreviation for* National Heart, Lungs, and Blood Institute  

	A division of the :ref:`dict NIH` that focuses on heart, lung, blood, and sleep health. Funds the :ref:`dict BioData Catalyst` platform.  

Further reading: `<https://www.nhlbi.nih.gov/>`_  

.. updated 2022-05-16  



.. _dict NIH:

NIH
---
*abbreviation for* National Institute of Health  

	An American government institution, part of the Department of Health and Human Services (HHS), that engages in medical research.  

Further reading: `<https://www.nih.gov/>`_  

.. updated 2022-05-16  



.. _dict OICR:

OICR
----
*abbreviation for* Ontario Institute for Cancer Research  

	A non-profit research institute based in Toronto that is focused on cancer detection and treatment. One of the two institutes involved in the development of Dockstore, the other being :ref:`dict UCSC`.  

Further reading: `<https://oicr.on.ca/>`_  

.. updated 2022-05-16  



.. _dict ORCID:

ORCID
-----
pronounced "or-kid", rhymes with kid  

*abbreviation for* Open Researcher and Contributor ID  

	ID used to identify researchers and their work in a way that doesn't solely rely on names.  

Further reading: `<https://info.orcid.org/what-is-orcid/>`_  

.. updated 2022-05-16  



.. _dict organization:

organization
------------
	In the context of Dockstore, an organization is a representation of some sort of institute, grant, project, or company. Organizations are created by Dockstore admins, but any user with at least two external accounts linked to their Dockstore account can request the creation of an organization on Dockstore.  

Further reading: `<https://dockstore.org/organizations>`_  

.. updated 2022-05-16  



.. _dict parameter file:

parameter file
--------------
	A :ref:`dict JSON` or :ref:`dict YAML` file that describes the inputs to a workflow. This usually includes internal links, or links to data in a Google or S3 bucket.  


.. updated 2022-05-16  



.. _dict preemptible:

preemptible
-----------
	A type of :ref:`dict GCP` :ref:`dict VM` which may have its running jobs interrupted at any given time, and will be shut down if running for more than 24 hours. A preemptible machine is significantly cheaper than a standard VM, at the cost of possibly stopping before your computational work is finish. You can use preemptible machines when running workflows on GCP backends to save on compute costs.  

.. note:: This term as we define it here is associated with Google and may have different definitions in other contexts.  

see also :ref:`dict spot instance`  

Further reading: `<https://cloud.google.com/compute/docs/instances/preemptible>`_  

.. updated 2022-05-16  



.. _dict Seven Bridges:

Seven Bridges
-------------
	A cloud-based workflow execution platform developed by Seven Bridges Genomics. Seven Bridges supports the execution of :ref:`dict CWL` workflows and features a graph-based GUI to make workflow development easier. The computational backend of a Seven Bridges workspace can be selected by the user, with both :ref:`dict GCP` and :ref:`dict AWS` being supported. Dockstore supports directly importing :ref:`dict CWL` workflows into a Seven Bridges workspace. Seven Bridges is part of the :ref:`dict BioData Catalyst` grant.  

see also :ref:`dict Terra`  

Further reading: `<https://www.sevenbridges.com/platform/>`_  

.. updated 2022-05-16  



.. _dict Spot Instance:

Spot Instance
-------------
	A type of :ref:`dict EC2` instance which is usually much cheaper than the typical on-demand EC2 cost. A spot instance is not guaranteed to be available at any given time, as it is based upon currently unused EC2 availability.  

.. note:: This term as we define it here is associated with Amazon and may have different definitions in other contexts.  

see also :ref:`dict preemptible`  

Further reading: `<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html>`_  

.. updated 2022-05-16  



.. _dict Terra:

Terra
-----
	A cloud-based workflow execution platform developed by the Broad Institute. Terra supports the execution of :ref:`dict WDL` workflows, Jupyter/R notebooks, and integrated apps such as a DICOM-file viewer. The computational backend of a Terra workspace is based upon Google, allowing Google-specific features such as :ref:`dict preemptible` machines to be used in workflows. Dockstore supports directly importing :ref:`dict WDL` workflows into a Terra workspace. Terra is part of the :ref:`dict BioData Catalyst`, :ref:`dict AnVIL Project`, and :ref:`dict eLwazi` grants.  

see also :ref:`dict Seven Bridges`  

Further reading: `<https://terra.bio>`_  

.. updated 2022-05-16  



.. _dict TES:

TES
---
*abbreviation for* Task Execution Service  

	A standardized API developed by :ref:`dict GA4GH` for describing and executing batch execution tasks.  

Further reading: `<https://ga4gh.github.io/task-execution-schemas/docs/>`_  

.. updated 2022-05-16  



.. _dict tool:

tool
----
	A single command line program wrapped in a descriptor language. Languages that formally describe tools (such as :ref:`dict CWL`) may chain them together into a :ref:`dict workflow`.  

see also :ref:`dict workflow`  

Further reading: `<https://docs.dockstore.org/en/stable/getting-started/intro-to-dockstore-tools-and-workflows.html>`_  

.. updated 2022-05-16  



.. _dict UCSC:

UCSC
----
*abbreviation for* University of California, Santa Cruz  

	A public university located in Santa Cruz that is focused on undergraduate and graduate education and research. The Genomics Institute, a branch of UCSC's engineering department, is one of the two institutes involved in the development of Dockstore, the other being :ref:`dict OICR`.  

Further reading: `<https://ucsc.edu>`_  

.. updated 2022-05-16  



.. _dict VM:

VM
--
*abbreviation for* virtual machine  

	An emulated computer system that runs on another computer system. Usually implies that an entire operating system(s) (the guest OS) is being run on top of another operating system (the host OS) via the host's hypervisor. The hypervisor manages the execution of processes of the guest operating system. This is in contrast to a :ref:`dict container`, which do not involve hypervisors nor run entire guest operating systems.  

see also :ref:`dict container`  

.. updated 2022-05-16  



.. _dict WDL:

WDL
---
pronounced "widdle", rhymes with little  

*abbreviation for* :ref:`dict Workflow Description Language`  


.. updated 2022-05-16  



.. _dict workflow:

workflow
--------
	A command line program wrapped in a descriptor language, which usually has multiple steps. In :ref:`dict CWL`, a workflow is usually made up of multiple tools. Other languages consider a workflow to be the basic unit.  

see also :ref:`dict tool`  

Further reading: `<https://docs.dockstore.org/en/stable/getting-started/intro-to-dockstore-tools-and-workflows.html>`_  

.. updated 2022-05-16  



.. _dict Workflow Description Language:

Workflow Description Language
-----------------------------
	A workflow language managed by the Open WDL Project that is designed to describe command-line tools. Usually written as :ref:`dict WDL`. WDL and :ref:`dict CWL` are relatively similar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features.  

see also :ref:`dict WDL`  

Further reading: `<https://openwdl.org/>`_  

.. updated 2022-05-16  



.. _dict Workflow Execution Service:

Workflow Execution Service
--------------------------
	A standardized API developed by :ref:`dict GA4GH` for describing a standard programmatic way to run and manage workflows.  

Further reading: `<https://ga4gh.github.io/workflow-execution-service-schemas/>`_  

.. updated 2022-05-16  



.. _dict YAML:

YAML
----
*abbreviation for* YAML Ain't Markup Language  

	Human-readable data-serialization language. Commonly used for configuration files.  

see also :ref:`dict JSON`  

Further reading: `<https://yaml.org/>`_  

.. updated 2022-05-16  



