WES Tutorial for AWS AGC
========================
Amazon Web Services' (AWS) Amazon Genomics CLI (AGC) is a command line tool for launching cloud infrastructure
within AWS accounts that can be used to execute genomics workflows. The infrastructure deployed by AGC implements the WES
standard, and thus can be directly communicated with by using the Dockstore CLI.

Check out the official AGC `GitHub page <https://github.com/aws/amazon-genomics-cli>`_.

Download and Install AWS AGC
----------------------------
AGC provides a `quick-start guide <https://aws.github.io/amazon-genomics-cli/docs/getting-started/>`_ for initial setup
and getting familiar with the tool. The following workflow execution tutorials will cover all steps for using AGC once
it has been `installed <https://aws.github.io/amazon-genomics-cli/docs/getting-started/installation/>`_.

Tutorial Topics
----------------
The following WDL workflow tutorials will cover:

1. Deploying an AGC project and context
2. Configuring the Dockstore CLI to communicate with AGC infrastructure
3. Launching a workflow

.. note::

    1. AWS AGC requires a special JSON file to be passed as the test parameter file for workflows, this JSON is formatted as follows:

        .. code:: text

            {
                "workflowInputs": <pathToInputJSON>
            }

    2. AWS AGC references descriptor files by URLs. The Dockstore CLI references the primary descriptor in an execution request as a GA4GH Tool Registry Service (`TRS <https://github.com/ga4gh/tool-registry-service-schemas>`_) URL.
    The AGC infrastructure will only be able to access the file referenced by the TRS URL if the workflow is published (i.e. public) on Dockstore.

Configuring AGC and the Dockstore CLI
----------------------------------------
1. Create a file named ``agc-project.yaml`` that contains:

    .. code:: text

        name: dockstoreAgcTutorialProject
        data:
          - location: s3://human-pangenomics
            readOnly: true
        schemaVersion: 1
        contexts:
          ctx1:
            engines:
              - type: wdl
                engine: cromwell

This will create an AGC project named ``dockstoreAgcTutorialProject``, with a single context named ``ctx1``. The section containing

    .. code:: text

        data:
          - location: s3://human-pangenomics
            readOnly: true

configures the AGC contexts in this project to be able to read the AWS S3 bucket ``human-pangenomics``. This is an `open-access data <https://registry.opendata.aws/>`_
bucket that will be used for one of the following example workflows.

.. note::

    For AGC infrastructure to interact with an S3 resource, the desired S3 bucket must be specified in the project's ``agc-project.yaml`` file
    and your AWS account must already have access to the S3 resource.


2. Activate AGC on your account. If this is your first time running AGC on an account, this may take a few minutes.

    .. code:: text

        agc account activate

3. Deploy an AGC context by running the below command in the same directory as ``agc-project.yaml``. This may take a few minutes.

    .. code:: text

        agc context deploy ctx1

4. Retrieve the WES endpoint created by the context. This will return a few values, the WES endpoint is the value under *WESENDPOINT*:

    .. code:: text

        agc context describe ctx1

    .. code:: text

        WESENDPOINT	https://example123.execute-api.us-west-2.amazonaws.com/prod/

5. Copy the WES endpoint into the Dockstore CLI config file located at ``~/.dockstore/config`` and append ``ga4gh/wes/v1`` to the end of the URL.
Your Dockstore CLI config file should have a named AWS profile included to allow the CLI to authorize requests to AWS. The resulting
config file will look similar to:

    .. code:: text

            [WES]
            url: https://example123.execute-api.us-west-2.amazonaws.com/prod/ga4gh/wes/v1
            authorization: aws-wes-profile
            type: aws

6. To verify that the Dockstore CLI is communicating with the AGC infrastructure, list the WES server info. A JSON response will be printed
to your terminal with the server's configuration.

    .. code:: text

        dockstore workflow wes service-info

.. note::
    At this point, the AGC infrastructure is deployed and the Dockstore CLI has been configured.

    The AGC context and Dockstore configuration file do not need to be modified for the remainder of these examples, and will continue to function until the resources are modified and/or destroyed.

