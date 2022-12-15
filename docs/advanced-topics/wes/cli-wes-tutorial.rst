Launching workflows using WES and the Dockstore CLI
===================================================

The Dockstore CLI supports the Global Alliance for Genomics and Health's (`GA4GH <https://www.ga4gh.org/>`_)
Workflow Execution Service (`WES <https://ga4gh.github.io/workflow-execution-service-schemas/docs/>`_) standard.
The WES standard defines a format for sending workflow execution, monitoring, and retrieval requests to a server.

The Benefits of WES
--------------------
WES supports interoperability and reproducibility when launching bioinformatics workflows against execution engines, and provides a standardized
set of API calls for gathering pertinent information regarding the target server, execution run logs, and retrieving execution outputs. This
means that you can send the same workflow execution request to two different WES servers and they will both interpret and
launch your workflow in a similar manner.

The Dockstore CLI supports the WES standard. This means that you can send your workflows as a WES request to a desired server, given a URL and method of authorization,
allowing quick and easy launches of Dockstore workflows. Furthermore, since the Dockstore CLI supports local workflow launches, it's easy to
develop a workflow locally and then, once you've ironed out all the bugs, send that workflow to your WES server of choice for remote execution.

To launch a workflow on a WES server, the command can be as simple as:

   .. code:: bash

        dockstore workflow wes launch --entry github.com/dockstore-testing/dockstore-whalesay2:master

WES Basics
--------------
The WES Schema defines 6 API calls, each of which is available via the Dockstore CLI.

GetServiceInfo
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `GetServiceInfo <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/GetServiceInfo>`_

This endpoint describes information regarding the WES server that you are interacting with. This includes information such as which languages
and language versions are supported (WDL, CWL, NFL, etc...), which version of WES the server is running, and the configuration settings of the server itself.
To view the server info of a WES server, you can run:

   .. code:: bash

        dockstore workflow wes service-info

ListRuns
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `ListRuns <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/ListRuns>`_

This endpoint lists past and current workflow execution runs. You can specify the latest X entries by passing in a count parameter.
To view the latest 5 entries on a WES server, you can run:

   .. code:: bash

        dockstore workflow wes list --count 5

RunWorkflow
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `RunWorkflow <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/RunWorkflow>`_

This endpoint specifies how to send a workflow execution request to a WES server. This includes passing in a primary workflow descriptor file,
the input JSON file, and any additional attachment files needed for your workflow.
To launch a Dockstore workflow that takes an input JSON, you can run:

   .. code:: bash

        dockstore workflow wes launch --entry example/dockstore-entry/whalesay:master --json inputs.json

GetRunStatus
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `GetRunStatus <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/GetRunStatus>`_

This endpoint allows you to retrieve the run status of a launched workflow. After launching a WES workflow, a run ID is returned that can
be used to query information regarding the run.
To get the run status of a launched workflow, you can run:

   .. code:: bash

        dockstore workflow wes status --id example-runid-12345-67890

GetRunLog
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `GetRunLog <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/GetRunLog>`_

This endpoint allows you to retrieve the run logs of a launched workflow. After launching a WES workflow, a run ID is returned that can
be used to query information regarding the run.
To get the run log of a launched workflow, you can run:

   .. code:: bash

        dockstore workflow wes logs --id example-runid-12345-67890

CancelRun
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `CancelRun <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/CancelRun>`_

This endpoint allows you to cancel the execution of a launched workflow. After launching a WES workflow, a run ID is returned that can
be used to cancel the workflow run.
To cancel a launched workflow, you can run:

   .. code:: bash

        dockstore workflow wes cancel --id example-runid-12345-67890


Configuring the Dockstore CLI
------------------------------
To configure the Dockstore CLI to make WES requests, the Dockstore CLI configuration file must be modified with a WES section. The configuration file is
located by default in your home directory, at ``~/.dockstore/config``, although you can pass any config file to the Dockstore CLI using
the ``--config`` parameter. The WES section of the config file specifies three values, the URL of the WES server, an authorization type, and
an authorization value:

*~/.dockstore/config*

.. code:: text

    [WES]
    url: WES_URL
    authorization: AUTHORIZATION_VALUE
    type: AUTHORIZATION_TYPE

The Dockstore CLI supports two authorization types, ``aws`` and ``bearer``:

1. The ``aws`` authorization type indicates that the provided authorization value will be the string name of an AWS named profile, and that the Dockstore CLI must use the `AWS SigV4 <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ signing process for HTTP/HTTPS requests. AWS SigV4 signing is required when making AWS API requests, such as when contacting a WES server via an AWS API Gateway endpoint.
2. The ``bearer`` authorization type indicates that the provided authorization value will be an authenticating string/token that the Dockstore CLI will attach under the *AUTHORIZATION* header for HTTP/HTTPS requests.

For example, to specify an AWS API Gateway endpoint as the WES URL, and an AWS named profile as the authorization value, the WES config section
would look similar to:

*~/.dockstore/config*

.. code:: text

    [WES]
    url: https://example.execute-api.us-west-2.amazonaws.com/prod/ga4gh/wes/v1
    authorization: aws-wes-profile
    type: aws

By default, the Dockstore CLI reads the configuration file located at ``~/.dockstore/config``. A separate config file can be passed to the CLI
by running the following:

   .. code:: bash

        dockstore --config /path/to/custom_config workflow wes ...

Having multiple configuration files may be useful if you have access to various different WES servers, and want to easily switch between
them when making WES requests.

.. toctree::
   :caption: WES Tutorials
   :maxdepth: 1

   wes-agc-tutorial
