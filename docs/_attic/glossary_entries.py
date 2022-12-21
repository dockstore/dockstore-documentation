# This file is called by _attic/glossary_generator.py to generate a glossary in RST format. 
# Its dependency, glossarpy, is currently maintained by Ash O'Farrell.
#
# To reference any entry here elsewhere in our documentation, use :ref:`dict x` where x is
# the name of the entry, with spaces. Example: :ref:`dict Amazon Genomics CLI`
#
# Style Guide:
# * glossary_generator.py will alphabetize entries in the rendered RST, but please try to keep this .py file in
#   alphabetical order for the sake of organization
# * Do not create newlines within strings (glossarpy can handle this but it makes tracking changes harder).
# * Do not use title case for the `name` of a GlossEntry; follow actual dictionary capitalization conventions
# * To link one GlossEntry to another in `definition` or `acronym_full` enclose the name (first positional arg)
#   of the entry to link in [brackets]
# * Due to RST limitations, do not make internal links plural
#   * acceptable: [WDL] [WDL], [WDL]. [WDL]'s [Seven Bridges] [Seven Bridges], [Seven Bridges]. [Seven Bridges]'s
#   * will break: [WDL]s [Seven Bridges]s

from glossarpy.GlossEntry import GlossEntry

dotDockstoredotYAML = GlossEntry(".dockstore.yml", 
	acronym_full="", 
	definition="This file is part of [GitHub App registration]. It indexes workflows or tools within a repository, including their optional test parameter files, and the author(s) of said workflows or tools.", 
	furtherreading="/assets/templates/template", 
	institute="", 
	pronunciation='')

AGC = GlossEntry("AGC",
	acronym_full="[Amazon Genomics CLI]")

AbsolutePath = GlossEntry("absolute path",
	definition="A path that starts with the character ``/`` and contains the full set of directories necessary to resolve a file, starting from the root directory of the repository or filesystem. For example: ``/Dockstore.cwl`` or ``/bin/sh``",
	furtherreading="",
	institute="",
	pronunciation='')

AmazonGenomicsCLI = GlossEntry("Amazon Genomics CLI", 
	definition="A [CLI]-based tool that supports launching bioinformatics-related workflows on [AWS] cloud infrastructure. The [Dockstore CLI] can launch workflows on AWS using Amazon Genomics CLI's [WES] implementation.", 
	furtherreading="https://aws.amazon.com/blogs/industries/announcing-amazon-genomics-cli-preview/", 
	institute="", 
	pronunciation='',
	seealso="[AGC]")

AnVIL = GlossEntry("AnVIL Project", 
	acronym_full="Analysis Visualization and Informatics Labspace", 
	definition="A federated cloud platform funded by [NHGRI] designed to manage and store genomics and related data, enable population-scale analysis, and facilitate collaboration through the sharing of data, code, and analysis results. Sometimes referred to as just \"the AnVIL\" or \"AnVIL\".", 
	furtherreading="https://anvilproject.org/", 
	institute="", 
	pronunciation="") 

API = GlossEntry("API", 
	acronym_full="Application Programmer Interface", 
	definition="A software connection or interface used to exchange data, often between two different platforms. Communication between different cloud platforms is mediated by various APIs, such as [TES].", 
	furtherreading="", 
	institute="", 
	pronunciation="")

AWS = GlossEntry("AWS", 
	acronym_full="Amazon Web Services", 
	definition="A provider of cloud services, most notably cloud computing and cloud storage, available on-demand and hosted by Amazon. Netflix and AirBnB are examples of a system that is powered by AWS. Some bioinformatics systems such as [Seven Bridges] can leverage AWS by launching workflows on [EC2] instances.", 
	furtherreading="https://docs.aws.amazon.com/index.html?nc2=h_ql_doc_do", 
	institute="", 
	pronunciation="", 
	seealso="[GCP]")

BDC = GlossEntry("BDC", 
	acronym_full="[BioData Catalyst]", 
	pronunciation='"bee-dee-see"')

BDCatalyst = GlossEntry("BD Catalyst", 
	acronym_full="[BioData Catalyst]")

BioDataCatalyst = GlossEntry("BioData Catalyst", 
	acronym_full="", 
	definition="A cloud-based platform funded by [NHLBI] to provide tools, applications, and workflows in secure workspaces to expand research in heart, lung, blood, and sleep health.", 
	furtherreading="https://biodatacatalyst.nhlbi.nih.gov/", 
	institute="", 
	pronunciation="")

