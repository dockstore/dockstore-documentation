When setting the value of a field that accepts a ``<String Array>``, be sure to format the list of values in YAML format.  For example, if you are setting the ``testParameterFiles`` field, you can use either the "one per line" YAML array format:

::

  testParameterFiles:
    - /path/to/test.json

or the "compact" YAML array format:

::

  testParameterFiles: [ /path/to/test.json ]
