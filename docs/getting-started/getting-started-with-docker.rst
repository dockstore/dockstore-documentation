Getting Started with Docker
===========================

Tutorial Goals
--------------
This is the first part of our "Getting Started" tutorial series, where we will walk you through the creation of a tool called BAMstats and publish it onto Dockstore. This particular page, "Getting Started with Docker," will go through the basics of Docker and have you develop a Dockerfile for the BAMstats tool.

This tutorial assumes you have basic knowledge of a Unix-like file system, such as what a working directory is, and how to move between directories on the command line.

-  Learn about Docker
-  Create a Dockerfile
-  Use the Dockerfile you created to make a Docker image for a real bioinformatics tool
-  Create a tag locally
-  Test your Docker image locally

Introduction to Docker
----------------------

.. note:: See `Docker Overview <https://docs.docker.com/get-started/overview/>`__ for an excellent overview of Docker.

There is a good chance that you have heard of containerization. A container is essentially an emulated filesystem that bundles up some kind of software. It's similar to a virtual machine, but is usually much lighter on system resources, because a container (unlike a VM) does not need to run an extra operating system.

Docker is a well-known type of containerization software. It provides a fast environment for both users and developers. A developer can package software and its dependencies into an Docker image, and then share that Docker image with users. Users who download your Docker image and run it with the Docker program will be able to run the software you packaged without having to handle the installation of your program's prerequisites or anything else; it's ready to go as-is.

Docker images are usually shared on registries such as Quay.io, Docker Hub, and GitLab. When a user downloads an image and runs it locally, it creates an editable copy of the image. The editable copy is called a Docker container. You can think of an image as a template, and a container as something made from that template.

What do I need to run Docker?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Docker generally recommends that people `install it via Docker Desktop <https://docs.docker.com/desktop/#download-and-install>`__. Docker Desktop includes the command line Docker Engine program that we will be using in this tutorial, plus a GUI to make adjustment of certain settings a little easier. You could instead `install the Docker Engine from binaries <https://docs.docker.com/engine/install/binaries/>`__, but this is generally not recommended as it is a little harder to install than Docker Desktop and does not automatically receive updates. In either case, to install a modern version of Docker, you will need a 64 bit system. Generally speaking you will also need root permissions on whatever system you are running on.

Users of HPC (high performance compute) systems may not be able to run Docker Engine directly, depending on your sysadmin's policies and the details of your HPC's scheduling system. We can't go over all of possible HPC setups here, but we recommend checking out `Singularity <https://sylabs.io/guides/2.6/user-guide/singularity_and_docker.html>`__ and `Shifter <https://github.com/NERSC/shifter>`__, both of which are designed for running Docker images without using the Docker Engine program. If your HPC does not support Docker Engine, there is a strong chance it is already set up with an alternative.

For the sake of simplicity, this tutorial will assume you are running Docker Engine on a non-HPC Unix-like system.

Tutorial: Making a Dockerfile for the BAMstats tool
---------------------------------------------------

Create a new repository
~~~~~~~~~~~~~~~~~~~~~~~

See the
`dockstore-tool-bamstats <https://github.com/CancerCollaboratory/dockstore-tool-bamstats>`__
repository on GitHub which we created as an example. This is linked to
the Quay.io repository at
`dockstore-tool-bamstats <https://quay.io/repository/collaboratory/dockstore-tool-bamstats>`__.

For the rest of this tutorial, you may wish to work in your own
repository with your own tool or "fork" the repository above into your
own GitHub account.

With a repository established in GitHub, the next step is to create the
Docker image with BAMStats correctly installed.

Create a Dockerfile
~~~~~~~~~~~~~~~~~~~

We will create a Docker image with BAMStats and all of its dependencies
installed. To do this we must create a ``Dockerfile``. Here's a sample
`Dockerfile <https://github.com/CancerCollaboratory/dockstore-tool-bamstats/blob/develop/Dockerfile>`__:

.. code:: dockerfile

    #############################################################
    # Dockerfile to build a sample tool container for BAMStats
    #############################################################

    # Set the base image to Ubuntu
    FROM ubuntu:14.04

    # File Author / Maintainer
    MAINTAINER Brian OConnor <briandoconnor@gmail.com>

    # Setup packages
    USER root
    RUN apt-get -m update && apt-get install -y wget unzip openjdk-7-jre zip

    # get the tool and install it in /usr/local/bin
    RUN wget -q http://downloads.sourceforge.net/project/bamstats/BAMStats-1.25.zip
    RUN unzip BAMStats-1.25.zip && \
        rm BAMStats-1.25.zip && \
        mv BAMStats-1.25 /opt/
    COPY bin/bamstats /usr/local/bin/
    RUN chmod a+x /usr/local/bin/bamstats

    # switch back to the ubuntu user so this tool (and the files written) are not owned by root
    RUN groupadd -r -g 1000 ubuntu && useradd -r -g ubuntu -u 1000 ubuntu
    USER ubuntu

    # by default /bin/bash is executed
    CMD ["/bin/bash"]

