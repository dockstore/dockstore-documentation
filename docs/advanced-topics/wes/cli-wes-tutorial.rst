Launching workflows using WES and the Dockstore CLI
===================================================

The Dockstore CLI implements the Global Alliance for Genomics and Health's (`GA4GH <https://www.ga4gh.org/>`_)
Workflow Execution Service (`WES <https://ga4gh.github.io/workflow-execution-service-schemas/docs/>`_) standard.
The WES standard defines a format for sending workflow execution, monitoring and retrieval requests and receiving responses between a client and server.

The Benefits of WES
--------------------
WES supports interoperability and reproducibility when launching bioinformatics workflows against execution engines, and provides a standardized
set of API calls for gathering pertinent information regarding server information, execution run logs, and retrieving execution outputs. This
means that as a workflow developer you can send the same workflow execution request to two different WES servers and they will both interpret and
launch your workflow in a similar manner.

The Dockstore CLI implements the WES standard, and can send your workflows as a WES request to a server given a URL and method of authorization,
allowing quick and easy launches of Dockstore workflows. Furthermore, since the Dockstore CLI supports local workflow launches, it's easy to
develop a workflow locally and then, once you've ironed out all the bugs, send that workflow to your WES server of choice for remote execution.

Once you're ready to launch workflows on a WES server, the command can be as simple as:

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

This endpoint lists previous workflow execution runs. You can specify the latest X entries by passing in a count parameter.
To view the latest 5 entries run on a WES server, you can run:

   .. code:: bash

        dockstore workflow wes logs --count 5

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

This endpoints allows you to retrieve the run status of a launched workflow. After launching a WES workflow, a run ID is returned that can
be used to query information regarding the run.
To get the run status of a launched workflow, you can run:

   .. code:: bash

        dockstore workflow wes status --id example-runid-12345-67890

GetRunLog
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `GetRunLog <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/GetRunLog>`_

This endpoints allows you to retrieve the run logs of a launched workflow. After launching a WES workflow, a run ID is returned that can
be used to query information regarding the run.
To get the run log of a launched workflow, you can run:

   .. code:: bash

        dockstore workflow wes logs --id example-runid-12345-67890

CancelRun
^^^^^^^^^^^^^^^^^^^^^^^^
The official documentation for this endpoint can be found here: `CancelRun <https://ga4gh.github.io/workflow-execution-service-schemas/docs/#operation/CancelRun>`_

This endpoints allows you to cancel the execution of a launched workflow. After launching a WES workflow, a run ID is returned that can
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

For example, to specify an AWS API Gateway endpoint as the WES URL, and an AWS named profile as the authorization, the WES config section
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
