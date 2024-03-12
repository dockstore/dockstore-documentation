Workflow Metrics
================

.. contents::
   :local:
   :depth: 1

What Are Workflow Metrics?
------------------------------------
Workflow metrics are metrics of workflow executions on a platform. Metrics include things like the resources used during the execution, and how often workflow executions succeeded or failed.

Users are able to execute workflows on various platforms using Dockstore's Launch With feature, shown on the right side in the screenshot below.

.. figure:: /assets/images/docs/metrics/workflow-launch-with.png
    :alt: Launch With Partners

Platforms are able to submit metrics of workflows executed on their platform to Dockstore and we aggregate the metrics and display them in the UI to the users in the :ref:`Metrics tab <How to view metrics>`.

Why Would I, a Platform Owner, Want to Submit Workflow Metrics?
---------------------------------------------------------------

As a platform owner, workflow metrics indicate to others that your platform is compatible with many workflows on Dockstore. Workflow metrics provide valuable information to users, including information about the resources and time needed to run the workflow. It helps the user determine if the workflow is high quality and likely to function correctly.

Platform owners are able to submit metrics for workflow executions, retrieve submitted executions, and update submitted executions. 

.. _Getting started with submitting metrics:

Getting Started With Submitting Metrics to Dockstore
----------------------------------------------------

The following sections go over how a platform can submit workflow metrics to Dockstore. 

.. contents::
   :local:
   :depth: 1

Dockstore will occasionally aggregate the workflow metrics you submit and display them in the :ref:`Dockstore UI<How to view metrics>`.

Record workflow execution metrics on your platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step is to collect metrics for executions of public Dockstore workflows that occur on your platform. The mandatory metrics that Dockstore requires are the date of execution and the execution status. 
If they are available, you may also collect additional metrics such as how long it took the workflow to run, CPU requirements, memory requirements, etc.

Format the workflow metrics for Dockstore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The metrics that you collect may not be in the format that the Dockstore API expects. You have to format them so they follow Dockstore's schema, which you can view in the :ref:`Submit Workflow Metrics to Dockstore<Submit executions>` section.

For example, execution dates are expected to be in ISO 8601 UTC date format and there are a defined set of execution statuses that can be submitted.

.. note::
   If you are unable to format the workflow metrics to match Dockstore's schema or you would like to try submitting metrics without continuing with the following steps, 
   contact us via our `GitHub <https://github.com/dockstore/dockstore/issues>`_ issues or open a helpdesk ticket on `Discourse <https://discuss.dockstore.org/>`_ and we can help get your metrics into Dockstore.
   
   This may involve you providing us with a file of metrics, such as a CSV file, and Dockstore will process the file and ingest the metrics into our system.

Register a platform partner user on Dockstore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only Dockstore admins, curators, and platform partners can :ref:`submit metrics<Submit executions>` for workflow executions, and :ref:`retrieve and update submitted executions<Viewing And Updating Submitted Workflow Metrics>`.
If you're a platform owner and you don't have a platform partner user on Dockstore, please:

1. :doc:`Create a Dockstore account </getting-started/register-on-dockstore>`, if you haven't already. You will use the credentials of this user to submit Dockstore metrics.
2. Contact us via our `GitHub <https://github.com/dockstore/dockstore/issues>`_ issues or open a helpdesk ticket on `Discourse <https://discuss.dockstore.org/>`_ and we will give your Dockstore user a platform partner role.

.. _Submit executions:

Submit workflow metrics to Dockstore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have the metrics formatted and you registered a platform partner Dockstore user, you may use the Dockstore API to submit workflow metrics. You will need the Dockstore token of a user with a platform partner role.

Go to https://dockstore.org/api/static/swagger-ui/index.html#/extendedGA4GH/executionMetricsPost and provide your Dockstore token using the lock icon at the top right of the endpoint. This is the endpoint used to submit metrics to Dockstore. Click the "Try it out” button.

First, fill out the parameters. This is where you input information about which workflow was executed and what platform it was executed on.

For the ``id`` parameter, provide the TRS ID of the workflow that you want to submit metrics for. For example, the `dockstore-tool-bamstats <https://dockstore.org/workflows/github.com/dockstore/dockstore-tool-bamstats/wdl:1.25-9?tab=info>`__ workflow has the TRS ID ``#workflow/github.com/dockstore/dockstore-tool-bamstats/wdl`` as shown in the “Info” tab with the label “TRS".