CancerGenomicsCloud = GlossEntry("Cancer Genomics Cloud", 
	acronym_full="", 
	definition="A cloud platform by [Seven Bridges] and funded by [NCI] for bioinformatics analysis.", 
	furtherreading="", 
	institute="", 
	pronunciation="")

CGC = GlossEntry("CGC", 
	acronym_full="[Cancer Genomics Cloud]")

CLI = GlossEntry("CLI", 
	acronym_full="Command Line Interface", 
	definition="A program that can be interacted with on the command line, usually via \"Terminal\" on MacOS and Linux or \"cmd\"/Command Prompt on Windows. CLI programs generally do not have a graphical user interface.", 
	furtherreading="https://en.wikipedia.org/wiki/Command-line_interface", 
	institute="", 
	pronunciation="")

CloudComputing = GlossEntry("cloud computing", 
	acronym_full="", 
	definition="Doing computational tasks on a remote machine that is made available on-demand without the user having to manage all aspects of it. Generally implies that the user is essentially renting computational resources from someone else. Well-known cloud providers include [GCP], [AWS], Microsoft Azure, and Alibaba Cloud.", 
	furtherreading="https://en.wikipedia.org/wiki/Cloud_computing", 
	institute="", 
	pronunciation='')

Catagories = GlossEntry("categories", 
	acronym_full="", 
	definition="A group of workflows or tools curated by Dockstore with a similar scientific purpose.", 
	furtherreading="", 
	institute="", 
	pronunciation='')

Collections = GlossEntry("collection", 
	acronym_full="", 
	definition="A group of at least one [entry] on Dockstore that the members of an [organization] found useful, created themselves, or considered interesting. Each collection has a description, which you can read to see why the organization compiled workflows/tools in a collection", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='')

CommonWorkflowLanguage = GlossEntry("Common Workflow Language", 
	acronym_full="", 
	definition="A workflow language that describes how to run command-line tools. [WDL] and CWL are relatively similar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features. For example, CWL has the ability to use Javascript expressions within its own commands. CWL makes a distinction between a [tool] and a [workflow].", 
	furtherreading="https://www.commonwl.org/user_guide/", 
	institute="", 
	pronunciation="", 
	seealso="[CWL], [WDL]")

Container = GlossEntry("container", 
	acronym_full="", 
	definition="An emulated computer system that contains programs and their prerequisites, but does not contain the entire operating system. Unlike a [VM], a container shares the same kernel as the host OS. A well known type of container is a [Docker container].", 
	furtherreading="https://en.wikipedia.org/wiki/OS-level_virtualization", 
	institute="", 
	pronunciation='')

Cromwell = GlossEntry("Cromwell", 
	acronym_full="", 
	definition="An open-source [WDL] executor managed by the Broad Institute. Cromwell is the default [WDL] executor for the [Dockstore CLI] and is the executor used by [Terra].", 
	furtherreading="https://cromwell.readthedocs.io/en/stable/", 
	institute="Broad Institute", 
	pronunciation="",
	seealso="[miniwdl]")

CWL = GlossEntry("CWL", 
	acronym_full="[Common Workflow Language]")

cwltool = GlossEntry("cwltool", 
	acronym_full="", 
	definition="An open-source [CWL] executor which serves as the official reference implementation of [Common Workflow Language]. It is used by the [Dockstore CLI] to run CWL tools and workflows.", 
	furtherreading="https://github.com/common-workflow-language/cwltool", 
	institute="", 
	pronunciation="")

DAG = GlossEntry("DAG", 
	acronym_full="Directed Acyclic Graph", 
	definition="A directional graph like a flowchart that does not have any loops. On Dockstore we use DAGs to show the steps that a workflow takes.", 
	furtherreading="https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html", 
	institute="", 
	pronunciation="")

DescriptorFile = GlossEntry("descriptor file", 
	acronym_full="", 
	definition="A file used to programmatically describe a tool or workflow. This file represents the instructions that will actually be executed. On Dockstore, we support .ga, .cwl, .wdl, and .nfl file extensions for [Galaxy], [CWL], [WDL], and [Nextflow] respectively.", 
	furtherreading="", 
	institute="", 
	pronunciation='')

