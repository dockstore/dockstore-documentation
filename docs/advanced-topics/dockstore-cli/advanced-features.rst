Advanced CLI Features
=====================

.. contents:: Table of Contents
  :local:

.. _file-provisioning:

File Provisioning
-----------------

As a convenience, the Dockstore CLI can perform file
provisioning for inputs and outputs.

File provisioning for some protocols, like HTTP and FTP, is built-in
while other protocols are handled by plugins as documented
`here <https://github.com/dockstore/dockstore-cli/tree/master/dockstore-file-plugin-parent>`__.

To illustrate, for this
`tool <https://dockstore.org/containers/quay.io/collaboratory/dockstore-tool-bamstats>`__
we provide a couple of parameter files that can be used to parameterize
a run of bamstats.

In the following JSON file, this file indicates for a CWL run that the
input file should be present and readable at
``/tmp/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam``. The
output file will be copied to ``/tmp/bamstats_report.zip`` (which should
be writeable).

::

    {
      "bam_input": {
            "class": "File",
            "path": "/tmp/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam"
        },
        "bamstats_report": {
            "class": "File",
            "path": "/tmp/bamstats_report.zip"
        }
    }

The Dockstore command-line allows you to specify that the input file can
be at an HTTP(S) location, an FTP location, an AWS S3 location, a Google
Storage gs location, a `synapse
id <https://python-docs.synapse.org/tutorials/python_client/#accessing-data>`__, or a `DRS
URI <https://github.com/ga4gh/data-repository-service-schemas/issues/49>`__
in place of that path. For example, the following indicates that the
input file will be downloaded under HTTP.

::

    {
      "bam_input": {
            "class": "File",
            "path": "https://s3.amazonaws.com/oconnor-test-bucket/sample-data/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam"
        },
        "bamstats_report": {
            "class": "File",
            "path": "/tmp/bamstats_report.zip"
        }
    }

Provisioning for output files works in the same way and has been tested
with S3 output locations.

For some file provisioning methods, additional configuration may be
required.

The below summarizes some of the plugins available:

.. |s3_plugin| replace:: `s3-plugin <https://github.com/dockstore/s3-plugin>`__
.. |synapse_plugin| replace:: `synapse-plugin <https://github.com/dockstore/synapse-plugin>`__
.. |dos_plugin| replace:: `data-object-service-plugin <https://github.com/dockstore/data-object-service-plugin>`__
.. |gcs_plugin| replace:: `gcs-plugin <https://github.com/dockstore/gs-plugin>`__

.. |s3_example| replace:: s3://oicr.temp/bamstats\_report.zip
.. |dos_example| replace:: dos://ec2-52-26-45-130.us-west-2.compute.amazonaws.com:8080/911bda59-b6f9-4330-9543-c2bf96df1eca
.. |gs_example| replace:: gs://genomics-public-data/references/GRCh38/chr1.fa.gz

+-------------------------------+---------+---------------------------------+--------------+
| Plugin                        | Prefix  | Example                         | Supported    |
|                               |         |                                 | Operations   |
+===============================+=========+=================================+==============+
| |s3_plugin|                   | s3://   | |s3_example|                    | download,    |
|                               |         |                                 | upload, set  |
|                               |         |                                 | metadata on  |
|                               |         |                                 | upload       |
+-------------------------------+---------+---------------------------------+--------------+
| |synapse_plugin|              | syn://  | syn://syn8299856                | download     |
|                               |         |                                 |              |
|                               |         |                                 |              |
+-------------------------------+---------+---------------------------------+--------------+
| |dos_plugin|                  | dos://  | |dos_example|                   | download     |
|                               |         |                                 |              |
|                               |         |                                 |              |
|                               |         |                                 |              |
+-------------------------------+---------+---------------------------------+--------------+
| |gcs_plugin|                  | gs://   | |gs_example|                    | download,    |
|                               |         |                                 | upload, set  |
|                               |         |                                 | metadata on  |
|                               |         |                                 | upload       |
+-------------------------------+---------+---------------------------------+--------------+

AWS S3
~~~~~~

For AWS S3, create a ``~/.aws/credentials`` file and a ``~/.aws/config``
file as documented at the following
`location <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html>`__.

