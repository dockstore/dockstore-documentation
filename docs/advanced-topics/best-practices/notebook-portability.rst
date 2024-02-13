Notebook Portability
====================

Per the "Interoperable" and "Reusable" guidelines of the :ref:`dict FAIR` principles, Dockstore notebooks should run correctly in as many environments as possible.  To that end, we have the following recommendations for authors:

- **Prefer stable language constructs and time-tested features of core packages.**  A notebook with unusual code or software requirements is less likely to run everywhere.
- **Catalog software dependencies using requirements.txt or similar mechanisms.**  Many notebook environments will automatically read `requirements.txt` and install the software it specifies.
- **Access remote data via publically-accessible urls and standard protocols.**  If your notebook can always read the data it requires, it's more likely to run successfully.
- **Avoid using a custom kernel image, if possible.**  Some notebook environments, such as Google Colab, don't allow you to use a custom kernel image.

Google Colab
------------

At startup, most notebook environments copy all files from the repository to the environment and install the packages listed in `requirements.txt`.  However, some environments, most notably :doc:`Google Colab <../../launch-with/google-colab-launch-with>`, don't.

To ensure that after a notebook launches, it can access the repo file content and use the software packages listed in `requirements.txt`, even when running on Colab, a common pattern is to include a code cell at the top of the notebook that executes:

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

The above `iPython <https://ipython.org/>`_ code will copy the repo files into the current working directory, install the packages listed in `requirements.txt`, and have no effect if the files are already available and the packages have been previously installed.

GitHub Codespaces
-----------------

To launch a notebook to a GitHub Codespace, the repo must include a dev container file that specifies the path of the notebook file and to launch the Codespace notebook extensions.  See :doc:`Launch with GitHub Codespaces <../../launch-with/github-codespaces-launch-with>` page for more details.

Help Us
-------
Dockstore is actively researching ways to improve notebook portability.  Have an idea, feedback, or solution?  Please let us know via the "Discussion" link below!