Docker = GlossEntry("Docker", 
	acronym_full="", 
	definition="A program that can create \"images\" which are somewhat similar to virtual machines, as well as run those images. In the context of bioinformatics, this technology has two main benefits: First, a [Docker image] bundles up everything a given piece of software needs to run, meaning that someone who wants to run (for example) samtools via Docker only needs to install Docker, not samtools. Second, an instance of a Docker image is a relatively standardized environment even when running on different backends, meaning that two people running the same software in the same Docker image on two different computers are likely to get the exact same results. In other words, Docker is good for reproducibility and ease of use.", 
	furtherreading="https://docker-curriculum.com/", 
	institute="", 
	pronunciation='"daw-ker", rhymes with walker')

DockerContainer = GlossEntry("Docker container", 
	acronym_full="", 
	definition="In order to actually use the software inside a [Docker image] using the `docker run` command, the Docker program creates a writable [layer] on top of the image, which leads to the creation of a [Docker container]. You can think of a Docker image as an unchanging template, and a Docker container as a writable instance generated from that template. A Docker image can exist on its own, but a Docker container requires a Docker image.", 
	furtherreading="https://www.docker.com/resources/what-container/", 
	institute="", 
	pronunciation="")

Dockerfile = GlossEntry("Dockerfile", 
	acronym_full="", 
	definition="A file describing the creation of a [Docker image] by running commands that each form a [layer].", 
	furtherreading="https://docs.docker.com/engine/reference/builder/", 
	institute="", 
	pronunciation="")

DockerImage = GlossEntry("Docker image", 
	acronym_full="", 
	definition="A read-only file that represents a filesystem that contains some sort of code and that code's dependencies. A Docker image can be created using the `docker build` command in conjunction with a [Dockerfile]. If a workflow language references a Docker image, then the workflow executor will download that Docker image (unless was already downloaded previously) and add a writable layer onto the Docker image, which results in the creation of a [Docker container].", 
	furtherreading="", 
	institute="", 
	pronunciation="")

DockstoreCLI = GlossEntry("Dockstore CLI", 
	acronym_full="Dockstore Command Line Interface", 
	definition="A command-line program developed by Dockstore. It is not required to use Dockstore, but it has many features to make running and developing workflows easier.", 
	furtherreading="/advanced-topics/dockstore-cli/dockstore-cli-faq", 
	institute="", 
	pronunciation="", 
	seealso="[CLI]")

DockstoreGHA = GlossEntry("Dockstore GitHub App", 
	acronym_full="", 
	definition="The GitHub App that allows for Dockstore to automatically sync changes made in a GitHub repository with an [entry] in Dockstore.", 
	furtherreading="/getting-started/github-apps/github-apps-landing-page", 
	institute="", 
	pronunciation='', 
	seealso="[GitHub App registration]")

DOI = GlossEntry("DOI", 
	acronym_full="Digital Object Identifier", 
	definition="An identifier that provides a long-lasting link to some sort of [immutable] digital object. On Dockstore, you can use Zenodo to mint a DOI of your workflows and tools to increase reproducibility. ", 
	furtherreading="", 
	institute="", 
	pronunciation="")

DRS = GlossEntry("DRS",
        acronym_full="Data Repository Service",
        definition="A standardized [API], created by the [GA4GH] Cloud Work Stream, that provides portable access to repositories of data resources.",
        furtherreading="https://github.com/ga4gh/data-repository-service-schemas",
        institute="GA4GH",
        pronunciation='"derse", rhymes with verse')

DSIAfrica = GlossEntry("DS-I Africa", 
	acronym_full="Data Science for health discovery and Innovation in Africa", 
	definition="An [NIH] initiative to leverage data science to address the African continent's public health needs.", 
	furtherreading="https://commonfund.nih.gov/africadata", 
	institute="", 
	pronunciation='')

EC2 = GlossEntry("EC2", 
	acronym_full="Elastic Compute Cloud", 
	definition="The cloud computing side of [AWS]. You can make use of Amazon's [spot instance] feature, which may reduce the cost of running workflows, when using EC2 instances.", 
	furtherreading="https://docs.aws.amazon.com/ec2/index.html", 
	institute="", 
	pronunciation='')

