When setting a field that accepts a ``<String Array>``, be sure to specify the list of strings in YAML format.  For example, to set the ``testParameterFiles`` field, you can use either the "one per line" YAML array format:

::

  testParameterFiles:
    - /path/to/test.json

or the "compact" YAML array format:

::

  testParameterFiles: [ /path/to/test.json ]