For the ``version_id`` parameter, provide the name of the workflow version that was executed. It can be any version listed in the "Versions" tab of the workflow. For example, `dockstore-tool-bamstats <https://dockstore.org/workflows/github.com/dockstore/dockstore-tool-bamstats/wdl:1.25-9?tab=versions>`__ has the following versions currently: ``1.25-9`` and ``develop``. It is recommended to submit execution metrics for versions that are unlikely to change, like tags.

Select the ``platform`` that the workflow was executed on from the available values.

For the ``description``, you may provide an optional description about the metrics you're submitting.

.. figure:: /assets/images/docs/metrics/submit-metrics-parameters.png
    :alt: Query parameters for submitting metrics

.. _Submit metrics request body schema:

In the request body, provide the workflow execution metrics that you want to submit. Click on Schema to view the schema of the request body.

.. figure:: /assets/images/docs/metrics/executions-request-body-schema.png
    :alt: Request body schema for submitting metrics

You can provide a individual executions through ``runExecutions``, ``taskExecutions``, and ``validationExecutions``.

.. important::
   Each execution must have a unique ``executionId`` for the workflow, workflow version, and platform that it belongs to. It is your responsibility to ensure the uniqueness of the execution IDs. 
   The execution ID is also used to :ref:`get a submitted execution<View submitted execution>` and :ref:`update a submitted execution<Update submitted execution>`.

A ``RunExecution`` is a workflow execution. The required fields are:

- ``executionId``
- ``dateExecuted``
- ``executionStatus``

If you want to provide additional metrics that are not defined in the schema, use the ``additionalProperties`` key to provide your metric.

.. figure:: /assets/images/docs/metrics/run-executions-schema.png
    :alt: Schema for run executions

A ``TaskExecution`` contains a list of task executions that were executed during a workflow execution. The required fields are:

- ``executionId``
- ``dateExecuted``
- A list of ``taskExecutions``. A task execution follows the ``RunExecution`` schema.

.. figure:: /assets/images/docs/metrics/task-executions-schema.png
    :alt: Schema for task executions

A ``ValidationExecution`` is an execution of a validator tool, like miniwdl, on the workflow. The required fields are: 

- ``executionId``
- ``dateExecuted``
- ``validatorTool``
- ``validatorToolVersion``
- ``isValid``

If you want to provide additional metrics that are not defined in the schema, use the ``additionalProperties`` key to provide your metric.

.. figure:: /assets/images/docs/metrics/validation-executions-schema.png
    :alt: Schema for validation executions
    
.. _Submitting metrics example:

Submitting metrics example
**************************

The following is an example of how to submit metrics for version 1.25-9 of the `dockstore-tool-bamstats <https://dockstore.org/workflows/github.com/dockstore/dockstore-tool-bamstats/wdl:1.25-9?tab=info>`__ workflow that was executed on Terra. 

.. _Submitting metrics example parameters:

The parameters are:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Parameter
     - Value
   * - id
     - #workflow/github.com/dockstore/dockstore-tool-bamstats/wdl
   * - version_id
     - 1.25-9
   * - platform
     - TERRA

The request body contains three executions in total:

- One workflow execution that was successful and took 30 seconds to execute
- One task execution list consisting of one task execution that failed and took 1 second to execute  

  - Note: there is only one task execution because this workflow only contains one task
- One validation execution of miniwdl version 1.9.1 which validated the workflow successfully

.. figure:: /assets/images/docs/metrics/submit-executions-example.png
   :alt: Example request for submitting individual workflow executions, task executions and validation executions

The curl command looks something like:

.. code:: bash

   curl -X 'POST' \
      'https://dockstore.org/api/api/ga4gh/v2/extended/%23workflow%2Fgithub.com%2Fdockstore%2Fdockstore-tool-bamstats%2Fwdl/versions/1.25-9/executions?platform=TERRA' \
      -H 'accept: */*' \
      -H 'Authorization: Bearer fakedockstorebearertoken' \
      -H 'Content-Type: application/json' \
      -d '{
      "runExecutions": [
         {
            "executionId": "2c8c7c45-d4e6-4a0c-891d-a28e7c995c70",
            "dateExecuted": "2023-03-31T15:06:49.888745366Z",
            "executionStatus": "SUCCESSFUL",
            "executionTime": "PT30S"
         }
      ],
      "taskExecutions": [
         {
            "executionId": "127540b0-530f-44c5-9e76-6653755f3fd6",
            "dateExecuted": "2023-03-01T15:06:49.888745366Z",
            "taskExecutions": [
            {
               "executionId": "54e85b77-b2d9-4176-8cea-b6ce9cc25cc8",
               "dateExecuted": "2023-03-01T15:06:49.888745366Z",
               "executionStatus": "FAILED_RUNTIME_INVALID",
               "executionTime": "PT1S"
            }
            ]
         }
      ],
      "validationExecutions": [
         {
            "executionId": "009512c1-92a7-4880-9243-2a1bfe6b78cd",
            "dateExecuted": "2023-03-31T15:06:49.888745366Z",
            "validatorTool": "miniwdl",
            "validatorToolVersion": "1.9.1",
            "isValid": true
         }
      ]
   }'

If it was submitted successfully, you should receive a ``204`` response code.

.. _How to view metrics:

Viewing Aggregated Workflow Metrics in Dockstore
------------------------------------------------

Dockstore aggregates the workflow execution metrics that platforms submit into aggregated metrics for users to view.

To search for workflows with metrics, navigate to the `search <https://dockstore.org/search>`_ page and select a platform for the Execution Metrics and/or Validation Metrics facets.

.. figure:: /assets/images/docs/metrics/metrics-search-facets.png
    :alt: Metrics search facets

Select a workflow and click on the Versions tab. Versions that have metrics have a check mark in the Metrics column.

.. figure:: /assets/images/docs/metrics/versions-metrics-column.png
    :alt: Metrics column in Versions table

Select a version with metrics then click on the Metrics tab to view the metrics available.

.. figure:: /assets/images/docs/metrics/metrics-tab.png
    :alt: Metrics tab

.. _Viewing And Updating Submitted Workflow Metrics:

Viewing And Updating Submitted Workflow Metrics
-----------------------------------------------

As a platform owner who previously :ref:`submitted execution metrics to Dockstore<Getting started with submitting metrics>`, you may want to view or update submitted executions.

.. _View submitted execution:

Viewing a submitted execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view an execution that you previously submitted, you can retrieve it by its execution ID.

Go to https://dockstore.org/api/static/swagger-ui/index.html#/extendedGA4GH/executionGet and provide your Dockstore token using the lock icon at the top right of the endpoint.

Fill out the parameters. This is where you input information about which workflow, version, and platform the execution belongs to. It should be the same values that you used when you submitted the execution to Dockstore.

In addition, specify the execution ID of the execution you want to view. Recall that the execution ID is a value that you assigned the execution when you submitted the execution.

.. figure:: /assets/images/docs/metrics/get-execution-parameters.png
    :alt: Parameters for getting an execution

Getting an execution example
****************************

We'll retrieve an execution that was submitted in :ref:`this example<Submitting metrics example>`.

Provide the same ``id``, ``version_id`` and ``platform`` :ref:`parameter values<Submitting metrics example parameters>`. 

Next, provide the execution ID of the workflow execution that was submitted, which was ``2c8c7c45-d4e6-4a0c-891d-a28e7c995c70``.

.. figure:: /assets/images/docs/metrics/get-execution-example.png
    :alt: Get execution example

The curl command looks something like:

.. code:: bash

   curl -X 'GET' \
      'https://dockstore.org/api/api/ga4gh/v2/extended/%23workflow%2Fgithub.com%2Fdockstore%2Fdockstore-tool-bamstats%2Fwdl/versions/1.25-9/execution?platform=TERRA&executionId=2c8c7c45-d4e6-4a0c-891d-a28e7c995c70' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer fakedockstorebearertoken'

If the request was successful, you should receive a ``200`` status code and the execution that you requested, like below:

.. code:: bash

   {
      "aggregatedExecutions": [],
      "runExecutions": [
         {
            "additionalProperties": null,
            "cost": null,
            "cpuRequirements": null,
            "dateExecuted": "2023-03-31T15:06:49.888745366Z",
            "executionId": "2c8c7c45-d4e6-4a0c-891d-a28e7c995c70",
            "executionStatus": "SUCCESSFUL",
            "executionTime": "PT30S",
            "memoryRequirementsGB": null,
            "region": null
         }
      ],
      "taskExecutions": [],
      "validationExecutions": []
   }

.. _Update submitted execution:

Updating workflow metrics
^^^^^^^^^^^^^^^^^^^^^^^^^

You may want to update metrics that you have previously submitted because you received new metrics for the execution at a later time.

Go to https://dockstore.org/api/static/swagger-ui/index.html#/extendedGA4GH/ExecutionMetricsUpdate and provide your Dockstore token using the lock icon at the top right of the endpoint. This is the endpoint used to update metrics that were submitted to Dockstore. Click the "Try it out” button.

First, fill out the parameters. This is where you input information about which workflow and version was executed and what platform it was executed on. 

For the ``id``, ``version_id``, and ``platform`` parameters, provide the values that you previously used when submitting the metrics you want to update to Dockstore. This ensures that the correct metrics are updated. For example, to update the metrics that were submitted in the :ref:`Submitting metrics example<Submitting metrics example>`, provide the same ``id``, ``version_id`` and ``platform``.

For the ``description``, you may provide an optional description about the metrics you're updating.

.. figure:: /assets/images/docs/metrics/update-metrics-parameters.png
    :alt: Query parameters for submitting metrics

In the request body, provide the updated workflow execution metrics that you want to update in Dockstore. Click on Schema to view the schema of the request body. It is the same schema used for :ref:`submitting metrics<Submit metrics request body schema>`.

.. important::
   Ensure that the execution you are updating have the same execution ID as the execution you previously submitted.

You must provide the full execution object when updating the execution. See :ref:`how to retrieve a submitted execution<View submitted execution>` if you do not have the full execution object.

Only metrics that are optional during submission can be updated. For example, for a workflow ``RunExecution``, you may update ``executionTime``, but you may not update ``executionStatus`` because it is a required field, indicated by the red asterisk.

.. figure:: /assets/images/docs/metrics/run-executions-schema.png
    :alt: Schema for run executions

Click Execute. You should receive a ``207`` reponse code with a response body containing individual response codes for each execution you wanted to update.

Updating an execution example
*****************************

We'll update an execution that was submitted in :ref:`this example<Submitting metrics example>`.

Provide the same ``id``, ``version_id`` and ``platform`` :ref:`parameter values<Submitting metrics example parameters>`.

Recall that this is the workflow execution that was submitted:

.. code:: bash

   "runExecutions": [
      {
         "executionId": "2c8c7c45-d4e6-4a0c-891d-a28e7c995c70",
         "dateExecuted": "2023-03-31T15:06:49.888745366Z",
         "executionStatus": "SUCCESSFUL",
         "executionTime": "PT30S"
      }
   ]

Add a cost metric to the workflow execution. This is the updated workflow execution that we will use. 

.. code:: bash

   "runExecutions": [
      {
         "executionId": "2c8c7c45-d4e6-4a0c-891d-a28e7c995c70",
         "dateExecuted": "2023-03-31T15:06:49.888745366Z",
         "executionStatus": "SUCCESSFUL",
         "executionTime": "PT30S",
         "cost": {
            "value": 5.99
         }
      }
   ]

.. figure:: /assets/images/docs/metrics/update-execution-example.png
    :alt: Update execution example

The curl looks something like the following:

.. code:: bash

   curl -X 'PUT' \
      'https://dockstore.org/api/api/ga4gh/v2/extended/%23workflow%2Fgithub.com%2Fdockstore%2Fdockstore-tool-bamstats%2Fwdl/versions/1.25-9/executions?platform=TERRA' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer fakedockstorebearertoken' \
      -H 'Content-Type: application/json' \
      -d '{
      "runExecutions": [
         {
            "executionId": "2c8c7c45-d4e6-4a0c-891d-a28e7c995c70",
            "dateExecuted": "2023-03-31T15:06:49.888745366Z",
            "executionStatus": "SUCCESSFUL",
            "executionTime": "PT30S",
            "cost": {
               "value": 5.99
            }
         }
      ]
   }'

You should receive a ``207`` status code and a response body like below:

.. code:: bash

   {
      "executionResponses": [
         {
            "error": null,
            "executionId": "2c8c7c45-d4e6-4a0c-891d-a28e7c995c70",
            "status": 200
         }
      ]
   }

The response body indicates that the update for execution with execution ID ``2c8c7c45-d4e6-4a0c-891d-a28e7c995c70`` was successful.

You can verify that the field was updated by :ref:`viewing the execution<View submitted execution>`.

.. discourse::
    :topic_identifier: 7983
