Dockstore Yaml Command Line Validator Tool
==========================================

Description
-----------------

The Dockstore Yaml Command Line Validator Tool is used to verify that a :ref:`dict .dockstore.yml`
file is valid for use in Dockstore and that all referenced files are present.

The Dockstore Yaml Command Line Validator Tool is particularly helpful when you are trying to sync a GitHub repository with Dockstore
by adding a :ref:`dict .dockstore.yml` to the root or ``.github`` directory of the repository. As you can verify that :ref:`dict .dockstore.yml`
is valid before pushing, and it can help you to determine why your repository is not syncing with Dockstore.

The Dockstore Yaml Command Line Validator Tool will first determine if :ref:`dict .dockstore.yml`
is a valid yaml file and display the following if :ref:`dict .dockstore.yml` is a valtid yaml file
(but not necessarily valid for use in Dockstore),

::

  path/to/.dockstore.yml is a valid yaml file


If :ref:`dict .dockstore.yml` is not a valid yaml file the following
will be displayed along with an error message explaining why :ref:`dict .dockstore.yml` is not a valid yaml file,

::

  path/to/.dockstore.yml is not a valid yaml file



Next, the Dockstore Yaml Command Line Validator Tool will determine if :ref:`dict .dockstore.yml`
is valid for use in Dockstore, if it is it will display this message,

::

  path/to/.dockstore.yml is a valid dockstore yaml file and all required files are present
  
If :ref:`dict .dockstore.yml` is not a valid for use in Dockstore
the Dockstore Yaml Command Line Validator Tool will display a helpful error message, such as,

::

  Your file structure has the following errors:
  path/to/dockstore.cwl.json does not exist

or,

::

  path/to/.dockstore.yml has the following errors:
  Unknown property: 'primaryDescriptorath'. Did you mean: 'primaryDescriptorPath'?

Usage
-----------------

The Dockstore Yaml Command Line Validator Tool can be used with the following command in the :ref:`dict Dockstore CLI`,

::

  dockstore yaml validate --path directory/of/.dockstore.yml

Path Parameter
```````````````

The ``--path`` parameter must be set to the directory that contains :ref:`dict .dockstore.yml`, but must not include :ref:`dict .dockstore.yml`.
For example,

::

  path/to/my/awesome/workflow

is acceptable, however

::

  path/to/my/awesome/workflow/.dockstore.yml

is not acceptable.

The ``--path`` parameter can be either an absolute or relative directory. Therefore, the following are valid uses of the Dockstore Yaml Command Line Validator Tool,

::

  dockstore yaml validate --path .


::

  dockstore yaml validate --path directory/of/.dockstore.yml

::

  dockstore yaml validate --path ../../path/to/service

::

  dockstore yaml validate --path ~/path/to/workflow

::

  dockstore yaml validate --path /usr/jdoe/dockstore/workflow


Please note that all files referenced in :ref:`dict .dockstore.yml`,
are checked relative to the path parameter, unless the path parameter ends in ``.github``, in this case all files referenced in  :ref:`dict .dockstore.yml`
are checked relative to the parent of the path parameter.

For example if ``./my/awesome/workflow/.dockstore.yml`` contained the following,

::

  testParameterFiles:
    - /dockstore.wdl.json

and you selected ``./my/awesome/workflow`` as the path parameter, then the Dockstore Yaml Command Line Validator Tool would check that the file ``./my/awesome/workflow/dockstore.wdl.json`` exists.

However, if ``./my/fantastic/workflow/.github/.dockstore.yml`` contained the following,

::

  testParameterFiles:
    - /workflow.cwl

and you selected ``./my/fantastic/workflow/.github`` as the path parameter, then the Dockstore Yaml Command Line Validator Tool would check that the file ``./my/fantastic/workflow/workflow.cwl`` exists.

.. discourse::
    :topic_identifier: 5577