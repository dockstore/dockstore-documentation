Workflow Development Process Best Practices
===========================================

Overview
--------

This document discusses some best practices in software development, and how you might incorporate them into workflow and tool development.

Although software engineering practices in the bioinformatics world are improving, the Dockstore team feels that common software engineering practices, such as Automated Builds, are not commonly used. This document discusses some ideas and real-world examples of good software engineering practices.

It is not intended to be a complete guide to workflow and tool development, but rather an overview of some concepts to give workflow and tool developers some ideas for features they incorporate into their development process. Once you have an automated framework in place, you can keep building on it, adding new features, more tests, etc.

.. note::

   For simplicity's sake, for the rest of this document we'll just use the term *workflow*, instead of saying *tool and workflow*, but all comments apply equally to both tools and workflows.

Automated Builds
----------------

Automated builds are just that -- builds that trigger automatically. They can by triggered on a schedule, on pushes to a branch, on the create of a pull request or tag, etc. The advantage of automated builds is that they can catch errors right away, instead of users of the workflows running into them. You can also use automated builds to do security scanning, and if you have a more complex system, package up your builds.


It's easy to introduce an error to your workflow, from something as simple as forgetting a closing quotation mark to some logic error in the middle of the program. Having automated builds can quickly catch any such problems early, before the workflow is even used.

Build Servers
`````````````

There are lots of options for doing automated builds. You can search the web for "Continuous Integration" and get lots of results. Here is a non-exhaustive list of some options:

- `GitHub Actions <https://docs.github.com/en/actions>`__
- `CircleCI <https://circle.com>`__
- `Travis CI <https://www.travis-ci.com>`__
- `Jenkins <https://www.jenkins.io>`__

GitHub Actions, CircleCI and Travis CI are cloud services; Jenkins is typically a server you set up in your own infrastructure.

Validation
``````````

As a minimum, you should verify that your workflow is syntactically correct. Depending on the language, you will have different tools at your disposal. For example, for WDL you could use `WOMTool <https://cromwell.readthedocs.io/en/stable/WOMtool>`__ and/or `miniWDL <https://miniwdl.readthedocs.io/>`__. These tools will not only catch syntax errors, but can also do semantic checking.

Tests
`````



Security
--------

You can scan your workflows for vulnerabilities using tools like Snyk and

Flattening and Packing
``````````````````````

Sharing Code
------------

Workflow languages do not necessarily make it easy to share code, unlike other languages --- Java has Maven, Python has PyPi, JavaScript has NPM, etc.


Use Cases
---------

Following are a couple of real world examples of high quality workflows that get published on Dockstore, using some of the techinques described above.

Galaxy's IWC
````````````

The Galaxy Intergalactic Workflow Commission has high quality workflows for Galaxy. They have one `repository <https://github.com/galaxyproject/iwc>`__, which contains all of their workflows, and then a build system that creates individual workflows and pushes them to different GitHub repositories, one workflow per repository, such as `this <https://github.com/iwc-workflows/sars-cov-2-pe-illumina-artic-variant-calling>`__ and `this <https://github.com/iwc-workflows/Assembly-Hifi-Trio-phasing-VGP5>`__.

The automated builds are done with GitHub Actions.


Broad Institute's Viral Pipelines
`````````````````````````````````

The automated builds are done with GitHub Actions. Some of the interesting things:

- Generate documentation
- Validate with both Cromwell and miniWDL

https://github.com/broadinstitute/viral-pipelines
