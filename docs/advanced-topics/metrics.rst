Workflow Metrics
================

What are workflow metrics?
------------------------------------
Workflow metrics are metrics of workflow executions on a platform. Users are able to execute workflows on various platforms using Dockstore's Launch With feature, shown on the right side in the screenshot below.

.. figure:: /assets/images/docs/submit-metrics/workflow-launch-with.png
    :alt: Launch With Partners

Platforms are able to submit metrics of workflows executed on their platform to Dockstore and we aggregate the metrics and display them in the UI to the users in the :ref:`Metrics tab <How to view metrics>`.

Why would I want to submit workflow metrics?
--------------------------------------------
As a platform owner, workflow metrics indicate to others that your platform is compatible with many workflows on Dockstore. Workflow metrics provide valuable information to users to help them determine if they can use the workflow on your platform.


How do I submit workflow metrics?
---------------------------------

.. note:: Submitting workflow metrics is only available for admins, curators, and platform partners. If you're a platform owner and you don't have a platform partner user, please contact us via our `GitHub <https://github.com/dockstore/dockstore/issues>`_ issues or `Gitter <https://gitter.im/ga4gh/dockstore>`_ and we will help you get set up.

Go to https://dockstore.org/api/static/swagger-ui/index.html#/extendedGA4GH/executionMetricsPost. This is the endpoint used to submit metrics to Dockstore. Click the "Try it out” button.

First, fill out the query parameters. This is where you'll input information about which workflow was executed and what platform it was executed on.

For the ``id`` parameter, provide the TRS ID of the workflow that you want to submit metrics for. For example, the `dockstore-tool-bamstats <https://dockstore.org/workflows/github.com/dockstore/dockstore-tool-bamstats/wdl:1.25-9?tab=info>`__ workflow has the TRS ID ``#workflow/github.com/dockstore/dockstore-tool-bamstats/wdl`` as shown in the “Info” tab with the label “TRS".

For the ``version_id`` parameter, provide the name of the workflow version that was executed. It can be any version listed in the "Versions" tab of the workflow. For example, `dockstore-tool-bamstats <https://dockstore.org/workflows/github.com/dockstore/dockstore-tool-bamstats/wdl:1.25-9?tab=versions>`__ has the following versions currently: 1.25-9 and develop. It is recommended to submit execution metrics for versions that are unlikely to change, like tags.

Select the ``platform`` that the workflow was executed on from the available values.

For the ``description``, you may provide an optional description about the metrics you're submitting.

.. figure:: /assets/images/docs/submit-metrics/query-parameters.png
    :alt: Query parameters for submitting metrics

In the request body, provide the workflow execution metrics that you want to submit. Click on Schema to view the schema of the request body.

.. figure:: /assets/images/docs/submit-metrics/request-body-schema.png
    :alt: Request body schema for submitting metrics

You can provide a individual executions through ``runExecutions`` and ``validationExecutions``.

A run execution is an execution that runs the workflow. If you want to provide metrics for the run execution that are not defined in the schema, use the ``additionalProperties`` key to provide your metric.

.. figure:: /assets/images/docs/submit-metrics/run-executions-schema.png
    :alt: Schema for run executions

A validation execution is an execution of a validator tool, like miniwdl, on the workflow. If you want to provide metrics for the validation execution that are not defined in the schema, use the ``additionalProperties`` key to provide your metric.

.. figure:: /assets/images/docs/submit-metrics/validation-executions-schema.png
    :alt: Schema for validation executions

Instead of individual executions, you may also provide aggregated metrics through ``aggregatedExecutions``. If you want to provide aggregated metrics that are not defined in the schema, use the ``additionalAggregatedMetrics`` key to provide your metric.

.. figure:: /assets/images/docs/submit-metrics/aggregated-metrics-schema.png
    :alt: Schema for aggregated metrics
    
Lastly, provide your Dockstore token using the lock icon at the top right of the endpoint.

Below is an example of what the request for submitting metrics for a workflow that was executed on Terra looks like. The request body submits one run execution that was successful and took 30 seconds to execute, and one validation execution of miniwdl version 1.9.1 which validated the workflow successfully.


.. figure:: /assets/images/docs/submit-metrics/individual-executions-example.png
   :alt: Example request for submitting individual run executions and validation executions


The curl command results in something like:

.. code:: bash

   curl -X 'POST' \
      'https://dockstore.org/api/api/ga4gh/v2/extended/%23workflow%2Fgithub.com%2Fdockstore%2Fdockstore-tool-bamstats%2Fwdl/versions/1.25-9/executions?platform=TERRA' \
      -H 'accept: */*' \
      -H 'Authorization: Bearer iamafakebearertoken' \
      -H 'Content-Type: application/json' \
      -d '{
      "runExecutions": [
         {
            "executionStatus": "SUCCESSFUL",
            "executionTime": "PT30S"
         }
      ],
      "validationExecutions": [
         {
            "validatorTool": "miniwdl",
            "validatorToolVersion": "1.9.1",
            "isValid": true,
            "dateExecuted": "2023-03-31T15:06:49.888745366Z"
         }
      ]
   }'

If it was submitted successfully, you should receive a ``204`` response code. 

.. _How to view metrics:

How do I view workflow metrics?
-------------------------------

To view workflow metrics for a workflow on Dockstore, you will need to use the ``metrics`` feature flag.

To use the ``metrics`` feature flag, append ``metrics`` to the Dockstore URL as a query parameter. You only need to do this once, unless you refresh/close your browser.

For example, if you're on the https://dockstore.org page, append ``metrics`` such that it looks like this: https://dockstore.org?metrics.

If you're on a page that already contains query parameters, indicated by the presence of a question mark, append ``metrics`` to the URL using an ampersand. For example, if you're on the https://dockstore.org/workflows/github.com/gatk-workflows/seq-format-conversion/BAM-to-Unmapped-BAM:3.0.0?tab=info page, append ``metrics`` such that it looks like https://dockstore.org/workflows/github.com/gatk-workflows/seq-format-conversion/BAM-to-Unmapped-BAM:3.0.0?tab=info&metrics.

After applying the ``metrics`` feature flag, a Metrics tab will appear when viewing a workflow on Dockstore. Click on the Metrics tab and you will see workflow metrics if they are available.

.. figure:: /assets/images/docs/submit-metrics/metrics-tab.png
    :alt: Metrics tab
