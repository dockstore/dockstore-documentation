#########
Checksums
#########

To help developers who want to distribute or run immutable copies of tools and workflows, Dockstore (1.9+) can provide checksums for files and Docker
images when certain conditions are met. Currently, checksums are not accessible through the UI, but can be fetched by using various TRS
endpoints. Keep reading to learn what is supported and how to retrieve the checksum information.

File Descriptor Checksum Support
================================
Dockstore returns a SHA-256 checksum for every container, descriptor, and test parameter file included in a
tool or workflow. You must publish your entry in order to access the information via our `TRS V2 endpoints <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20>`_.
More specifically, the endpoints that contain checksums for files are as follows:

- `Descriptor (primary) <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdTypeDescriptorGet>`_
- `Descriptor (secondary) <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdTypeDescriptorRelativePathGet>`_
- `Test Parameter Files <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdTypeTestsGet>`_
- `Container Files <https://dockstore.org/api/static/swagger-ui/index.html#/GA4GHV20/toolsIdVersionsVersionIdContainerfileGet>`_

The id parameter used in the endpoints above can be found on an entry's public page; underneath the Info tab, look for the bolded words **TRS**.

After gathering the checksum using the above method you can verify a descriptor's checksum using the shasum terminal application.
This is done by requesting the PLAIN_WDL, PLAIN_CWL, PLAIN_NFL, or PLAIN_GALAXY descriptor type and piping the output to shasum.

::

    ~$ TRS_ID=%23workflow%2Fgithub.com%2Fdockstore-testing%2Fdockstore-workflow-md5sum-unified%2Fwdl
    ~$ TRS_VERSION=1.2.0
    ~$ curl -s https://dockstore.org/api/ga4gh/trs/v2/tools/$TRS_ID/versions/$TRS_VERSION/WDL/descriptor | jq '.checksum'
    [
      {
        "checksum": "5afec4aaeaba5a8d1261a7fe4cbdb8ca1362a57561e03b7504fc633a1f87f0cd",
        "type": "sha-256"
      }
    ]
    ~$ curl -s https://dockstore.org/api/ga4gh/trs/v2/tools/$TRS_ID/versions/$TRS_VERSION/PLAIN_WDL/descriptor | shasum -a 256
    5afec4aaeaba5a8d1261a7fe4cbdb8ca1362a57561e03b7504fc633a1f87f0cd  -

The resulting checksum should match what was provided by the API above.

If you use the Dockstore CLI client, descriptor checksums are verified before being sent to the execution engine.

CLI Descriptor Validation Support
------------------------------------------
By default, when launching tools or workflows from the CLI, primary and secondary descriptors will be validated using their SHA-256 checksums. Checksums are
not validated when launching local entries.

You can prevent checksum validation with the ``--ignore-checksums`` flag. For example, the following command will not validate descriptor
checksums:

::

    dockstore [tool/workflow] launch --ignore-checksums --entry <entryPath> --json <parameterFile>


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

To verify if a checksum as reported by the Dockstore API matches what you download from the Docker registry, first find the checksum
and image path using one of the above methods for the image you would like to verify. Then download the image using the
Docker CLI client.

::

    docker pull quay.io/briandoconnor/dockstore-tool-md5sum:1.0.4

When the download has completed, a digest is provided in the terminal output. This should match the checksum provided
by the Dockstore API.

Verifying the image checksum can give you better guarantees the image has not changed since the workflow was published to Dockstore.
However, in some cases the image checksum may diverge, for example, if the image was defined in a git branch that has since
been updated. For best results, and to avoid your Docker image being deleted because of a registry's retention policy,
use Docker images referred to by a tagged version or digest. The verification features available may vary between execution engines.

.. note::

  For Amazon ECR and GitHub Container Registry images, checksum gathering will only work with Docker images produced with
  Docker version 1.10 or later, which creates images using the Docker V2 Schema 2 image manifest.
  Docker has deprecated the Schema 1 manifest and we do not support it.

For more information on Docker registry retention policies see posts from `Docker <https://www.docker.com/blog/scaling-dockers-business-to-serve-millions-more-developers-storage/>`_,
`AWS <https://aws.amazon.com/blogs/compute/clean-up-your-container-images-with-amazon-ecr-lifecycle-policies/>`_,
or `Azure <https://docs.microsoft.com/en-us/azure/container-registry/container-registry-retention-policy>`_.

Tools
-----
As noted in the table above, Docker image checksums are grabbed on refresh and should work as long as the image is from Quay.io, Docker Hub,
Amazon ECR, or GitLab. It's also important to note that this is done for the Docker image registered on the tool through Dockstore and not necessarily
the one referenced within the descriptor file itself.

Workflows and GitHub App Tools
------------------------------
For workflows and GitHub App tools, Docker image checksums are grabbed on snapshot. However, the Docker images we can retrieve from descriptor files
are more limited compared to the other checksum support covered so far. Although we can generally provide checksum info for referenced Docker
images for CWL, WDL, and NFL, there are some caveats. Most conditions are language specific, but for all workflow languages, the images
referenced must be from Quay.io, Docker Hub, or Amazon ECR and they must include a version. The following are the known constraints for each language.

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

.. discourse::
    :topic_identifier: 6308