Hello World Workflow
---------------------
The Dockstore entry associated with this workflow can be found here `agc-hello-world <https://dockstore.org/workflows/github.com/dockstore-testing/wes-testing/agc-hello-world:v1.12?tab=info>`_.

This WDL workflow prints out the string "Hello from AGC" as its output.

    *Dockstore.wdl*

    .. code:: text

            version 1.0
            workflow w {
                call hello {}
            }
            task hello {
                command { echo "Hello from AGC" }
                runtime {
                    docker: "ubuntu:latest"
                }
                output { String out = read_string( stdout() ) }
            }

1. Since this workflow is publicly posted on `Dockstore.org <https://dockstore.org/>`_, we can quickly launch it by passing the Dockstore CLI the entry name and its version:

    .. code:: text

        dockstore workflow wes launch --entry github.com/dockstore-testing/wes-testing/agc-hello-world:v1.12

2. The above command will return a unique run ID, similar to:

    .. code:: text

        8e8e9f4b-fb1a-41df-bc37-9396d6f97db5

    Copy the run ID and run the following to get the workflow run logs:

    .. code:: text

        dockstore workflow wes logs --id 8e8e9f4b-fb1a-41df-bc37-9396d6f97db5

    The logs returned will look similar to:

        .. code:: text

            {
              "run_id" : "8e8e9f4b-fb1a-41df-bc37-9396d6f97db5",
              "request" : {
                "workflow_params" : { },
                "workflow_type" : "WDL",
                "workflow_type_version" : "1.0",
                "tags" : null,
                "workflow_engine_parameters" : null,
                "workflow_url" : null
              },
              "state" : "COMPLETE",
              "run_log" : null,
              "task_logs" : [ {
                "name" : "w.hello|e6ce6c0a-ae99-43de-accc-4e43183de73f",
                "cmd" : [ "echo \"Hello from AGC\"" ],
                "start_time" : "2022-03-04T17:19:52.341Z",
                "end_time" : "2022-03-04T17:23:17.196Z",
                "stdout" : "s3://agc-example123-us-west-2/project/dockstoreAgcTutorialProject/userid/userM2QLG/context/ctx1/cromwell-execution/w/8e8e9f4b-fb1a-41df-bc37-9396d6f97db5/call-hello/hello-stdout.log",
                "stderr" : "s3://agc-example123-us-west-2/project/dockstoreAgcTutorialProject/userid/userM2QLG/context/ctx1/cromwell-execution/w/8e8e9f4b-fb1a-41df-bc37-9396d6f97db5/call-hello/hello-stderr.log",
                "exit_code" : 0
              } ],
              "outputs" : {
                "id" : "8e8e9f4b-fb1a-41df-bc37-9396d6f97db5",
                "outputs" : {
                  "w.hello.out" : "Hello from AGC"
                }
              }
            }

    Notice that the output for task ``hello`` of workflow ``w`` is "Hello from AGC".

FastQ Read Counts Workflow
--------------------------
The Dockstore entry associated with this workflow can be found here `agc-fastq-read-counts <https://dockstore.org/workflows/github.com/dockstore-testing/wes-testing/agc-fastq-read-counts:v1.12?tab=info>`_.

This WDL workflow tabulates read counts of the input fastq file.

    *Dockstore.wdl*

    .. code:: text

        version 1.0

        workflow fastqReadCounts {

            call countFastqReads

            output {
                File totalReadsFile = countFastqReads.totalReadsFile
            }
        }



        task countFastqReads {

            input {
                Array[File] inputFastq

                Int memSizeGB = 4
                Int diskSizeGB = 128
                String dockerImage = "biocontainers/samtools:v1.9-4-deb_cv1"
            }

            command <<<

                set -o pipefail
                set -e
                set -u
                set -o xtrace

                READ_COUNT=0

                for fq in ~{sep=' ' inputFastq}
                do
                      FILE_COUNT=$(zcat "${fq}" | wc -l )/4
                      READ_COUNT=$(( $READ_COUNT + $FILE_COUNT ))
                done

                echo $READ_COUNT > total_reads.txt
            >>>

            output {

                File totalReadsFile  = "total_reads.txt"
            }

            runtime {
                memory: memSizeGB + " GB"
                disks: "local-disk " + diskSizeGB + " SSD"
                docker: dockerImage
                preemptible: 1
            }
        }

