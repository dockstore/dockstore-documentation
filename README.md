# Dockstore Documentation

Dockstore is using [Read the Docs](https://readthedocs.org/) for documentation! Please take a look at [our style guide](./style-guide.md) to learn about our approach to documentation.

Below are some tips for setting up the documentation locally and updating the code.

## Setting up locally

Install pip dependencies (Requires Python 3.9+)
`pip install -r requirements.txt`

Go to the docs directory
`cd docs`

Generate the HTML to generate HTML pages in a new folder called `_build`
`make html`

Check for broken links
`make linkcheck`

Open the `_build/html/index.html` in your browser!

OICR partners can view additional developer docs here: https://wiki.oicr.on.ca/display/DOC/Read+The+Docs

## Writing/Maintaining docs
Most of our docs are written in RST. A handful are written are in markdown. Both the RST and markdown documents will be rendered as HTML using the Python-based documentation manager Sphinx.

Most of our docs can be maintained by modifying individual RST and MD files directly. There are a few exceptions:
* When creating a new page, it must exist on the table of contents (`toctree`) which forms the sidebar on the left — in most cases this requires adding a new entry to index.rst
* dictionary.rst is generated from entries in `docs/_attic/glossary_entries.py` by `docs/_attic/glossary_generator.py` in order to easily handle the complexities of large RST documents — dictionary.rst is regenerated upon every `make` command (changes will not appear in git unless `docs/_attic/glossary_entries.py` is modified), but this regeneration can also be called explictly with `make glossary`
* Certain doi.org links, plus any images that link to internal documents, must have those links added to `linkcheck_ignore` in conf.py
