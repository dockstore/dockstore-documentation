.. hint::
    Mac users, make note of this :ref:`FAQ <how-do-i-use-the-dockstore-cli-on-a-mac>` entry if you run into errors while going through the developer tutorials.

Introduction
============

This series is an introduction to everything required to properly use Dockstore as a contributor of workflows or tools. It is designed to be somewhat modular, so if you wish to jump into any individual topics, you may do so. But if you follow it in order, you'll learn an overview of how Docker and workflow languages like CWL, WDL, Nextflow, and Galaxy are changing how scientists use and create tools via a series of tutorials which goes through the whole process of:

- :doc:`Creating a Docker image that an analysis will run within </getting-started/getting-started-with-docker>`
- Describing a simple analysis with a descriptor file written in one the following languages: :doc:`CWL </getting-started/getting-started-with-cwl>`, :doc:`WDL </getting-started/getting-started-with-wdl>`, :doc:`Nextflow </getting-started/getting-started-with-nextflow>`, or :doc:`Galaxy </getting-started/getting-started-with-galaxy>`
- :doc:`Creating a Dockstore account </getting-started/register-on-dockstore>
- Registering :doc:`a tool </getting-started/dockstore-tools>` or :doc:`a workflow </getting-started/dockstore-workflows>` on Dockstore

The tool we will be using throughout this tutorial is
`BAMStats <http://bamstats.sourceforge.net/>`__. It is a tool for
summarising Next Generation Sequencing alignments. It accepts a BAM file
as input and produces a ZIP file containing an HTML report on the alignment.

Note that this tutorial series assumes you are running on a system that can run Docker. This isn't the case for all users, especially HPC users. Read :doc:`our notes on Docker alternatives </advanced-topics/docker-alternatives>` for more details.

.. discourse::
    :topic_identifier: 1281