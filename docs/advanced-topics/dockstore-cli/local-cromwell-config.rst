Cromwell, when running locally, loses the ability to set compute resources within what is specified in a task's runtime attributes. This is a problem with scattered tasks, as by default, every instance of a scattered task may attempt to execute at the same time. As such, the local version of Cromwell sometimes uses too many resources when running scattered tasks, causing some or all instances of the scattered task to get [sigkilled](https://www.gnu.org/software/libc/manual/html_node/Termination-Signals.html). There is also the possability of concurrent instances of a scattered task locking up Docker for your operating system. 

.. tip::  If a Docker lockup happens, you will notice tasks do not progress beyond WaitingForReturnCode and you will be temporarily unable to use Docker on your OS. This can be resolved by restarting Docker on your machine.

The easiest way to avoid these issues is to set up a Cromwell configuration file that sets concurrent-job-limit. Of course, there is a tradeoff: If you set a concurrent-job-limit, tests involving scattered tasks will execute slower as less instances of a scattered task will run in parallel. That being said, we still recommend setting this value when running on a local machine, as it makes Cromwell much more stable.

1. Download `this template file <https://github.com/broadinstitute/cromwell/blob/develop/cromwell.example.backends/cromwell.examples.conf>`__ and name it ``.cromwell.conf``
2. Uncomment ``#default = "LocalExample"`` in the ``backend`` section in order to override the default local Cromwell setup with what is in the configuration file.
3. Under ``LocalExample``, under ``config``, uncomment the setting for ``concurrent-job-limit`` and set it to 1. Note that this is an integer, not a boolean; you could set it to 2 if you want to up to two jobs to run at once.  

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

How do I ensure the Dockstore CLI is using my Cromwell configuration file?
--------------------------------------------------------------------------
You may optionally edit ``root = "cromwell-executions"`` to something else if you wish to be certain that your configuration is getting used, as it will change the name of the executions folder, making it immediately clear that your config is being used. Might we suggest ``root = "dockstore-is-cool"``?