Egress = GlossEntry("egress", 
	acronym_full="", 
	definition="The action of leaving a place. In the context of [cloud computing], data egress refers to data being moved from one location to another, such as from the cloud to a local machine, between cloud providers, and between locations of a single cloud provider. Data egress often results in the charge of fees (usually called egress charges). Data egress can be one of the most expensive cloud costs incurred. Sometimes, the person hosting the file is charged for data egress. Other times, the person downloading the file is charged (such as when downloading files from a Google bucket that has the requester-pays option enabled).", 
	furtherreading="", 
	institute="cloud computing", 
	pronunciation='"ee-gress", rhymes with aggress')

Elwazi = GlossEntry("eLwazi", 
	acronym_full="", 
	definition="An African-lead open data science platform funded as part of the [NIH]'s [DS-I Africa] program.", 
	furtherreading="https://elwazi.org/",
	institute="", 
	pronunciation='"el-woz-ee", derived from the Xhosa word for knowledge (uLwazi) and the Luganda word for rock symbolizing robustness (Olwazi)')

Entry = GlossEntry("entry", 
	acronym_full="", 
	definition="Shorthand for a [tool] or [workflow] that has been registered on Dockstore.", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='')

EnvironmentVariable = GlossEntry("environment variable", 
	acronym_full="", 
	definition="A variable that affects how processes run on a computer. For example, [cwltool] references the environment variable $TMPDIR when deciding where to place files.", 
	furtherreading="https://en.wikipedia.org/wiki/Environment_variable",
	institute="", 
	pronunciation='')

FacetedSearch = GlossEntry("faceted search", 
	acronym_full="", 
	definition="A type of search which allows users to narrow down their results based upon certain aspects of the things being searched. On Dockstore, our faceted search at <https://dockstore.org/search> allows users to narrow down their search to a particular workflow language, author, and/or other fields.", 
	furtherreading="https://en.wikipedia.org/wiki/Faceted_search", 
	institute="", 
	pronunciation='')

FAIR = GlossEntry("FAIR", 
	acronym_full="Findable, Accessible, Interoperable, and Reusable", 
	definition="A set of guidelines to improve the Findability, Accessibility, Interoperability, and Reuse of digital assets. This concept is often applied to data, but can be applied to other assets such as workflows.", 
	furtherreading="https://www.go-fair.org/fair-principles/",
	institute="", 
	pronunciation='"fair", rhymes with pear')

GA4GH = GlossEntry("GA4GH", 
	acronym_full="Global Alliance For Genomics and Health", 
	definition="A network of public and private institutions which aims to accelerate progress in genomic research and human health by cultivating a common framework of standards and harmonized approaches for effective and responsible genomic and health-related data sharing.", 
	furtherreading="https://www.ga4gh.org/", 
	institute="", 
	pronunciation='')

Galaxy = GlossEntry("Galaxy", 
	acronym_full="", 
	definition="An open-source platform that uses [FAIR] principles, most well-known for its web-based UI used to create and run a variety of bioinformatics tools. A Galaxy `instance` is a running Galaxy interface/server that can be used to create and execute tools and workflows.",
	furtherreading="https://galaxyproject.org/", 
	institute="", 
	pronunciation='')

GalaxyWorkflow = GlossEntry("Galaxy workflow", 
	acronym_full="", 
	definition="A type of [workflow] that follows the standards of the [Galaxy] execution system. Dockstore supports the registration of Galaxy workflows with the file extension .ga", 
	furtherreading="https://galaxyproject.org/learn/advanced-workflow/", 
	institute="", 
	pronunciation='')

GCP = GlossEntry("GCP", 
	acronym_full="Google Cloud Platform", 
	definition="A system used for cloud computing and cloud storage hosted by Google. Well-known users of GCP include LinkedIn and Verizon, but GCP can also power bioinformatics. [Terra] is an example of a bioinformatics system that runs on a GCP backend. When running workflows on GCP backends, make sure to account for the storage needed for your workflow, as GCP compute backends do not automatically scale their storage size at runtime. GCP backends allow you to make use of Google's [preemptible] feature, which may reduce the cost of running workflows.", 
	furtherreading="https://cloud.google.com/gcp", 
	institute="", 
	pronunciation="", 
	seealso="[EC2]")

Gen3 = GlossEntry("Gen3", 
	acronym_full="", 
	definition="A data science platform affiliated with the University of Chicago. Hosts phenotypic and genotypic data for the [BD Catalyst], [AnVIL Project], [Kids First], and [eLwazi] grants.", 
	furtherreading="https://gen3.org/", 
	institute="", 
	pronunciation='')

