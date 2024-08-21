.. note:: The topics in this tutorial are experimental. We are working on improving support for rootless containers,
   but for now, some things may not be compatible.

Docker Alternatives
===================

In some situations using Docker may be impractical because it requires all users to have root access.
Several alternatives have been developed to make it possible to run rootless containers.

.. contents::
   :local:
   :depth: 2

While Dockstore uses Docker by default, if necessary it may be possible to run your workflows with one
of these alternatives. Because the call to Docker or an alternative is made by the workflow runner, usually cwltool
or Cromwell, and not Dockstore directly, the difficulty of configuring a Docker alternative depends on the workflow
type. Some Dockstore entries will run seamlessly without Docker, and some may be entirely incompatible in a rootless
environment.

Rootless Docker
---------------
In December 2020 with the release of Docker Engine v20.10, "rootless Docker" has officially become part of Docker itself.
While this does open the door for some systems, it does require special setup and it has some limitations. You can read all about it on `Docker's own docs about Rootless Mode <https://docs.docker.com/engine/security/rootless/>`__.

Rootless Docker, a product of Docker, is very convenient because no configuration of Dockstore is required to use it.
When it is installed, all ``docker`` commands are run in rootless mode without needing to set this as an option.
Therefore, the normal Docker commands invoked by cwltool and Cromwell will be executed rootlessly.

Rootless Docker installation is simple and does not require root. Regular Docker must not already be installed.
Just execute the installation script:

::

    curl -sSL https://get.docker.com/rootless | sh

It may display a message that you need to add it to the PATH or do some other configuration.
You can confirm that rootless Docker is working with ``docker info``;
under ``Security Options`` it should output ``rootless``.

cwltool
~~~~~~~

cwltool `documents <https://github.com/common-workflow-language/cwltool#using-user-space-replacements-for-docker>`_
support for some Docker alternatives but does not mention rootless Docker. In our testing, it seems the ``docker run``
command issued by cwltool is incompatible with rootless Docker and causes a permissions error with the volume mapping.
cwltool with rootless Docker did not work for any tested workflows.

Cromwell
~~~~~~~~

As rootless Docker does not require any change of configuration to use, it can be used with Cromwell through
Dockstore despite the lack of a Cromwell config option.

Cromwell does not document support for rootless Docker, but they seem to be compatible. Most WDL workflows we tried
worked smoothly with rootless Docker.

Cromwell supports most CWL features as well as WDL. You can use Cromwell instead of cwltool when running CWL files
with Dockstore by adding the following line to your ``~/.dockstore/config``:
::

    cwlrunner: cromwell

This may not work with all CWL entries, but it is a good workaround for the cwltool incompatibility described above.

Singularity
-----------

Singularity is perhaps the most well-supported Docker alternative. Singularity can pull Docker images and build them
into its own image format (.sif), but not all Docker features are compatible. For instance, dockerfile ``USER``
commands are not compatible with Singularity.
A common problem observed when running Dockstore entries with Singularity is that the process fails on
``singularity pull`` because the entry's dockerfile or its base image contains a ``USER root`` command. In many cases
the use of root may be unnecessary. Whenever possible, dockerfiles on Dockstore should avoid using root.

.. note:: A best practice when using Docker for workflows is not to rely on a specific user.
   This is doubly true for Singularity where it is not just best practice but necessary.

Singularity provides a `fake root <https://docs.sylabs.io/guides/3.4/user-guide/fakeroot.html>`_ option that might circumvent
the problems using root in certain situations. There does not seem to be a way to use this option through cwltool. It
can be used with Cromwell by editing the Singularity command format set in your Cromwell config file.

More information about compatibility of dockerfiles with Singularity
can be found `here <https://docs.sylabs.io/guides/3.4/user-guide/singularity_and_docker.html#best-practices>`__.

Singularity can be installed following the instructions
`here <https://github.com/sylabs/singularity/blob/main/INSTALL.md>`__.

.. note:: Multiple installations of Go have been known to cause a ``Go compiler not found`` error when installing Singularity.
   If you see this error, please uninstall all versions of Go and reinstall just one version.

cwltool
~~~~~~~

Singularity is available as a command line option for cwltool like this:
::

    cwltool --singularity <workflow> <input json>

To set this option through Dockstore, add the following line to your ``~/.dockstore/config``:
::

    cwltool-extra-parameters: --singularity

Cromwell
~~~~~~~~

Cromwell can be configured to use Singularity instead of Docker as described
`here <https://cromwell.readthedocs.io/en/stable/tutorials/Containers/#singularity>`__.
This requires creating a Cromwell config file with a section describing the backend provider settings.
Examples of this are available in the Cromwell GitHub
`here <https://github.com/broadinstitute/cromwell/tree/develop/cromwell.example.backends>`__.

To tell Dockstore to run Cromwell with a custom configuration, such as the example config file linked above,
add a line to your ``~/.dockstore/config``:
::

    cromwell-vm-options: -Dconfig.file=<absolute path to your Cromwell conf>

Podman
---------------

Podman is a daemon-less alternative of Docker that allows end users to run Docker/Open Container Initiative (OCI) containers without root privileges.

Podman can be installed following the instructions
`here <https://podman.io/docs/installation>`__.

cwltool
~~~~~~~

Podman is also available as a command line option for cwltool like this:
::

    cwltool --podman <workflow> <input json>

To set this as the default option when running via the Dockstore CLI, add the following line to your ``~/.dockstore/config``:
::

    cwltool-extra-parameters: --podman

Cromwell
~~~~~~~~
For Cromwell, we can set a symbolic link to run Podman instead of Docker on workflows.
::

    ln -s /usr/bin/podman /usr/bin/docker

Note that you should not do this if you already have Docker installed on your machine.



.. discourse::
    :topic_identifier: 6476
