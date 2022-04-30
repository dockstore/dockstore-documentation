# Dockstore Documentation

Dockstore is using [Read the Docs](https://readthedocs.org/) for documentation! Please take a look at [our style guide](./style-guide.md) to learn about our approach to documentation.

Below are some tips for setting up the documentation locally and updating the code.

## Setting up locally

Install pip dependencies (Requires Python)
`pip install -r requirements.txt`

Go to the docs directory
`cd docs`

Generate the HTML
`make html`

Check for broken links
`make linkcheck`

Open the _build/html/index.html in your browser!

Developer Docs: https://wiki.oicr.on.ca/display/DOC/Read+The+Docs 