GitHubAppRegistration = GlossEntry("GitHub App registration", 
	acronym_full="", 
	definition="The recommended way to register a [tool] or [workflow] on Dockstore. This involves creating a [.dockstore.yml] file on the GitHub repository (other source-control methods are not supported) that hosts the tool or workflow, as well as installing the [Dockstore GitHub App]. This allows a Dockstore entry to remain in sync with the source-control repository automatically, including new branches, tagged commits, and releases created on GitHub after registration of the entry.", 
	furtherreading="/getting-started/github-apps/github-apps-landing-page", 
	institute="Dockstore", 
	pronunciation='')

GitHubAppTool = GlossEntry("GitHub App tool", 
	acronym_full="", 
	definition="A [tool] registered using the [Dockstore GitHub App].", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='', 
	seealso="[GitHub App registration]")

GitHubAppWorkflow = GlossEntry("GitHub App workflow", 
	acronym_full="", 
	definition="A [workflow] registered with the [Dockstore GitHub App].", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='', 
	seealso="[GitHub App registration]")

Immutable = GlossEntry("immutable", 
	acronym_full="", 
	definition="Unchanging, unable to be modified. Immutability implies that an object cannot be updated.", 
	furtherreading="", 
	institute="", 
	pronunciation='')

Interoperable = GlossEntry("interoperable", 
	acronym_full="", 
	definition="The ability of data or tools from multiple resources to effectively integrate data, or operate processes, across all systems with a moderate degree of effort.", 
	furtherreading="", 
	institute="", 
	pronunciation="")

JSON = GlossEntry("JSON", 
	acronym_full="JavaScript Object Notation", 
	definition="A human-readable file format that originated in JavaScript, but is now used by a variety of applications. Dockstore supports the inclusion of JSON and [YAML] files in entries to provide sample inputs for workflow and tool entries. Some workflow executors, such as [Cromwell], can use these files to configure their inputs rather than having to manually listing every input when calling the workflow on the command line.", 
	furtherreading="https://www.json.org/json-en.html", 
	institute="", 
	pronunciation='"jason"', 
	seealso="[YAML]")

Jupyter = GlossEntry("Jupyter", 
	acronym_full="", 
	definition="A project focused on developing \"notebooks\" for programming languages, most famously Python due to it starting as a splinter of iPython in the early 2010s. Other languages such as R are also supported. Jupyter notebooks allow for blocks of code to be nestled between markdown text, allowing for easy documentation of the code blocks and reproducibility of analysis.", 
	furtherreading="https://jupyter.org/", 
	institute="", 
	pronunciation='"Jupiter" like the planet')

Kernel = GlossEntry("kernel", 
	acronym_full="", 
	definition="An operating system's core program that is always loaded in memory, and modulates interactions between software and physical hardware, including but not limited to managing memory access for any program currently in RAM.", 
	furtherreading="https://en.wikipedia.org/wiki/Kernel_(operating_system)", 
	institute="", 
	pronunciation='')

# I am purposely choosing the word "birth abnormalities" instead of "birth defects" and would prefer this
# definition not be changed to "birth defects" due to the fact Kids First also studies intersexuality.
# The concept of intersexuality as being a defect to always be "corrected" has lead to serious issues
# regarding bodily autonomy, gender identity, and informed consent.
KidsFirst = GlossEntry("Kids First", 
	acronym_full="Gabriella Miller Kids First Program", 
	definition="An [NIH] program, supported by the NIH Common Fund, relating to the influence of genomics on pediatric health, with a focus on pediatric cancer and structural birth abnormalities (such as cleft palate).", 
	furtherreading="https://commonfund.nih.gov/kidsfirst/highlights", 
	institute="", 
	pronunciation='')

Labels = GlossEntry("labels", 
	acronym_full="", 
	definition="On Dockstore, we use labels to \"tag\" Dockstore entries with information about them. Workflow or tool developers can add labels to a Dockstore [entry] page that they have edit access to. An entry's labels will appear in search results.", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='')

LaunchWith = GlossEntry("launch with", 
	acronym_full="", 
	definition="On Dockstore, this refers to the functionality of exporting a [workflow] to one of our cloud execution partners.", 
	furtherreading="", 
	institute="", 
	pronunciation='')

