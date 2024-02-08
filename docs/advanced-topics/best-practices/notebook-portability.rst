Notebook Portability
====================

Per the "Interoperable" and "Reusable" tenets of the :ref:`dict FAIR` principles, Dockstore notebooks should run correctly in as many environments as possible.  To that end, we have the following recommendations for authors:

- **Use stable language constructs and time-tested features of core packages.**  A notebook with unusual code or software requirements is less likely to run everywhere.
- **Catalog software dependencies using requirements.txt or similar mechanisms.**  Many notebook environments will automatically read `requirements.txt` and install the software it specifies.
- **Access remote data via publically-accessible urls and stable protocols.**  If your notebook can always read the data it requires, it's more likely to run successfully.
- **Avoid using a custom kernel image, if possible.**  Some notebook environments, such as Google Colab, don't allow you to use a custom kernel image.

Google Colab
------------

At startup, most notebook environments copy all files from the repository to the environment and install the packages listed in `requirements.txt`.  However, some environments, most notably :doc:`Google Colab <../../launch-with/google-colab-launch-with>`, don't.

To ensure that after a notebook launches, it has access to the repo files and/or can read and install the software packages listed in `requirements.txt`, even when running on Colab, a common pattern is to add a code cell at the top of the notebook that executes:

- `git clone` to copy the source GitHub repo's files into the notebook environment.
- `pip install` to install the packages listed in `requirements.txt`.

For example:

.. code:: sh

    %mkdir -p /tmp/repo
    %pushd /tmp/repo
    !git clone https://github.com/svonworl/simple-notebook /tmp/repo
    !git checkout main
    !pip install -r requirements.txt
    %popd
    %cp -rn /tmp/repo/* .

GitHub Codespaces
-----------------

To launch a notebook to a GitHub Codespace, the repo must include a dev container file that specifies the path of the notebook file and to launch the Codespace notebook extensions.  See :doc:`"Launch with GitHub Codespaces" <../../launch-with/github-codespaces-launch-with>` page for more details.

Help Us!
--------
Dockstore is researching ways to improve notebook portability.  Have an idea or solution?  Please `let us know! <https://github.com/dockstore/dockstore/issues/new/choose>`_

