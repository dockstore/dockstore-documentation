# WDL Training
This tutorial will provide you with an introduction to [WDL](https://openwdl.org/). WDL stands for Workflow Description Language. It is a language for creating complex workflows that can be run locally or in a cloud environment.

## Exercise 1
The Dockstore CLI can be used to run WDL workflows, among other things. Here we will use it to run a Hello World workflow.

### Part A - Run your first WDL
Our first WDL will be a simple hello world workflow. It will print a welcome message based on an input file and store it to a file. The file exists as HelloWorld.wdl.

Parameter files can be passed along when running a workflow to provide additional information. This allows the same workflow to be run on different inputs. See hello.json to see the format of the parameter file.

Now lets launch the workflow using the Dockstore CLI.
```shell
$ dockstore workflow launch --local-entry HelloWorld.wdl --json hello.json
```

### Part B - Explore the Dockstore CLI (Take home exercise)
The Dockstore CLI can do a lot more than just run workflows. One neat feature is that it can be used to generate a template parameter file for a workflow. This template can be filled in and used during a run of a workflow, like we saw with hello.json in the previous part.
```shell
$ dockstore workflow convert wdl2json --wdl HelloWorkflow.wdl > parameter.json
```

Take a look at the parameter.json file. It is a JSON file that contains parameters that must be filled in to run the workflow. In this example there is just the one parameter, which is a file parameter called myName.

A typical scenario is running the above command to create the parameter JSON, filling it in, and then calling the workflow run command.

## Exercise 2 - Set runtime and parameterize variables
This exercise will have you setting the Docker image for a task using a parameter file.

## Exercise 3 - Use imports in a multi-task workflow
This exercise will have you creating a workflow that imports tasks from other files.