WES Tutorial for running CWL workflows through the Toil Engine on AWS AGC
=========================================================================

.. note::
    Although the process for running WDL workflows through the Cromwell engine on AWS AGC is very similar to the process
    described in this tutorial, there are a few differences. For information on how to launch a WDL workflow on AWS
    AGC please consult this :doc:`tutorial <wes-wdl-agc-tutorial>`.

Amazon Web Services' (AWS) Amazon Genomics CLI (AGC) is a command line tool for launching cloud infrastructure
within AWS accounts that can be used to execute genomics workflows. The infrastructure deployed by AGC implements the WES
standard, and thus can be directly used by the Dockstore CLI.

Check out the official AGC `Info page <https://aws.github.io/amazon-genomics-cli>`_.

For developers, check out the official AGC `GitHub page <https://github.com/aws/amazon-genomics-cli>`_.

Download and Install AWS AGC
----------------------------
AGC provides a `quick-start guide <https://aws.github.io/amazon-genomics-cli/docs/getting-started/>`_ for initial setup
and getting familiar with the tool. The following workflow execution tutorial will cover all steps for using AGC once
it has been `installed <https://aws.github.io/amazon-genomics-cli/docs/getting-started/installation/>`_.

Tutorial Topics
----------------
The following CWL workflow tutorials will cover:

1. Deploying an AGC project and context
2. Configuring the Dockstore CLI to communicate with AGC infrastructure
3. Launching a workflow


Configuring AGC and the Dockstore CLI
----------------------------------------
1. Create a file named ``agc-project.yaml`` that contains:

    .. code:: text

        name: dockstoreAgcTutorialProject
        schemaVersion: 1
        contexts:
          ctx2:
            engines:
              - type: cwl
                engine: toil

This will create an AGC project named ``dockstoreAgcTutorialProject``, with a single context named ``ctx2``.

.. note::

    For AGC infrastructure to interact with an S3 resource, the desired S3 bucket must be specified in the project's ``agc-project.yaml`` file
    and your AWS account must already have access to the S3 resource. For more information on how to this, please click `here <https://aws.github.io/amazon-genomics-cli/docs/concepts/data/>`_.


2. Activate AGC on your account. If this is your first time running AGC on an account, this may take a few minutes.

    .. code:: text

        agc account activate

3. Deploy an AGC context by running the below command in the same directory as ``agc-project.yaml``. This will take approximately 10 minutes.

    .. code:: text

        agc context deploy ctx2

4. Retrieve the WES endpoint created by the context. This will return a few values, the WES endpoint is the value under *WESENDPOINT*:

    .. code:: text

        agc context describe ctx2

    .. code:: text

        WESENDPOINT     https://example123.execute-api.us-west-2.amazonaws.com/prod/

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


Words Workflow
--------------
The Dockstore entry associated with this workflow can be found here `words <https://dockstore.org/workflows/github.com/dockstore-testing/tooltester-wes-testing/words:stable-version-for-testing-v4?tab=info>`_.



    *main.cwl*

    .. code:: text

        cwlVersion: v1.0
        class: Workflow
        requirements:
          ScatterFeatureRequirement: {}
        inputs:
          words: File
          vowels: string[]
        outputs:
          summaryFile:
            type: File
            outputSource: sumWords/summaryFile

        steps:
          countWordsWithLetter:
            scatter: vowel
            in:
              words: words
              vowel: vowels
            out: [countFile]
            run:
              class: CommandLineTool
              baseCommand: grep
              inputs:
                words: File
                vowel: string
              arguments:
                - $(inputs.vowel)
                - $(inputs.words.path)
                - --count
              outputs:
                countFile:
                  type: stdout
              stdout: count.txt
          sumWords:
            in:
              countFiles: [countWordsWithLetter/countFile]
            out: [summaryFile]
            run:
              class: CommandLineTool
              baseCommand: ["awk", "{ sum += $1 } END { print sum }"]
              inputs:
                countFiles:
                  type: File[]
                  inputBinding:
                    position: 1
              outputs:
                summaryFile:
                  type: stdout
              stdout: summary.txt