1. This workflow takes an array of files as an input. Create a file named ``input.json`` in your working directory with contents:

    *input.json*

    .. code:: text

        {
            "fastqReadCounts.countFastqReads.inputFastq": ["s3://human-pangenomics/working/HPRC_PLUS/HG005/raw_data/Illumina/child/5A1-24481579/5A1_S5_L001_R1_001.fastq.gz"]
        }

2. As a requirement of AGC input parsing, create a second file named ``agcWrapper.json`` in your working directory.
   This file indicates which WES attachment will be used as the input JSON for the workflow execution step, in this case, ``input.json`` is our input file:

    *agcWrapper.json*

    .. code:: text

        {
            "workflowInputs": "input.json"
        }

3. Since this workflow is publicly posted on `Dockstore.org <https://dockstore.org/>`_, we can quickly launch it by passing the Dockstore CLI the entry and input files. File attachments can be specified with the ``--attach`` or ``-a`` switch:

    .. code:: text

        dockstore workflow wes launch --entry github.com/dockstore-testing/wes-testing/agc-fastq-read-counts:v1.12 --json agcWrapper.json -a input.json


4. The above command will return a unique run ID, similar to:

    .. code:: text

        b4e86806-2dc0-4d70-b494-52651e9b3de0

    Copy the run ID and run the following to get the workflow run logs:

    .. code:: text

        dockstore workflow wes logs --id b4e86806-2dc0-4d70-b494-52651e9b3de0

    The logs returned will look similar to:

    .. code:: text

        {
          "run_id" : "b4e86806-2dc0-4d70-b494-52651e9b3de0",
          "request" : {
            "workflow_params" : { },
            "workflow_type" : "WDL",
            "workflow_type_version" : "1.0",
            "tags" : null,
            "workflow_engine_parameters" : null,
            "workflow_url" : null
          },
          "state" : "COMPLETE",
          "run_log" : null,
          "task_logs" : [ {
            "name" : "fastqReadCounts.countFastqReads|XXXXX",
            "cmd" : [ null ],
            "start_time" : "2022-03-04T19:00:15.787Z",
            "end_time" : "2022-03-04T19:00:20.185Z",
            "stdout" : "s3://agc-example123-us-west-2/project/dockstoreAgcTutorialProject/userid/righanseM2QLG/context/ctx1/cromwell-execution/fastqReadCounts/b4e86806-2dc0-4d70-b494-52651e9b3de0/call-countFastqReads/countFastqReads-stdout.log",
            "stderr" : "s3://agc-example123-us-west-2/project/dockstoreAgcTutorialProject/userid/righanseM2QLG/context/ctx1/cromwell-execution/fastqReadCounts/b4e86806-2dc0-4d70-b494-52651e9b3de0/call-countFastqReads/countFastqReads-stderr.log",
            "exit_code" : 0
          } ],
          "outputs" : {
            "id" : "b4e86806-2dc0-4d70-b494-52651e9b3de0",
            "outputs" : {
              "fastqReadCounts.totalReadsFile" : "s3://agc-example123-us-west-2/project/dockstoreAgcTutorialProject/userid/userM2LQJ/context/ctx1/cromwell-execution/fastqReadCounts/b4e86806-2dc0-4d70-b494-52651e9b3de0/call-countFastqReads/cacheCopy/total_reads.txt"
            }
          }
        }

5. The output of this workflow is a text file containing a read count. To retrieve the file's contents, you can navigate to the S3 URL via the
AWS console, or copy the file contents using the AWS CLI:

    .. code:: text

        aws s3 cp s3://agc-example123-us-west-2/project/dockstoreAgcTutorialProject/userid/userM2LQJ/context/ctx1/cromwell-execution/fastqReadCounts/b4e86806-2dc0-4d70-b494-52651e9b3de0/call-countFastqReads/cacheCopy/total_reads.txt -

.. discourse::
    :topic_identifier: 90210