Get more information on the implementing plugin at
`s3-plugin <https://github.com/dockstore/s3-plugin>`__.

Google Cloud Storage
~~~~~~~~~~~~~~~~~~~~

    Automatically installed in Dockstore 1.6.0+

For Google Cloud Storage, you can download, upload, and set metadata on
uploaded objects with the gs-plugin. The plugin handles urls with the
``gs://`` prefix such as
``gs://genomics-public-data/references/GRCh38/chr1.fa.gz``. Get more
information on the implementing plugin at
`gs-plugin <https://github.com/dockstore/gs-plugin>`__.

Synapse
~~~~~~~

For Synapse, you can add ``synapse-api-key`` and ``synapse-user-name``
to ``~/.dockstore/config`` under the section
``[dockstore-file-synapse-plugin]``.

Get more information on the implementing plugin at
`synapse-plugin <https://github.com/dockstore/synapse-plugin>`__.

Data Object Service (DOS)
~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, no additional configuration is directly supported by the Data
Object Service plugin. However, specifying a DOS URI will download a
file with either built-in support or one of the plugins. If done through
one of the plugins, that plugin may need to be configured, e.g., if a
DOS URI leads to downloading a file from AWS S3, then you may need to
configure your AWS S3 plugin.

Get more information on the implementing plugin at
`data-object-service-plugin <https://github.com/dockstore/data-object-service-plugin>`__.

Input File Cache
----------------

When developing or debugging tools, it can be time and space consuming
to repeatedly download input files for your tools. A feature of the
Dockstore CLI is the ability to cache input files locally so that they
can be quickly re-used for multiple attempts at launching a tool.

This feature relies upon Linux
`hard-linking <https://en.wikipedia.org/wiki/Hard_link>`__. So when
enabling this feature, it is important to ensure that the location of
the cache directory (by default ``~/.dockstore/cache/``) is on the same
filesystem as the working directory where you intend on running your
tools.

There are two configuration file keys that can be used to activate input
file caching and to configure the location of the cache. These are added
(or changed) inside your configuration file at ``~/.dockstore/config``.

::

    use-cache = true
    cache-dir =

The former is false by default and can be set to true in order to
activate the cache. The latter is ``~/.dockstore/cache/`` by default and
can be set to any directory location.

File Provision Retries
----------------------

By default, Dockstore will attempt to download files up to three times.
Control this with the ``file-provision-retries`` parameter inside
``~/.dockstore/config``.

Running Launchers with Extra flags
----------------------------------

When running a tool or workflow, you may want to add additional
parameters or flags to the executor. You can do this by updating your
Dockstore config file  (``~/.dockstore/config``).

As an example, adding the following line to your config file will stop
``cwltool`` from removing the Docker container and temp directory as
mounted on the host, and make it run in debug mode.

::

    cwltool-extra-parameters: --debug, --leave-container, --leave-tmpdir


At times, ``cwltool`` can create a large amount of output in addition to
the workflow’s standard output and error. This `can lead to memory
problems`_ in the Dockstore CLI. To avoid this, you can run in quiet
mode by adding the ``--quiet`` flag.

.. _can lead to memory problems: https://github.com/dockstore/dockstore/issues/1420


You can add additional Java VM options to the command line for the Cromwell
launcher. For example, by adding the following line to your config file you can
provide the location of a Cromwell config file and memory pool requirements to the Java VM.

::

    cromwell-vm-options: -Dconfig.file=/Users/mydir/cromwell.conf, -Xms256m, -Xmx2048m



You can add additional Cromwell options to the command line for the Cromwell
launcher. For example, by adding the following line to your config file you can
provide the ``-t`` and ``--options`` options to the Cromwell command line.

::

    cromwell-extra-parameters: -t WDL, --options workflow_options.json


.. _alternative-cwl-launchers:

Alternative CWL Launchers
-------------------------

By default, the Dockstore CLI launches CWL tools/workflows using
`cwltool <https://github.com/common-workflow-language/cwltool>`__.
However, we have an experimental integration with other launchers such
as: -
`cwl-runner <https://www.commonwl.org/v1.0/CommandLineTool.html#Executing_CWL_documents_as_scripts>`__
- `Cromwell <https://cromwell.readthedocs.io/en/stable/>`__

