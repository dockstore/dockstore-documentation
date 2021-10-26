Verification
============

What is a verified tool/workflow?
---------------------------------
A verified tool/workflow indicates that it was successfully run and verified by either:

-  the :ref:`Dockstore ToolTester`
-  our team
-  an outside party

Historically, the majority of tool validation has been done by the docktesters
team currently headed by Miguel Vazquez and formerly headed by Francis
Ouellette.

We also strive to use this to highlight tools that share a common set of
recommended characteristics:

-  tools should include a description and an author
-  tools should include a README.md or similar in their source repo
   describing any other relevant information about the tool
-  tools should include at least one test parameter file indicating how
   to run the tool on some sample data
-  the Dockerfile should be helpful in reconstructing how a tool was
   built from source
-  tools and/or their reference data should be publically available


Why would I want to verify?
-------------------------------------------
There are several reasons why you would want a tool/workflow to be verified.
If you're a platform owner, verifying would indicate to others that your platform is compatible with many tools/workflows on Dockstore so others will be more likely to use your platform.
If you're tool/workflow developer, verifying would assure others that your tool/workflow is of high quality and is very likely to work for others.


How do I verify?
---------------------------------------
If you are an admin/curator, follow the :ref:`Verification Process` section in this document.
If you are not an admin/curator, please send us a heads-up via our `GitHub <https://github.com/dockstore/dockstore/issues>`_ issues or `Gitter <https://gitter.im/ga4gh/dockstore>`_!


How do I tell if a tool/workflow is verified?
---------------------------------------------

There are 3 new indicators on Dockstore.org that indicates whether or
not the tool/workflow is verified.

First, go to the page of the tool/workflow such as
https://dockstore.org/containers/quay.io/briandoconnor/dockstore-tool-md5sum:1.0.4?tab=info.
Since this tool/workflow is verified, 3 indicators can be
seen:

.. figure:: /assets/images/docs/verification/tool.png
   :alt: Tool Page

   Tool Page

1. At the top left, the checkmark indicates that at least one of the
   tool/workflow’s version has been verified. As a whole, this
   tool/workflow is considered verified.

2. At the top right, the recent versions of the tool/workflow are
   listed. There is a checkmark if a specific version of the
   tool/workflow is verified.

3. The bottom right shows whether the currently selected/viewed version
   is verified. The selected version is indicated in the URL as well as
   the title (e.g. quay.io/briandoconnor/dockstore-tool-md5sum:1.0.4).
   In this example, the version 1.0.4 is selected/viewed. This bottom
   right verification box contains more details such as the platform and
   verifier. This example shows that “Dockstore CLI” is the platform and
   “Phase 1 GA4GH Tool Execution Challenge” is the verifier.

Additional information for all verified versions can be viewed at a glance
in the versions tab:

.. figure:: /assets/images/docs/verification/versions-tab.png
   :alt: Versions Tab

   Versions Tab

Once again, the checkmarks indicate the version is verified. Platforms
which the version was verified on are displayed to the right of it. In
this case, it’s “Dockstore CLI”.

.. _Verification Process:

Verification Process
--------------------

.. note:: Verifying is only available for admins and curators. Please contact one if you want your tool/workflow to be verified.

1.  Go to
    https://dockstore.org/api/static/swagger-ui/index.html#/extendedGA4GH/verifyTestParameterFilePost
2.  Click “Try it out”
3.  Provide a “type”. See the
    description for allowable values.
4.  Provide the TRS ID for the tool/workflow being verified.
    For example, the `dockstore-tool-md5sum`_ tool has the TRS ID:
    “quay.io/briandoconnor/dockstore-tool-md5sum” as shown in the “Info”
    tab with the label: “TRS CWL” or “TRS WDL”
5.  Provide the version_id of the tool/workflow to verify. It can be any
    version listed in the Version tab of the tool/workflow.
    `dockstore-tool-md5sum <https://dockstore.org/containers/quay.io/briandoconnor/dockstore-tool-md5sum:master?tab=versions>`__
    has the following versions currently: 1.0.4, master, develop, 1.0.3,
    latest, 1.0.2, 1.0.1, and 1.0.0. It is recommended to only verify versions
    that are unlikely to change (tags).
6.  Provide the “relative_path” of the test parameter file being
    verified. The path of the test parameter file is relative to the
    primary descriptor. This path can be found using the `files
    endpoint`_ or by viewing the files tab of a tool/workflow such as:
    https://dockstore.org/containers/quay.io/briandoconnor/dockstore-tool-md5sum:1.0.4?tab=files
    and then further selecting the Test Parameter Files tab and view the
    right-most “File” dropdown. This relative path must be a test
    parameter file, providing a descriptor will not work.
7.  Provide the “platform”. Some examples are: HCA, Cromwell, Arvados,
    etc.
8.  Select the “verified” status either as “true” or “false”. Use “true”
    to verify, “false” to “unverify”.
9.  Provide “metadata”, this is typically the verifier’s identity which
    can be something like “GA4GH/DREAM Challenge”
10. Lastly, provide your Dockstore token using the lock icon at the top
    right of the endpoint

Below is a screenshot of someone verifying the “test.json” test
parameter file of the “master” version of the “dockstore-tool-md5sum”
tool.

.. figure:: /assets/images/docs/verification/swagger.png
   :alt: Swagger-UI

   Swagger-UI

The curl command results in something like:

::

   curl -X POST "https://dockstore.org/api/api/ga4gh/v2/extended/quay.io%2Fbriandoconnor%2Fdockstore-tool-md5sum/versions/master/CWL/tests/test.json?platform=Dockstore%20CLI&verified=true&metadata=Phase%201%20GA4GH%20Tool%20Execution%20Challenge" -H  "accept: application/json" -H  "Authorization: Bearer iamafakebearertoken"

A successful response will result in something like:

::

   {
     "Dockstore CLI": {
       "metadata": "Phase 1 GA4GH Tool Execution Challenge",
       "verified": true
     }
   }


Additional Verification Information
-----------------------------------

To see more verification information about a specific version, first 
select the version.

Then click "More Info" in the "Verification and Logs" panel in the 
bottom right.

A popup will appear:

.. figure:: /assets/images/docs/verification/verification-information.png
   :alt: Verification Information

   Verification Information

It lists the platform it was verified on, the platform version, test parameter file that was used, and metadata (verifier).
Below it, there may be an additional Logs section which contains information from Dockstore ToolTester.


.. _Dockstore ToolTester:

Dockstore ToolTester
--------------------


Dockstore ToolTester is a semi-automated process where Dockstore will attempt to launch certain verified tools/workflows through the latest Dockstore CLI.
Typically this launching process occurs before a Dockstore CLI release and is done so in order to ensure compatibility. The logs contain much useful information:

-  Dockstore CLI version used
-  pip packages installed
-  version of the tool/workflow that was launched
-  time when launched
-  runner that was used (cromwell, cwltool, etc)
-  files used (which descriptor file, which test parameter file)

.. _dockstore-tool-md5sum: https://dockstore.org/containers/quay.io/briandoconnor/dockstore-tool-md5sum:master?tab=info
.. _files endpoint: https://dockstore.org/api/static/swagger-ui/index.html#/GA4GH/toolsIdVersionsVersionIdTypeFilesGet_1