This Dockerfile has a lot going on in it. There are good tutorials
online about the details of a Dockerfile and its syntax. An excellent
resource is the Docker website itself, including the `Best practices for
writing
Dockerfiles <https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/>`__
webpage. We'll highlight some sections below:

.. code:: dockerfile

    FROM ubuntu:14.04

This uses the ubuntu 14.04 base distribution. How do we know to use
``ubuntu:14.04``? This comes from either a search on Ubuntu's home page
for their "official" Docker images, or you can simply go to
`DockerHub <https://hub.docker.com>`__ or `Quay <https://quay.io>`__ and
search for whatever base image you like. You can extend anything you
find there. So if you come across an image that contains most of what
you want, you can use it as the base here. Just be aware of its source:
Many people tend to stick with "official", basic images for security reasons.

.. code:: dockerfile

    MAINTAINER Brian OConnor <briandoconnor@gmail.com>

You should include your name and contact information.

.. code:: dockerfile

    USER root
    RUN apt-get -m update && apt-get install -y wget unzip openjdk-7-jre zip
    RUN wget -q http://downloads.sourceforge.net/project/bamstats/BAMStats-1.25.zip
    RUN unzip BAMStats-1.25.zip && \
        rm BAMStats-1.25.zip && \
        mv BAMStats-1.25 /opt/

This switches to the ``root`` user to perform software installs. It
downloads BAMStats, unzips it, and installs it in the correct location,
``/opt``.

This is one of the main advantages of Docker. On some systems the above process might take days or weeks of working with a sysadmin to install dependencies. Instead of installing dependencies on every machine someone might want to run a workflow/tool on, we can create a Docker image that wraps that workflow/tool. With Docker, we only need to correctly configure the environment and dependencies for a program once, and once that Docker image is set up, we avoid repeating that process. All we need to do is transfer that Docker image to other machines, and they will be able to run what's inside it. This greatly simplifies the process for other users.

.. code:: dockerfile

    COPY bin/bamstats /usr/local/bin/
    RUN chmod a+x /usr/local/bin/bamstats

