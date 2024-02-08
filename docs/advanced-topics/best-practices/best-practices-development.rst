Workflow and Tool Development Process Best Practices
====================================================

Overview
--------

This page discusses some best practices in software engineering, and how you can incorporate them into workflow and tool development.

Although the use of software engineering practices in the bioinformatics world is improving, the Dockstore team has noticed that many common best practices, such as automated builds, are not always used in workflow and tool development. This document discusses some ideas and has real-world examples of best practices in bioinformatics.

This is not a complete guide to workflow and tool development, but rather an overview of some concepts to give developers some ideas for features they can incorporate into their development processes. Once you have an automated framework in place, you can keep building on it, adding new features, more tests, etc.

.. note::

   For simplicity's sake, for the rest of this page we'll just use the term *workflow*, instead of saying *workflow and tool*, but all comments apply equally to both tools and workflows.

Automated Builds
----------------

Automated builds are just that -- builds that trigger automatically. They can trigger on a schedule (daily, weekly, etc.), by pushes to a branch, by the creation of a pull request or tag, etc.

The advantage of automated builds is that they catch errors right away, before a workflow user spends time and money running the faulty workflow. You can also use automated builds to do security scanning, and if you have a more complex system, package up your builds. 

It's easy to introduce an error to your workflow, from something as simple as missing a closing quotation mark to a logic error in the middle of the program. Automated builds can quickly catch such problems.


Build Servers
`````````````

There are lots of options for doing automated builds. You can search the web for "Continuous Integration" and get lots of results. As a starting point, here are some services the Dockstore team has used:

- `GitHub Actions <https://docs.github.com/en/actions>`__
- `CircleCI <https://circle.com>`__
- `Travis CI <https://www.travis-ci.com>`__
- `Jenkins <https://www.jenkins.io>`__

GitHub Actions, CircleCI and Travis CI are generally cloud services; Jenkins is typically a server you set up in your own infrastructure.

Validation
``````````

Validation tools work by statically analyzing your code. That is, they don't run the code, they inspect it by analyzing the source code.

As a minimum, you should verify that your workflow is syntactically correct. Depending on the language, you will have different tools at your disposal. For example, for WDL you could use `WOMTool <https://cromwell.readthedocs.io/en/stable/WOMtool>`__ and/or `miniWDL <https://miniwdl.readthedocs.io/>`__. 

These tools can not only catch syntax errors, but can also do semantic checking and linting. Semantic checking does things like ensuring you initialize a variable before use. Linting can ensure there are patterns that improve your code's readability, e.g., the line length doesn't exceed a certain number, indentation is consistent, etc.

.. note::

   Dockstore validates your workflows for syntactical correctness. It shows the validation results in the UI, and prevents users from doing certain operations if a version is invalid, e.g., Dockstore disables the `Launch with` buttons for invalid versions. But ideally you should catch errors before pushing your version to Dockstore.

Tests
`````

Automated testing greatly improves software development. If set up correctly, it lets you make changes to your workflows with confidence that you're not breaking anything. You can also introduce new features that have been tested in advance. While it's unlikely you can verify everything, your tests can grow over time to cover more and more.

Security
--------

You can scan your workflows for vulnerabilities using automated tools. To our knowledge, there are no tools available for workflow languages, but there are tools that scan Docker images. Some Docker repositories, such as quay.io. have image scans.

Flattening and Packing
``````````````````````

Some languages offer tools that package your workflows into a single file. For example, `cwltool <https://github.com/common-workflow-language/cwltool>`__ offers a `--pack` option to combine all of a CWL workflow's files into one single file. This makes it easier to distribute your workflow, and enables your workflow to run on platforms that do not support imports.

Sharing Code
------------

Workflow languages do not typically make it easy to share dependencies like other languages do (Maven in Java, PyPI in Python, etc.). One common technique is to have one Git repository with multiple workflows, with all the workflows referencing common code in the same repository, using relative paths. You can then publish multiple workflows from the single repository, or push the individual workflows to different repositories. For an example of the latter, see the Galaxy IWC use case below.

Another technique is to `import code using https urls <https://github.com/aofarrel/myco/blob/469620a1c8ecda44ae843985f6d640e9ca24d028/myco_sra.wdl#L3>`__. This can work, but does get difficult to manage as you'll need to update multiple repositories if a change is made in common code.


Use Cases
---------

Following are a couple of real world examples of workflows published on Dockstore, that use some of the techniques described above.

Galaxy's IWC
````````````

The Galaxy Intergalactic Workflow Commission (IWC) creates workflows for Galaxy. They have one `repository <https://github.com/galaxyproject/iwc>`__, which contains multiple workflows, and then a build system that creates individual workflows and pushes them to different GitHub repositories, one workflow per repository, such as an `Illumina variant caller <https://github.com/iwc-workflows/sars-cov-2-pe-illumina-artic-variant-calling>`__ and an `assembler <https://github.com/iwc-workflows/Assembly-Hifi-Trio-phasing-VGP5>`__. Only the repositories with individual workflows are published to Dockstore.

The automated builds are done with GitHub Actions. Here are some interesting things they are doing:

- `Lints <https://github.com/galaxyproject/iwc/blob/0a87074432faeb78c39870cf61b33656e2c217c9/.github/workflows/ci.yaml#L79>`__ the workflows
- `Runs tests weekly <https://github.com/galaxyproject/iwc/blob/0a87074432faeb78c39870cf61b33656e2c217c9/.github/workflows/ci.yaml#L109>`__

Broad Institute's Viral Pipelines
`````````````````````````````````

Unlike the Galaxy IWC example, the `Viral Pipelines <https://github.com/broadinstitute/viral-pipelines>`__ publishes all of its workflows from that single repository. All the different workflows are listed in their `dockstore.yml <https://github.com/broadinstitute/viral-pipelines/blob/52b297c93c395a193446cf331673935e5042f322/.dockstore.yml#L1>`__. The automated builds are done with GitHub Actions. Some of the interesting things:

- Validates with both `Cromwell <https://github.com/broadinstitute/viral-pipelines/blob/52b297c93c395a193446cf331673935e5042f322/.github/workflows/build.yml#L87>`__ and `miniWDL <https://github.com/broadinstitute/viral-pipelines/blob/52b297c93c395a193446cf331673935e5042f322/.github/workflows/build.yml#L34>`__.
- `Tests the documentation generation <https://github.com/broadinstitute/viral-pipelines/blob/52b297c93c395a193446cf331673935e5042f322/.github/workflows/build.yml#L137>`__ works correctly. The generated doc is `here <https://viral-pipelines.readthedocs.io/en/latest/workflows.html>`__.


