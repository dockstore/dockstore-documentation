Dockstore CLI FAQ
=================

For general FAQs not related to the Dockstore CLI, please see :doc:`our main FAQ page </faq>`.

.. contents:: Table of Contents
  :local:

How does launching CWLs with Dockstore CLI compare with cwltool?
----------------------------------------------------------------

Under the hood, the Dockstore CLI invokes cwltool to launch CWL workflows. However, it adds additional features. The Dockstore CLI can generate JSON parameter files from
entries on Dockstore (``dockstore tool convert``). 
Additionally, when launching tools, the Dockstore CLI makes it easy to specify entries
from the Dockstore website. We can also provision input and output files using HTTP,
FTP, S3, and GCS. As of Release 1.12, the Dockstore CLI has support for running on `a WES server <https://github.com/ga4gh/workflow-execution-service-schemas>`__. We also have preliminary support for `Synapse <https://www.synapse.org/>`__ and the `ICGC Storage
client <https://docs.icgc.org/download/guide/#score-client-usage>`__. Please see `file provisioning plugins <https://github.com/dockstore/dockstore-cli/tree/master/dockstore-file-plugin-parent>`__
for more information on these two file transfer sources.

.. _how-do-i-use-the-dockstore-cli-on-a-mac:

How do I use the Dockstore CLI on a Mac?
----------------------------------------

See `Docker for Mac <https://docs.docker.com/engine/installation/mac/>`__ for installation information.

.. note:: Docker behaves a bit differently on a
    `Mac <https://docs.docker.com/docker-for-mac/osxfs/#/namespaces>`__ than
    on a typical Ubuntu machine. By default the only shared volumes are
    /Users, /Volumes, /tmp, and /private. Note that /var is not a shared
    directory (and can't be set as one). ``cwltool`` uses your TMPDIR (the
    env variable) to setup volumes with Docker, which on a Mac can default
    to a subdirectory of /var. In order to get ``cwltool`` working on your
    Mac, you need to set your TMPDIR to be under one of the shared volumes
    in Docker for Mac. You can do this by doing something similar to the
    following:
    ::

        export TMPDIR=/tmp/docker_tmp

By default, Docker for Mac allocates fewer resources (CPU, Memory, Swap)
to containers compared to what is available on your host machine. You
can change what it allocates using the Docker for Mac GUI under
``Preferences > Advanced`` as described
`here <https://docs.docker.com/docker-for-mac/#advanced>`__.

* The default allocation can cause workflows or tools to fail without informing the user with a memory or resource related error message. If you find that your workflow or tool is behaving differently on a Mac compared to a similarly resourced Ubuntu environment, you can try increasing the resources allocated to Docker on the Mac to resolve the discrepancy.

How do I launch tools/workflows without internet access on compute nodes?
-------------------------------------------------------------------------

Some tools/workflows require Docker images to launch even if they are
local entries. If the compute nodes do not have internet access, you can
follow these steps:

1. download the Docker image(s) on the head node which does have internet access using the ``docker save -o <filename> <imagename>``
2. ensure that the ``<imagename>`` matches the image name specific in the CWL or WDL descriptor 
3. place the image file(s) in a location that the compute nodes have access to (make sure there are only images in that directory)
4. specify in the dockstore config file (default ~/.dockstore/config) the directory that contains your image(s) using ``docker-images = /home/user/docker_images_directory``

The Dockstore CLI will automatically load all Docker images in the
directory specified prior to a ``launch --local-entry`` command.

.. _return-code-wdl:

How do I find the return code for a WDL task?
---------------------------------------------

The numeric return code for a WDL task will be in that task's execution folder. It is a single file named `rc` with no extension. Generally speaking, a 0 is a success, and anything else is a failure.

Let's say you are running the vcf2gds workflow, which runs the check-gds task as a scattered task on an array of three files. Cromwell will refer to each instance of that scattered task as a "shard" and will name them starting with 0. If you notice that shard 0 seems to have failed, look for `/cromwell-executions/[workflow ID]/call-check_gds/shard-0/execution/rc` keeping in mind that the workflow ID will usually be a long mix of numbers, letters, and dashes such as 18a85cc0-aa59-4749-b1b9-e2580ed5e557.


.. _cromwell-docker-lockup:

I was running a WDL locally, but some of my tasks are failing randomly and/or now I cannot use Docker.
------------------------------------------------------------------------------------------------------

This is a known issue with how Cromwell and Docker, which the Dockstore CLI uses to launch WDL workflows, manage resources on a local machine. Certain problems related to resource management may happen when running locally that do not happen when running on the cloud. These problems are much more likely to happen if you are running a computationally intensive scattered task, such as LD pruning 23 chromosomes where each chromosome is an instance of a scattered task. The two most common problems we see are a "Docker lockup" and stochastic failure of tasks. It is possible for one, both, or neither of these problems to occur during a single submission.

If a Docker lockup happens, you will notice in-progress WDL tasks do not progress beyond the WaitingForReturnCode status on the command line. Additionally, you will be temporarily unable to "spin up" any Docker containers, even outside of Cromwell. Thankfully, this state can be resolved by restarting the Docker service via the Docker Desktop dropdown, or entering ``service docker restart`` on the command line.

The other issue we often see is some instances of scattered tasks getting `sigkilled <https://www.gnu.org/software/libc/manual/html_node/Termination-Signals.html>`__ by the operating system. You will know when this happens because the `rc` (return code) file will read 137. If it reads anything except 137, then you can assume that it wasn't actually a resource management error and look in stderr or stdout for the true culprit. For more on return codes, see :ref:`this FAQ <return-code-wdl>` entry.

To prevent these issues from happening, we recommend setting up your Cromwell configuration file to limit how many scattered tasks run at once, and then setting up the Dockstore CLI to make use of that Cromwell configuration file. :doc:`A step-by-step tutorial is available here. </advanced-topics/dockstore-cli/local-cromwell-config>`

The CLI is failing with Java 8 or 11
------------------------------------

If you see the following error when running the Dockstore CLI, you need
to upgrade your Java version:

::

    $ dockstore
    Error: A JNI error has occurred, please check your installation and try again
    Exception in thread "main" java.lang.UnsupportedClassVersionError: io/dockstore/client/cli/Client has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java Runtime only recognizes class file versions up to 52.0

The Dockstore CLI as of 1.7.0 is compiled and tested using Java 11 due
to the Java 8 EOL. You will need to upgrade from Java 8 to use CLI versions betweenn 1.7 and 1.13.

The Dockstore CLI as of 1.14.0 is compiled and tested using Java 17 due
to the approaching Java 11 EOL. You will need to update to Java 17 to use the CLI version 1.14.0+.
