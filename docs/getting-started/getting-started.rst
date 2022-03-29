.. hint::
    Mac users, make note of this :ref:`FAQ <how-do-i-use-the-dockstore-cli-on-a-mac>` entry if you run into errors while going through the developer tutorials.

Introduction
============

An introduction to everything required to properly use Dockstore as a contributor. Learn
about how Docker and workflow languages like CWL, WDL, Nextflow, Galaxy are changing how scientists use
and create tools via a series of tutorials which goes through the whole
process of:

- Creating a Docker image that an analysis will run within
- Describing a simple analysis with a descriptor file written in one the following languages: CWL, WDL, Nextflow, Galaxy
- Creating a Dockstore account
- Registering the descriptor files on Dockstore

The tool we will be using throughout this tutorial is
`BAMStats <http://bamstats.sourceforge.net/>`__. It is a tool for
summarising Next Generation Sequencing alignments. It accepts a BAM file
as input and produces a ZIP file containing an HTML report on the alignment.

.. discourse::
    :topic_identifier: 1281