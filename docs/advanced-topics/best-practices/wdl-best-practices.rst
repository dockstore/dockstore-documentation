WDL Best Practices
==================

Best Practices
--------------

Following are some best practices for creating tools. Our intention is
that this document will evolve as descriptor languages evolve so feel
free to provide suggestions and/or improvements.

In this tutorial, we will be using the same example from our getting started with WDL tutorial, `dockstore-tool-bamstats <https://github.com/CancerCollaboratory/dockstore-tool-bamstats/blob/develop/Dockstore.wdl>`__.

Authorship Metadata
-------------------

.. include:: authorship-metadata-intro.rst

This example includes author, email, and description metadata:

*/Dockstore.wdl*

::

    version 1.0
    task bamstats {
        input {
            File bam_input
            Int mem_gb
        }


        command {
            bash /usr/local/bin/bamstats ${mem_gb} ${bam_input}
        }

        output {
            File bamstats_report = "bamstats_report.zip"
        }

        runtime {
            docker: "quay.io/collaboratory/dockstore-tool-bamstats:1.25-6_1.0"
            memory: mem_gb + "GB"
        }

        meta {
            author: "Andrew Duncan"
            email: "Andrew.Duncan@oicr.on.ca"
            description: "![build_status](https://quay.io/repository/collaboratory/dockstore-tool-bamstats/status) A Docker container for the BAMStats command. See the [BAMStats](http://bamstats.sourceforge.net/) website for more information."
        }
    }

    workflow bamstatsWorkflow {
        input {
            File bam_input
            Int mem_gb
        }
        call bamstats { input: bam_input=bam_input, mem_gb=mem_gb }
    }

This results in the workflow's Info Tab being populated like:

.. figure:: /assets/images/docs/best_practices/wdl-info-tab-metadata.png
   :alt: wdl-info-tab-metadata

   wdl-info-tab-metadata

.. include:: sample-parameter-files-intro.rst

*test.wdl.json*

::

    {
      "bamstatsWorkflow.bam_input": "NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam",
      "bamstatsWorkflow.mem_gb": "4"
    }

Now invoke ``dockstore`` with the workflow wrapper and the input object
on the command line and ensure that it succeeds:

::

    $ dockstore workflow launch --local-entry wdl/bamqc.wdl --json test.wdl.json

    ...
    Calling out to Cromwell to run your workflow
    Executing: java -jar /Users/natalieperez/.dockstore/libraries/cromwell-44.jar run /Users/natalieperez/Projects/dockstore-tool-bamstats/Dockstore.wdl --inputs /var/folders/xq/7_kn047j4sb41bfb2_3nng4m0000gq/T/foo15775077532364354801json
    ...
    Cromwell exit code: 0
    Cromwell stdout:
    ...

Next Steps
----------

.. include:: authorship-metadata-outro.rst

.. discourse::
    :topic_identifier: 1546