Keep in mind that there are a few differences in how locked-down the
Docker execution environments are between the launchers. So a workflow
that succeeds in one may not necessarily succeed in another.

You can test all the launchers by cloning the dockstore-tool-md5sum
repository:
``git clone git@github.com:briandoconnor/dockstore-tool-md5sum.git`` and
then test with cwl-runner, Cromwell, and cwltool using
``dockstore tool launch --local-entry Dockstore.cwl --json test.json``
after the required configurations have been made.

Even though it's the default, you can also explicitly use cwltool by
adding the following to your ``~/.dockstore/config``:
``cwlrunner: cwltool``

cwl-runner
~~~~~~~~~~

If your workflow platform provides the cwl-runner alias as the
platform's default CWL implementation, you can activate it by adding the
following to your ``~/.dockstore/config``:

::

    cwlrunner: cwl-runner

.. _cromwell:

Cromwell
~~~~~~~~~~~~~~~

You can launch CWL tools/workflows using Cromwell by adding the
following to your ``~/.dockstore/config``:

::

    cwlrunner: cromwell

Cromwell with CWL handles imports differently than cwltool with CWL.
Cromwell requires imports of a workflow to be given in a zip directory,
where the files are referenced relative to the root of the zip
directory. With cwltool, the files imported are referenced relative to
the file importing them. You can read more about how Cromwell handles
imports `here <https://cromwell.readthedocs.io/en/stable/Imports/>`__.

When launching local CWL workflows with Cromwell, we zip the directory
where the primary descriptor file is located and use this zip file for
imports. This way the imports are resolved relative to the primary
descriptor. **You should store your descriptor files in a clean
directory if you can.**

For remote launches, we download the zip directory as returned by the
Dockstore API. Note that this should work for most cases where the
primary descriptor is in the root directory of its git repository.

WDL Launcher Configuration
--------------------------

By default, WDL tools/workflows will automatically be run by the Dockstore CLI
with the `Cromwell <https://github.com/broadinstitute/cromwell>`__ version listed below.

+-------------+-----------------------+
| CLI version | Cromwell version used |
+=============+=======================+
|     1.8     |          44           |
+-------------+-----------------------+
|     1.9     |          44           |
+-------------+-----------------------+
|     1.10    |          44           |
+-------------+-----------------------+
|     1.11    |          57           |
+-------------+-----------------------+
|     1.12    |          57           |
+-------------+-----------------------+
|     1.13    |          77           |
+-------------+-----------------------+
|     1.14    |          84           |
+-------------+-----------------------+

Additionally, you can override the Cromwell version in your
``~/.dockstore/config`` using for example:

::

    cromwell-version = 84

The Dockstore CLI will attempt to download the version of Cromwell JAR file you specify from the `Cromwell
download area <https://github.com/broadinstitute/cromwell/releases/>`__ to
``~/.dockstore/libraries``.

You can test Cromwell by cloning the dockstore-tool-md5sum repository:
``git clone git@github.com:briandoconnor/dockstore-tool-md5sum.git`` and
then test using
``dockstore tool launch --local-entry Dockstore.wdl --json test.wdl.json``

.. note:: The cromwell-version mentioned in ``~/.dockstore/config`` will
    also be used to specify the version of Cromwell used to launch CWL tools
    and workflows if you set ``cwlrunner: cromwell``.

.. _notifications:

Notifications
-------------

The Dockstore CLI has the ability to provide notifications via an HTTP
post to a user-defined endpoint for the following steps: - The beginning
of input files provisioning - The beginning of tool/workflow execution -
The beginning of output files provisioning - Final launch completion

Additionally, it will also provide notifications when any of these steps
have failed.

Usage
~~~~~

-  Define a webhook URL in the Dockstore config file with the
   "notifications" property like:

   ::

       token: iamafakedockstoretoken
       server-url: https://dockstore.org/api
       notifications: https://hooks.slack.com/services/aaa/bbb/ccc

-  UUID can be generated or user-defined uuid in the dockstore launch
   command like:

   .. code:: bash

       dockstore tool launch --local-entry Dockstore.cwl --json test.json --uuid fakeUUID

