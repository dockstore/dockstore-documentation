Yaml Command Line Validator Tool
================================

Description
-----------------

The Yaml Command Line Validator Tool is used to verify that a `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_ 
file is valid for use in Dockstore and that all referenced files are present.

The Yaml Command Line Validator Tool will first determine if `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_ 
is a valid yaml file and display the following if `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_ is a valid yaml file
(but not necessarily valid for use in Dockstore),

::

  path/to/.dockstore.yml is a valid yaml file


If `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_ is not a valid yaml file the following
will be displayed along with an error message explaining why `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_ is not a valid yaml file,

::

  path/to/.dockstore.yml is not a valid yaml file



Next, the Yaml Command Line Validator Tool will determine if `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_
is valid for use in Dockstore, if it is it will display this message,

::

  path/to/.dockstore.yml is a valid dockstore yaml file and all required files are present
  
If `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_ is not a valid for use in Dockstore
the Yaml Command Line Validator Tool will display a helpful error message, such as,

::

  Your file structure has the following errors:
  path/to/dockstore.cwl.json does not exist

or,

::

  path/to/.dockstore.yml has the following errors:
  Unknown property: 'primaryDescriptorath'. Did you mean: 'primaryDescriptorPath'?

Usage
-----------------

The Yaml Command Line Validator Tool can be used with the following command in the `Dockstore CLI <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-cli>`_,

::

  dockstore yaml validate --path directory/of/.dockstore.yml

**Path Parameter**

The ``--path`` parameter must be set to the directory that contains `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_, but must not include `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_.
For example,

::

  path/to/my/awesome/workflow

is acceptable, however

::

  path/to/my/awesome/workflow/.dockstore.yml

is not acceptable.

The ``--path`` parameter can be either an absolute or relative directory. Therefore, the following are valid uses of the Yaml Command Line Validator Tool,

::

  dockstore yaml validate --path directory/of/.dockstore.yml

::

  dockstore yaml validate --path ../../path/to/service

::

  dockstore yaml validate --path .

::

  dockstore yaml validate --path ~/path/to/workflow

::

  dockstore yaml validate --path /usr/jdoe/dockstore/workflow


Please note that all files referenced in `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_,
are checked relative to the path parameter, unless the path parameter ends in ``.github``, in this case all files referenced in  `.dockstore.yml <https://docs.dockstore.org/en/stable/dictionary.html?highlight=.dockstore.yml#dict-dockstore-yml>`_
are checked relative to the parent of the path parameter.

For example if ``./my/awesome/workflow/.dockstore.yml`` contained the following,

::

  testParameterFiles:
    - /dockstore.wdl.json

and you selected ``./my/awesome/workflow`` as the path parameter, then the Yaml Command Line Validator Tool would check that the file ``./my/awesome/workflow/dockstore.wdl.json`` exists.

However, if ``./my/fantastic/workflow/.github/.dockstore.yml`` contained the following,

::

  testParameterFiles:
    - /workflow.cwl

and you selected ``./my/fantastic/workflow/.github`` as the path parameter, then the Yaml Command Line Validator Tool would check that the file ``./my/fantastic/workflow/workflow.cwl`` exists.

.. discourse::
    :topic_identifier: 5577