Layer = GlossEntry("layer", 
	acronym_full="", 
	definition="In the context of Docker, a layer is a component of a Docker image. Each `RUN`, `COPY`, and `ADD` instruction in a [Dockerfile] will lead to the creation of a layer.", 
	furtherreading="https://docs.docker.com/storage/storagedriver/#images-and-layers", 
	institute="", 
	pronunciation="")

LegacyRegistration = GlossEntry("legacy registration", 
	acronym_full="", 
	definition="One of the two main ways of registering a [tool] or [workflow]. Legacy methods support a variety of source-control repositories, but new changes to the tool or workflow after registration will not be reflected on Dockstore until the maintainer of the Dockstore [entry] manually refreshes the tool or workflow in Dockstore's UI. For this reason, we generally recommend people use [GitHub App registration] instead.", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='')

LegacyTool = GlossEntry("legacy tool", 
	acronym_full="",
	definition="On Dockstore, we use this term to refer to a [tool] that is registered using a [legacy registration] method. Legacy tools are not automatically synchronized with their source control repository, but can be updated manually by the tool maintainer. Additionally, legacy tools require a [Dockerfile] to be registered, and are versioned based on the tags of their associated [Docker image]. A legacy tool can be converted into a [GitHub App tool] via :doc:`the method described here </getting-started/github-apps/migrating-tools-to-github-apps>`.", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='')

LegacyWorkflow = GlossEntry("legacy workflow", 
	acronym_full="", 
	definition="On Dockstore, we use this term to refer to a [workflow] that is registered using a [legacy registration] method. Legacy workflows are not automatically synchronized with their source control repository, but can be updated manually by the workflow maintainer. A legacy workflow can be converted into a [GitHub App workflow] via :doc:`the method described here </getting-started/github-apps/migrating-workflows-to-github-apps>`.", 
	furtherreading="", 
	institute="Dockstore", 
	pronunciation='')

miniwdl = GlossEntry("miniwdl",
	definition="A Python-based [WDL] executor managed by the Chan Zuckerberg Initiative.",
	furtherreading="https://github.com/chanzuckerberg/miniwdl",
	institute="Chan Zuckerberg Initiative", 
	seealso="[Cromwell]")

NCI = GlossEntry("NCI", 
	acronym_full="National Cancer Institute ", 
	definition="A division of the [NIH] focused on cancer research.", 
	furtherreading="https://www.nih.gov/about-nih/what-we-do/nih-almanac/national-cancer-institute-nci", 
	institute="NIH", 
	pronunciation="")

NCPI = GlossEntry("NCPI", 
	acronym_full="NIH Cloud Platform Interoperability", 
	definition="An effort to connect five [NIH] cloud projects and ensure they are interoperable. The five projects covered under this are the [AnVIL Project], [BioData Catalyst], Cancer Research Data Commons, [Kids First], and the National Center for Biotechnology Information.",
	furtherreading="https://datascience.nih.gov/nih-cloud-platform-interoperability-effort", 
	institute="NIH", 
	pronunciation='')

Nextflow = GlossEntry("Nextflow", 
	acronym_full="", 
	definition="A Java-based computational workflow engine. Dockstore supports the hosting of Nextflow workflows.", 
	furtherreading="https://www.nextflow.io/", 
	institute="", 
	pronunciation='')

NFL = GlossEntry("NFL", 
	acronym_full="[Nextflow]", 
	definition="An uncommon acronym for [Nextflow]. This abbreviation is not used as frequently as [CWL] or [WDL], but does see usage occasionally.", 
	furtherreading="", 
	institute="", 
	pronunciation='')

NHGRI = GlossEntry("NHGRI", 
	acronym_full="National Human Genome Research Institute", 
	definition="A division of the [NIH] that focus on genomics research. Funds the [AnVIL Project].", 
	furtherreading="https://www.genome.gov/", 
	institute="NIH", 
	pronunciation="")

NHLBI = GlossEntry("NHLBI", 
	acronym_full="National Heart, Lungs, and Blood Institute", 
	definition="A division of the [NIH] that focuses on heart, lung, blood, and sleep health. Funds the [BioData Catalyst] platform.", 
	furtherreading="https://www.nhlbi.nih.gov/", 
	institute="NIH", 
	pronunciation="")

