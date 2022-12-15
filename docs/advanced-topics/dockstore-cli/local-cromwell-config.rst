Using a Cromwell config with the Dockstore CLI
==============================================

Why set up a Cromwell configuration file?
-----------------------------------------

It is not necessary to set up a configuration file to use Cromwell or the Dockstore CLI, but advanced users may find some settings they may want to change. Additionally, setting up a Cromwell configuration file is the best way to avoid :ref:`Docker lockups and sigkilled tasks <cromwell-docker-lockup>` from happening when working with scattered tasks. Because avoiding those lockups is one of the more common use cases for setting up a Cromwell configuration file, we will focus on that specific use case here, but you can apply this to modify other Cromwell settings as needed.

To help keep scattered tasks from taking too many local resources, you can set up a Cromwell configuration file that sets a concurrent-job-limit. Of course, there is a tradeoff: If you set a concurrent-job-limit, tests involving scattered tasks will execute slower as fewer instances of a scattered task will run in parallel. That being said, we still recommend setting this value when running on a local machine, as it makes Cromwell much more stable.

1. Download `this template file <https://github.com/broadinstitute/cromwell/blob/develop/cromwell.example.backends/cromwell.examples.conf>`__ and name it ``.cromwell.conf`` before placing it in your home directory, e.g. ``/Users/ash`` (MacOS) or ``/home/ash`` (Linux). If you are on Mac OS, you may get a notification about naming the file like this -- this is normal; Mac OS normally hides files that have a period at the start of the name (called "dot files") to prevent people from deleting important operating system files by accident. 
2. Uncomment ``#default = "LocalExample"`` in the ``backend`` section in order to override the default local Cromwell setup with what is in the configuration file.
3. Under ``LocalExample``, under ``config``, uncomment the setting for ``concurrent-job-limit`` and set it to 1. Note that this is an integer, not a boolean; you could set it to 2 if you want to up to two jobs to run at once for example.  

The relevent part of your configuration file should now look like this, if we exclude the other providers that come before LocalExample:

::

    backend {
    # Override the default backend.
    default = "LocalExample"

    # The list of providers.
    providers {
       
        # Define a new backend provider.
        LocalExample {
            # The actor that runs the backend. In this case, it's the Shared File System (SFS) ConfigBackend.
            actor-factory = "cromwell.backend.impl.sfs.config.ConfigBackendLifecycleActorFactory"
          
            # The backend custom configuration.
            config {
                # Optional limits on the number of concurrent jobs
                concurrent-job-limit = 1

Close that file and add the following line to ``~/.dockstore/config`` in order to make the Dockstore CLI use the Cromwell configuration file.

::

    cromwell-vm-options: -Dconfig.file=<absolute-path-to-your-cromwell-config>

So, for example:

::

    cromwell-vm-options: -Dconfig.file=/Users/ash/.cromwell.conf

You're now all set up -- the Dockstore CLI will use this configuration file, and will only allow one instance of a scattered task to run at once.

How can I ensure the Dockstore CLI is using my Cromwell configuration file?
---------------------------------------------------------------------------
You may optionally edit ``root = "cromwell-executions"`` to something else if you wish to be certain that your configuration is getting used, as it will change the name of the executions folder, making it immediately clear that your config is being used. Might we suggest ``root = "dockstore-is-cool"``?

.. discourse::
    :topic_identifier: 6284