-  An HTTP post with a JSON payload will be sent to the url defined
   earlier that looks like:

   .. code:: json

       {
         "text": "someTextBasedOnMilestoneAndStatus",
         "username": "your linux username",
         "platform": "Dockstore CLI 1.4",
         "uuid": "someUserDefinedOrGeneratedUUID"
       }

Notes
~~~~~

-  To disable notifications, simply remove the webhook URL from the
   Dockstore config file
-  If the UUID is generated, the generated UUID will be displayed in
   beginning of the launch stdout

.. raw:: html

   <!--stackedit_data:
   eyJoaXN0b3J5IjpbMjA4MjI5MzQ4NV19
   -->

.. _workflow-execution-service-wes-command-line-interface-cli:

Workflow Execution Service (WES) Command Line Interface (CLI)
-------------------------------------------------------------

The Workflow Execution Service API describes a standard programmatic way
to run and manage workflows. See more information here:
https://github.com/ga4gh/workflow-execution-service-schemas

The Dockstore CLI implements a WES client that allows users to submit a
request to launch a workflow run, get the status of a run, or cancel a
run at a WES endpoint.

The Dockstore CLI will not transmit local files referenced in an input JSON
to the WES endpoint. Therefore, we recommend that an input JSON that has a
file input use a URL (not a local path) that
points to the file that the WES endpoint can resolve. For instance, in the
examples below if the input file test.json references a file then
the URL should be an https, gcs, s3, etc. URL like ``https://raw.githubusercontent.com/my_repository/my_file``.


Usage
~~~~~

-  Get help on WES commands:

   .. code:: bash

       dockstore workflow wes --help

-  Get help on the WES command to launch a workflow:

   .. code:: bash

       dockstore workflow wes launch --help

-  Launch a workflow run (--local-entry is not supported), e.g.:

   .. code:: bash

       dockstore workflow wes launch --entry github.com/briandoconnor/dockstore-workflow-md5sum:1.4.0 --json test.json

-  Launch a workflow run and override the WES URL and credentials
   specified in the config file:

   .. code:: bash

       dockstore workflow wes launch --entry github.com/briandoconnor/dockstore-workflow-md5sum:1.4.0 --json test.json --wes-url https://wes.qr1hi.arvadosapi.com/ga4gh/wes/v1
       --wes-auth 'Bearer <my token>'

-  Get status on a run (a run id is returned in the response from
   launching a WES workflow run):

   .. code:: bash

       dockstore workflow wes status --id <run id> [--verbose]

-  Cancel a run (a run id is returned in the response from launching a
   WES workflow run):

   .. code:: bash

       dockstore workflow wes cancel --id <run id>

WES Endpoint and Authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default Dockstore WES CLI requests will be sent to the WES endpoint
specified in the Dockstore config file and will use authorization
credentials specified in the Dockstore config file.

You can override the WES config file settings on the command line by
using global optional parameters - --wes-url <WES URL> URL where the WES
request should be sent, e.g. ``http://localhost:8080/ga4gh/wes/v1`` -
--wes-auth <auth> Authorization credentials for the WES endpoint, e.g.
'Bearer 12345'

Config file settings
^^^^^^^^^^^^^^^^^^^^

Place WES settings after a separate '[WES]' section of the config file.
At this time only 'url' and 'authorization' settings are supported. For
example:

.. code:: bash

    token: <my token>
    server-url: https://dockstore.org/api
    [WES]
    url: https://wes.qr1hi.arvadosapi.com/ga4gh/wes/v1
    authorization: Bearer <my token>



The table below summarizes some of the WES endpoints available:

+-----------+------------------------------------------------------+-----------+
| Sponsor   | Endpoint URL                                         | Language  |
+===========+======================================================+===========+
| Arvados   | ``https://wes.qr1hi.arvadosapi.com/ga4gh/wes/v1``    | CWL       |
+-----------+------------------------------------------------------+-----------+
| Illumina  | ``https://use1.platform.illumina.com/ga4gh/wes/v1``  | CWL       |
+-----------+------------------------------------------------------+-----------+


.. note::  WES SUPPORT IS IN PREVIEW MODE AT THIS TIME. RESULTS MAY BE UNPREDICTABLE.

.. discourse::
    :topic_identifier: 1274