This copies the local helper script ``bamstats`` from the git checkout
directory to ``/usr/local/bin``. (We'll talk more about that helper script later.) This is an important example; it shows
how to use ``COPY`` to copy files in the git directory structure to
inside the Docker image. After copying to ``/usr/local/bin`` we make the helper script executable by all users in the next line via `chmod` which is used to modify permissions in Unix-like systems.

.. code:: dockerfile

    RUN groupadd -r -g 1000 ubuntu && useradd -r -g ubuntu -u 1000 ubuntu
    USER ubuntu

    # by default /bin/bash is executed
    CMD ["/bin/bash"]

The user ``ubuntu`` is created and switched to in order to make file
ownership easier, and the default command for this Docker image is set to
``/bin/bash`` which is a typical default. ``bash`` is the command line interpreter that most Unix-like systems use, so we essentially say that by default this Docker image will allow the user to directly interact with it using bash commands.

An important thing to note is that this ``Dockerfile`` only scratches
the surface. Take a look at `Best practices for writing
Dockerfiles <https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/>`__
for an in-depth look at writing Dockerfiles.

Read more on the development process at
`https://docs.docker.com <https://docs.docker.com/>`__. For information
on building your Docker image on Quay.io we recommend their
`tutorial <https://quay.io/tutorial/>`__.

Build a Docker Image
~~~~~~~~~~~~~~~~~~~~

Now that you've created the ``Dockerfile``, the next step is to build the image. Install `Docker Engine <https://docs.docker.com/engine/install/ubuntu/>`__ or `Docker Desktop <https://docs.docker.com/desktop/linux/install/>`__. Once it is installed, you can use this command to build your Docker image:

::

    $> docker build -t quay.io/collaboratory/dockstore-tool-bamstats:1.25-6 .

The ``.`` is the path to the location of the Dockerfile, which is in the
same directory here. The ``-t`` parameter is the "tag" that this Docker
image will be called locally when it's cached on your host. A few things
to point out: the ``quay.io`` part of the tag typically denotes that
this was built on Quay.io (which we will see in a later section). I'm
manually specifying this tag so it will match the Quay.io-built version.
This allows me to build and test locally then, eventually, switch over
to the quay.io-built version. The next part of the tag,
``collaboratory/dockstore-tool-bamstats``, denotes the name of the tool
which is derived from the organization and repository name on Quay.io.
Finally ``1.25-6`` denotes a version string. Typically, you want to sync your version string with releases on GitHub.

The tool should build normally and should exit without errors. You
should see something like:

::

    Successfully built 01a7ccf55063

It might have a different name than ``01a7ccf55063`` but it should be a success regardless. Check that the tool is now in your local Docker image cache:

::

    $> docker images | grep bamstats
    quay.io/collaboratory/dockstore-tool-bamstats   1.25-6  01a7ccf55063   2 minutes ago   538.3 MB

Great! This looks fine!

Testing the Docker Image Locally
--------------------------------

OK, so you've built the image and created a tag. Now what?

The next step will be to test the tool directly via Docker to ensure
that your ``Dockerfile`` is valid and correctly installed the tool. If
you were developing a new tool, there might be multiple rounds of
``docker build``, followed by testing with ``docker run`` before you get
your Dockerfile right. 

This command will execute the Docker image we just made, launching it as a container. If you wish to run this yourself, make sure you launch on a host with at least 8GB of RAM and dozens of GB of disk space:

::

    $> docker run -it -v `pwd`:/home/ubuntu --user `echo $UID`:1000 quay.io/collaboratory/dockstore-tool-bamstats:1.25-6 /bin/bash

.. note:: This command expects your `UID <https://en.wikipedia.org/wiki/User_identifier>`__ to be 1000. If it is not, you need to add ``--user <your-id>:1000``.

You'll be dropped into a bash shell which works just like the Linux
environments you normally work in. We will come back to what ``-v`` is
doing in a bit. The goal now is to exercise the tool and make sure it
works as you expect. BAMStats is a very simple tool and generates some
reports and statistics for a BAM file. Let's run it on some test data
from the 1000 Genomes project:

::

    # this is inside the running Docker container
    $> cd /home/ubuntu
    $> wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/NA12878/alignment/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam
    # if the above doesn't work here's an alternative location
    $> wget https://s3.amazonaws.com/oconnor-test-bucket/sample-data/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam
    $> /usr/local/bin/bamstats 4 NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam

What's really going on here? The ``bamstats`` command above is a simple script someone wrote to make it easier to call BAMStats. This is the same helper script we mentioned earlier when writing the Dockerfile. This is what the ``COPY`` command copied into the Docker image via the Dockerfile.
Here's the helper script's contents:

::

    #!/bin/bash
    set -euf -o pipefail

    java -Xmx$1g -jar /opt/BAMStats-1.25/BAMStats-1.25.jar -i $2 -o bamstats_report.html -v html
    zip -r bamstats_report.zip bamstats_report.html bamstats_report.html.data
    rm -rf bamstats_report.html bamstats_report.html.data

You can see it just executes the BAMStats jar - passing in the GB of
memory and the BAM file while collecting the output HTML report as a zip
file followed by cleanup.

.. note::
    Notice how the output is written to whatever the current
    directory is. This is the correct directory to put your output in since
    the CWL tool described later assumes that outputs are all located in the
    current working directory that it executes your command in.

Let's take another look at the ``docker run`` command. The ``-v`` parameter is mounting the current working
directory into ``/home/ubuntu`` which was the directory we worked in
when running ``/usr/local/bin/bamstats`` above. The net effect is when
you exit the Docker container (with command ``exit`` or pressing
``ctrl + d``), you're left with a ``bamstats_report.zip`` file in the
current directory. This is a key point: It shows you how files are
retrieved from inside a Docker container.

You can now unzip and examine the ``bamstats_report.zip`` file on your
computer to see what type of reports are created by this tool. For
example, here's a snippet:

.. figure:: /assets/images/docs/report.png
   :alt: Sample report

   Sample report

Rather than interactively working with the image, you could also run
your Docker image from the command-line.

::

    $> wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/NA12878/alignment/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam
    $> docker run -w="/home/ubuntu" -it -v `pwd`:/home/ubuntu --user `echo $UID`:1000 quay.io/collaboratory/dockstore-tool-bamstats:1.25-6 bamstats 4 NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam

Next Steps
----------

**You could stop here!** However, we currently lack a standardized way to describe how to run this tool. That's what descriptor languages and Dockstore provide. We think it's valuable, and there's an increasing number of tools and workflows designed to work with various descriptor languages. To that end, we have continued this tutorial to describe how the command-line programs and input files can be parameterized and constructed via a descriptor language.

There are several descriptor languages available on Dockstore. Follow the
links to get an introduction.

- :doc:`CWL <getting-started-with-cwl>`
- :doc:`WDL <getting-started-with-wdl>`
- :doc:`Nextflow <getting-started-with-nextflow>`
- :doc:`Galaxy <getting-started-with-galaxy>`

.. discourse::
    :topic_identifier: 1280