NIH = GlossEntry("NIH", 
	acronym_full="National Institutes of Health", 
	definition="An American government institution, part of the Department of Health and Human Services (HHS), that engages in medical research.", 
	furtherreading="https://www.nih.gov/", 
	institute="", 
	pronunciation="")

OICR = GlossEntry("OICR", 
	acronym_full="Ontario Institute for Cancer Research", 
	definition="A non-profit research institute based in Toronto that is focused on cancer detection and treatment. One of the two institutes involved in the development of Dockstore, the other being [UCSC].", 
	furtherreading="https://oicr.on.ca/", 
	institute="", 
	pronunciation="")

ORCID = GlossEntry("ORCID", 
	acronym_full="Open Researcher and Contributor ID", 
	definition="A unique ID used to identify researchers and their work in a way that doesn't solely rely on names.", 
	furtherreading="https://info.orcid.org/what-is-orcid/", 
	institute="", 
	pronunciation='"or-kid", rhymes with kid')

Organization = GlossEntry("organization", 
	acronym_full="", 
	definition="In the context of Dockstore, an organization is a representation of some sort of institute, grant, project, or company. Organizations are approved by Dockstore admins, but any user with at least two external accounts linked to their Dockstore account (and have the authority to speak for the institute, grant, etc. in a technical manner) can request the creation of an organization on Dockstore.", 
	furtherreading="https://dockstore.org/organizations", 
	institute="", 
	pronunciation='')

ParameterFile = GlossEntry("parameter file", 
	acronym_full="", 
	definition="A [JSON] or [YAML] file that describes the inputs to a workflow, such as runtime parameters or links to cloud data.", 
	furtherreading="", 
	institute="", 
	pronunciation='')

Preemptible = GlossEntry("preemptible", 
	acronym_full="", 
	definition="A type of [GCP] [VM] which may have its running jobs interrupted at any given time, and will be shut down if running for more than 24 hours. A preemptible machine is significantly cheaper than a standard VM, at the cost of possibly stopping before your computational work is finished. You can use preemptible machines when running workflows on GCP backends to save on compute costs.", 
	furtherreading="https://cloud.google.com/compute/docs/instances/preemptible", 
	institute="Google", 
	pronunciation='', 
	seealso="[spot instance]")

PrimaryDescriptorFile = GlossEntry("primary descriptor file",
	acronym_full="",
	definition="The [descriptor file] that provides the overall description of a workflow or tool, which Dockstore processes first when the workflow or tool is registered.",
	furtherreading="",
	institute="",
	pronunciation='')

SecondaryDescriptorFile = GlossEntry("secondary descriptor file",
	acronym_full="",
	definition="An ancillary [descriptor file], referenced by the [primary descriptor file] or another secondary descriptor file, that describes part of a workflow or tool.",
	furtherreading="",
	institute="",
	pronunciation='')

SevenBridges = GlossEntry("Seven Bridges", 
	acronym_full="", 
	definition="A cloud-based workflow execution platform developed by Seven Bridges Genomics. Seven Bridges supports the execution of [CWL] workflows and features a graph-based GUI to make workflow development easier. The computational backend of a Seven Bridges workspace can be selected by the user, with both [GCP] and [AWS] being supported. Dockstore supports directly importing [CWL] workflows into a Seven Bridges workspace. Seven Bridges is part of the [BioData Catalyst] consortium.", 
	furtherreading="https://www.sevenbridges.com/platform/", 
	institute="", 
	pronunciation='', 
	seealso="[Terra]")

SpotInstance = GlossEntry("Spot Instance", 
	acronym_full="", 
	definition="A type of [EC2] instance which is usually much cheaper than the typical on-demand EC2 cost. A spot instance is not guaranteed to be available at any given time, as it is based upon currently unused EC2 availability.", 
	furtherreading="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html", 
	institute="Amazon", 
	pronunciation='', 
	seealso="[preemptible]")

TaskExecutionService = GlossEntry("Task Execution Service", 
	definition="A standardized [API] developed by [GA4GH] for describing and executing batch execution tasks.", 
	furtherreading="https://ga4gh.github.io/task-execution-schemas/docs/",)

TES = GlossEntry("TES", 
	acronym_full="[Task Execution Service]")

