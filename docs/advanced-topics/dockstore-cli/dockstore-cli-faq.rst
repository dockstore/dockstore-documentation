Dockstore CLI FAQ
=================

How does launching with Dockstore CLI compare with cwltool?
-----------------------------------------------------------

The Dockstore CLI has utilities to generate JSON parameter files from
entries on Dockstore (``dockstore tool convert``).

When launching tools, the Dockstore CLI makes it easy to specify entries
from Dockstore. We can also provision input and output files using HTTP,
FTP, and S3. We also have preliminary support for
`Synapse <https://www.synapse.org/>`__ and the `ICGC Storage
client <https://docs.icgc.org/download/guide/#score-client-usage>`__.
Please see `file provisioning
plugins <https://github.com/dockstore/dockstore-cli/tree/master/dockstore-file-plugin-parent>`__
for more information on these two file transfer sources.

The CLI is failing with Java 8
------------------------------

If you see the following error when running the Dockstore CLI, you need
to upgrade your Java version:

::

    $ dockstore
    Error: A JNI error has occurred, please check your installation and try again
    Exception in thread "main" java.lang.UnsupportedClassVersionError: io/dockstore/client/cli/Client has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java Runtime only recognizes class file versions up to 52.0

The Dockstore CLI as of 1.7.0 is compiled and tested using Java 11 due
to the Java 8 EOL. You will need to upgrade from Java 8 to use the CLI.

The CLI is failing with Java 8
------------------------------

If you see the following error when running the Dockstore CLI, you need
to upgrade your Java version:

::

    $ dockstore
    Error: A JNI error has occurred, please check your installation and try again
    Exception in thread "main" java.lang.UnsupportedClassVersionError: io/dockstore/client/cli/Client has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java Runtime only recognizes class file versions up to 52.0

The Dockstore CLI as of 1.7.0 is compiled and tested using Java 11 due
to the Java 8 EOL. You will need to upgrade from Java 8 to use the CLI.

.. _how-do-i-use-the-dockstore-cli-on-a-mac:

How do I use the Dockstore CLI on a Mac?
----------------------------------------

See `Docker for Mac <https://docs.docker.com/engine/installation/mac/>`__ for installation information.

.. note:: Docker behaves a bit differently on a
    `Mac <https://docs.docker.com/docker-for-mac/osxfs/#/namespaces>`__ than
    on a typical Ubuntu machine. By default the only shared volumes are
    /Users, /Volumes, /tmp, and /private. Note that /var is not a shared
    directory (and can't be set as one). ``cwltool`` uses your TMPDIR (the
    env variable) to setup volumes with docker, which on a Mac can default
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

How can I use the Dockstore CLI with Python 2?
----------------------------------------------

Python 2 support ended in 2020. You can get the Python 2 requirements.txt with ``curl -o requirements.txt "https://dockstore.org/api/metadata/runner_dependencies?python_version=2"``
but it is currently untested.

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
directory specified prior to a ``launch --local-entry`` command