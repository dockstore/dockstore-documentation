Dockstore CLI Overview
======================

The Dockstore CLI (command-line interface) allows you to interact with Dockstore from the command-line. You can interactively try things out in a terminal, use it in scripts, etc.

The CLI can perform various operations on tools and workflows, such as execution, searching, and publishing. It can also be used to validate .dockstore.yml files, to ensure that changes to your GitHub repository will be correctly processed by Dockstore.

It is beyond the scope of this page to document all the commands that can be executed with the CLI. We encourage you to explore all the possible commands in the CLI by using the CLI's help, described below.

Modes
-----

The CLI works by putting it into a mode. For example, if you you want to use the CLI against workflows, you put it into workflow mode by starting off with ``dockstore workflow ...``. You can see all possible modes by typing ``dockstore``:

::

  $ dockstore

  ...

  Usage: dockstore [mode] [flags] [command] [command parameters]

  Modes:
     tool                Puts dockstore into tool mode.
     workflow            Puts dockstore into workflow mode.
     checker             Puts dockstore into checker mode.
     plugin              Configure and debug plugins.
     deps                Print tool/workflow runner dependencies.
     yaml                Puts dockstore into yaml mode.

    ---------------------------------------------
    ...

Commands
--------

You can see the individual commands available to a mode by typing ``dockstore <mode>``. For example, to see the available commands for the workflow mode:

::

    dockstore workflow

    ... 

    Usage: dockstore workflow [flags] [command] [command parameters]

    Commands:

      convert          :  utilities that allow you to convert file types

      CWL              :  returns the Common Workflow Language Workflow definition for this entry
                          which enables integration with Global Alliance compliant systems

      download         :  download Workflows to the local directory

      info             :  print detailed information about a particular published Workflow

      label            :  updates labels for an individual Workflow

      launch           :  launch Workflows (locally)

      list             :  lists all the Workflows published by the user

      nfl              :  returns the Nextflow Workflow definition for this entry

      publish          :  publish/unpublish a Workflow in Dockstore

      refresh          :  updates your list of Workflows stored on Dockstore or an individual Workflow

      search           :  allows a user to search for all published Workflows that match the criteria

      star             :  star/unstar a Workflow in Dockstore

      test_parameter   :  updates test parameter files for a version of a Workflow

      WDL              :  returns the Workflow Descriptor Language definition for this entry

      wes              :  calls a Workflow Execution Schema API (WES) for a version of a Workflow

      manual_publish   :  registers a Github, Gitlab or Bitbucket workflow in Dockstore and then attempts to publish

      update_workflow  :  updates certain fields of a workflow

      version_tag      :  updates an existing version tag of a workflow

      restub           :  converts a full, unpublished workflow back to a stub

      ...

Command Parameters
------------------

For each command, you can see the command parameters available to it by typing ``dockstore <mode> <command>``. For example, to see the options available for launching a workflow locally with the CLI:

::

  $ dockstore workflow launch
  You can only use one of --local-entry and --entry at a time.

  ...

  Usage: dockstore workflow launch --help
         dockstore workflow launch [parameters] [command]

  Description:
    Launch an entry locally or remotely.

  Required parameters:
    --entry <entry>                     Complete workflow path in Dockstore (ex. NCI-GDC/gdc-dnaseq-cwl/GDC_DNASeq:master)
     OR
    --local-entry <local-entry>         Allows you to specify a full path to a local descriptor instead of an entry path


    --json <json file>                  Parameters to the entry in Dockstore, one map for one run, an array of maps for multiple runs
     OR
    --yaml <yaml file>                  Parameters to the entry in Dockstore, one map for one run, an array of maps for multiple runs (only for CWL)

  Optional parameters:
    --wdl-output-target                 Allows you to specify a remote path to provision output files to ex: s3://oicr.temp/testing-launcher/
    --uuid                              Allows you to specify a uuid for 3rd party notifications
    --ignore-checksums                  Allows you to ignore validating checksums of each downloaded descriptor


Commonly Executed Commands
--------------------------

The CLI has dozens of commands. Here are some that are documented more in depth:


- :doc:`Locally running WDL workflows <../../getting-started/getting-started-with-wdl>`
- :doc:`Locally running CWL workflows <../../getting-started/getting-started-with-cwl>`
- :doc:`Validating .dockstore.yml files <yaml-command-line-validator-tool>`
- :doc:`Setting up local file provisioning <set-up-file-provisioning-plugins>`
- :doc:`Running workflows remotely using the GA4GH WES API <../wes/cli-wes-tutorial>`