Terra = GlossEntry("Terra", 
	acronym_full="", 
	definition="A cloud-based workflow execution platform developed by the Broad Institute. Terra supports the execution of [WDL] workflows, Jupyter/R notebooks, and integrated apps. The computational backend of a Terra workspace is based upon Google, allowing Google-specific features such as [preemptible] machines to be used in workflows. Dockstore supports directly importing [WDL] workflows into a Terra workspace. Terra is part of the [BioData Catalyst], [AnVIL Project], and [eLwazi] consortia.", 
	furtherreading="https://terra.bio", 
	institute="", 
	pronunciation="", 
	seealso="[Seven Bridges]")

Tool = GlossEntry("tool", 
	acronym_full="", 
	definition="A single command line program wrapped in a descriptor language.  Languages that formally describe tools (such as [CWL]) may chain them together into a [workflow].", 
	furtherreading="/getting-started/intro-to-dockstore-tools-and-workflows",
	institute="", 
	pronunciation='', 
	seealso="[workflow]")

TRS = GlossEntry("TRS",
        acronym_full="Tool Registry Service",
        definition="A standardized [API], created by the [GA4GH] Cloud Work Stream, that provides portable access to a registry of tools, workflows, and associated files.  Every resource in a TRS registry has a public ID that can be used to retrieve it.  Dockstore `provides <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20>`__ a TRS interface.",
        furtherreading="https://ga4gh.github.io/tool-registry-service-schemas/",
        institute="GA4GH",
        pronunciation='"terse", rhymes with verse')

UCSC = GlossEntry("UCSC", 
	acronym_full="University of California, Santa Cruz", 
	definition="A public university located in Santa Cruz that is focused on undergraduate and graduate education and research. The Genomics Institute, a branch of UCSC's engineering department, is one of the two institutes involved in the development of Dockstore, the other being [OICR].", 
	furtherreading="https://ucsc.edu", 
	institute="", 
	pronunciation="")

VM = GlossEntry("VM", 
	acronym_full="virtual machine", 
	definition="An emulated computer system that runs on another computer system. Usually implies that an entire operating system(s) (the guest OS) is being run on top of another operating system (the host OS) via the host's hypervisor. The hypervisor manages the execution of processes of the guest operating system. This is in contrast to a [container], which do not involve hypervisors nor run entire guest operating systems.", 
	furtherreading="", 
	institute="", 
	pronunciation='', 
	seealso="[container]")

WDL = GlossEntry("WDL",
	acronym_full="[Workflow Description Language]",
	pronunciation='"widdle", rhymes with riddle')

WES = GlossEntry("WES",
	acronym_full="[Workflow Execution Service]",
	pronunciation='"wes", rhymes with mess')

WorkflowExecutionService = GlossEntry("Workflow Execution Service",
	definition="A standardized [API] developed by [GA4GH] for describing a standard programmatic way to run and manage workflows. This standard, also known as [WES], can be launched using the [Dockstore CLI] as described in this Dockstore blog post: <https://medium.com/dockstore/dockstore-partners-with-aws-agc-to-make-launching-workflows-quick-and-easy-7213510dabd8>",
	furtherreading="https://ga4gh.github.io/workflow-execution-service-schemas/")

Workflow = GlossEntry("workflow", 
	acronym_full="", 
	definition="A command line program wrapped in a descriptor language, which usually has multiple steps. In [CWL], a workflow is usually made up of multiple tools. Other languages consider a workflow to be the basic unit.", 
	furtherreading="/getting-started/intro-to-dockstore-tools-and-workflows", 
	institute="", 
	pronunciation='', 
	seealso="[tool]")

Workflow_Description_Language = GlossEntry("Workflow Description Language",
	furtherreading="https://openwdl.org/",
	definition="A workflow language managed by the Open WDL Project that is designed to describe command line tools. Usually written as [WDL]. WDL and [CWL] are relatively similar in principle, and code written in one language can often be translated into the other with some workarounds, but they are two different standards and each have unique features. Unlike CWL, WDL does not have an official reference implementation, but [Cromwell] and [miniwdl] are popular implementations.",
	seealso="[WDL], [CWL]")

YAML = GlossEntry("YAML", 
	acronym_full="YAML Ain't Markup Language", 
	definition="Human-readable data-serialization language. Commonly used for configuration files.", 
	furtherreading="https://yaml.org/", 
	institute="", 
	pronunciation='"yah-mul", rhymes with camel', 
	seealso="[JSON]")
