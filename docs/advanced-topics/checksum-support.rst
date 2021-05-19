#########
Checksums
#########

To help developers who want to distribute or run immutable copies of tools and workflows, Dockstore (1.9+) can provide checksums for files and Docker
images when certain conditions are met. Currently, checksums are not accessible through the UI, but can be fetched by using various TRS
endpoints. Keep reading to learn what is supported and how to retrieve the checksum information.

File Descriptor Checksum Support
================================
As of 1.9, Dockstore will calculate a SHA-1 checksum during a refresh for every container, descriptor, and test parameter file included in a
tool or workflow. Once the refresh is done, you must publish your entry in order to access the information via our `TRS V2 endpoints <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20>`_.
More specifically, the endpoints that contain checksums for files are as follows:

- `Descriptor (primary) <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdTypeDescriptorGet>`_
- `Descriptor (secondary) <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdTypeDescriptorRelativePathGet>`_
- `Test Parameter Files <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdTypeTestsGet>`_
- `Container Files <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdContainerfileGet>`_

The id parameter used in the endpoints above can be found on an entry's public page; underneath the Info tab, look for the bolded words **TRS**.

After gathering the checksum using the above method you can verify a descriptor's using the sha1sum terminal application.
This is done by requesting the PLAIN_WDL descriptor and piping the output to sha1sum.

::
    trsid=%23workflow%2Fgithub.com%2Fdockstore-testing%2Fdockstore-workflow-md5sum-unified%2Fwdl
    version=1.2.0
    curl -s https://dockstore.org/api/ga4gh/trs/v2/tools/$trsid/versions/$version/PLAIN-WDL/descriptor | sha1sum

The resulting checksum should match what was provided by the API above.

Docker Image Checksum Support
=============================
Checksum support for Docker images is more nuanced than it is for files. For quick reference, the table below displays the languages and
Docker image repositories currently available, and what action on Dockstore is required to collect this information.

.. raw:: html
    :file: ../_static/checksum-support.html

|

Once you perform the required action, you must also publish your entry in order to see the checksum info via the `TRS endpoints <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20>`_.
Descriptions for the two endpoints of note are as follows:

- To see all versions of an entry, use our `toolsGet <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsGet>`_  endpoint and fill out the id parameter
- To see a single version of an entry, go `here <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdGet>`_ and fill out id and version_id

Just like the file endpoints, the id parameter used in the endpoints above can be found on an entry's public page; underneath the Info tab, look for the bolded words **TRS**.

To verify a checksum as reported by the Dockstore API matches what you download from the Docker repository first find the checksum
and image path and registry using one of the above methods for the image you would like to verify. Then download the image using the
Docker CLI client.

::

    docker pull quay.io/briandoconnor/dockstore-tool-md5sum:1.0.4

When the download has completed a Digest is provided in the terminal output. This should match the checksum provided
by the Dockstore API.

Tools
-----
As noted in the table above, Docker image checksums are grabbed on refresh and should work as long as the image is from Quay.io, Docker Hub,
or GitLab. It's also important to note that this is done for the Docker image registered on the tool through Dockstore and not necessarily
the one included within the descriptor file itself.

Workflows
---------
For workflows, Docker image checksums are grabbed on snapshot. However, the Docker images we can retrieve from descriptor files
are more limited compared to the other checksum support covered so far. Although we can generally provide checksum info for referenced Docker
images for CWL, WDL, and NFL, there are some caveats. Most conditions are language specific, but for all workflow langagues, the images
referenced must be from Quay.io or Docker Hub and they must include a version. The following are the known constraints for each language.

.. There is a ticket to expand on when we are not able to parse the docker images. This is only what I'm fairly sure about...

Common Workflow Language
^^^^^^^^^^^^^^^^^^^^^^^^
- Various fields can be used to reference a Docker image, but we only support "dockerPull" for now.
- "$import" or "$include" can be used to reference a local or http(s) CWL descriptor, but we do not check for Docker image references made within files using http(s).

Workflow Descriptor Language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- The WDL docker attribute can be evaluated as an expression, but we only support it when the attribute is set using a string.

::

    runtime {
      # Unsupported
      # docker: "ubuntu:" + "18.04"

      # Unsupported
      # docker: "ubuntu:" + version

      # Supported
      docker: "ubuntu:18.04"
    }

Nextflow
^^^^^^^^
- Similar to WDL, a container can be set equal to an expression in Nextflow. Dockstore again supports simple strings, but also the container being set to a variable defined in the params scope. However, we do not support other types of expressions.

::

    // nextflow.config
    params {
      container = 'ubuntu:18.04'
      versionName = '18.04'
    }

    // conf/base.config
    process {
      // Unsupported
      container = "ubuntu:${params.versionName}"

      // Supported
      container = 'ubuntu:18.04'
      // Supported
      container = params.container
    }

- A Nextflow workflow can contain a "profiles" scope. Here, you can create different sets of configuration attributes. The workflow can then be run with whichever profiles are specified as a command line argument. If a Docker image is referenced within a profile, Dockstore will not recognize it.

::

    // nextflow.config
    params {
      container = 'ubuntu:18.04'
    }

    profiles {
      exampleProfile {
        // Unsupported
        container = 'ubuntu:18.04'
      }
    }

    // conf/base.config
    process {
      // Supported
      container = params.container
    }