1. This workflows takes a file, and an array of strings as an input.  Create a file named ``input.json`` in your working directory with the contents:

    *input.json*

    .. code:: text

            {
              "words": {
                "class": "File",
                "path": "https://raw.githubusercontent.com/dockstore-testing/tooltester-wes-testing/178957c33c37ce5b91e2c973c1f5dd6870c31b6a/words/mieliestronk-words.txt"
              },
              "vowels": ["a","e","i","o","u"]
            }

2. Since this workflow is publicly posted on `Dockstore.org <https://dockstore.org/workflows/github.com/dockstore-testing/tooltester-wes-testing/words:stable-version-for-testing-v4?tab=info>`_, we can quickly launch it by passing the Dockstore CLI the entry and input files.

    .. code:: text

        dockstore workflow wes launch --entry github.com/dockstore-testing/tooltester-wes-testing/words:stable-version-for-testing-v4 --json input.json


3. The above command will return a unique run ID, similar to:

    .. code:: text

        run-00000000000000000000000000000000

    Copy the run ID and run the following to get the workflow run logs:

    .. code:: text

        dockstore workflow wes logs --id run-00000000000000000000000000000000

    The logs returned will look similar to:

    .. code:: text

            {
              "run_id" : "run-00000000000000000000000000000000",
              "request" : {
                "workflow_params" : {
                  "words" : {
                    "class" : "File",
                    "path" : "https://raw.githubusercontent.com/dockstore-testing/tooltester-wes-testing/178957c33c37ce5b91e2c973c1f5dd6870c31b6a/words/mieliestronk-words.txt"
                  },
                  "vowels" : [ "a", "e", "i", "o", "u" ]
                },
                "workflow_type" : "CWL",
                "workflow_type_version" : "v1.0",
                "tags" : {
                  "Client" : "Dockstore"
                },
                "workflow_engine_parameters" : { },
                "workflow_url" : "https://dockstore.org/api/ga4gh/trs/v2/tools/%23workflow%2Fgithub.com%2Fdockstore-testing%2Ftooltester-wes-testing%2Fwords/versions/main/PLAIN_CWL/descriptor/%2Fwords%2Fmain.cwl"
              },
              "state" : "COMPLETE",
              "run_log" : {
                "name" : null,
                "cmd" : [ "<CENSORED>" ],
                "start_time" : "2023-04-20T21:15:35.906100",
                "end_time" : "2023-04-20T21:19:37.501446",
                "stdout" : "../../../../toil/wes/v1/logs/run-00000000000000000000000000000000/stdout",
                "stderr" : "../../../../toil/wes/v1/logs/run-00000000000000000000000000000000/stderr",
                "exit_code" : 0
              },
              "task_logs" : [ ],
              "outputs" : {
                "summaryFile" : {
                  "location" : "s3://<CENSORED FILE LOCATION>",
                  "basename" : "summary.txt",
                  "nameroot" : "summary",
                  "nameext" : ".txt",
                  "class" : "File",
                  "checksum" : "sha1$ce1e58dd77758f13b49d2ef4c33a651e353fe074",
                  "size" : 7
                }
              }
            }


4. The output of this workflow is a text file containing a number. To retrieve the file's contents, you can navigate to the S3 URL via the
AWS console, or copy the file contents using the AWS CLI:

    .. code:: text

        aws s3 cp s3://<CENSORED FILE LOCATION> -

5. When you are finished running workflows on your AGC context, you need to destroy it. Destroy your AGC context by running the below command in the same directory as ``agc-project.yaml``.
This will take approximately 20 minutes.

    .. code:: text

        agc context destroy ctx2

.. discourse::
    :topic_identifier: 6866
