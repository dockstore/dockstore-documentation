DOIs
====

Introduction
------------
A Digial Object Identifier (DOI) is a permanent identifier that can be used in publications to identify the exact
version of a workflow or tool (entry). DOIs are commonly referenced from academic papers.
See the `DOI Foundation <https://www.doi.org>`__ for more details.

For an entry, you will typically have a concept DOI, which is a DOI referencing the entire entry, and many version DOIs -- one DOI per version, that is linked to the concept DOI. If you navigate to the concept DOI,
you will typically be directed to the most recent version DOI.

Dockstore Support for DOIs
--------------------------

Dockstore can generate DOIs for entries, as well as recognize some DOIs generated outside of Dockstore. Dockstore displays DOIs associated with entries. If you have multiple DOIs associated
with a single entry, the entry owner can specify which DOI they want displayed.

Dockstore can generate DOIs for entries 2 ways:

* Explicitly initiated by a Dockstore user. This approach requires you linking your Zenodo account, and Dockstore will then issue a DOI on your behalf. See :doc:`Creating Snapshots & Requesting DOIs </advanced-topics/snapshot-and-doi>` for more details.
* Dockstore can automatically generate DOIs for your entries without the owner needed to link their Zenodo account. These DOIs are created in the Dockstore Zenodo Community.

In addition, Dockstore can discover DOIs created by a Zenodo-GitHub integration.


Choosing which DOI to display
-----------------------------

An entry can have up to 3 DOIs associated with it.

Comparison of the different ways of issuing DOIs
------------------------------------------------

With the different ways Dockstore supports DOIs, it may be confusing as to how to generate DOIs for your Dockstore entries. Here's a high level overview of some of the differences. Each section has a page with more details; this is a high level overview.


Creating Snapshots & Requesting DOIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These DOIs are initiated by entry owners. The entry owner has to explicitly initiate the process, either via the Dockstore UI or the Dockstore API. If issuing a DOI this way, you first need to `snapshot` your version.
Snapshotting a version makes it immutable, so that no further modifications to the version are allowed by Dockstore.

This approach requires you to have a Zenodo account and link it in Dockstore.


* You must initiate the DOI creation
    * More control over when DOIs are created
    * More cumbersome, you have to individually do it for every tag
* Version on Dockstore is snapshotted, which means it will ignore any future changes made on GitHub.
* Requires a Zenodo account, and that you link your account to Dockstore.
* Some confusion can occur if tags are renamed.

Automatic DOI Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Note: This feature is currently only available on request. Please contact the Dockstore team at `discuss.dockstore.org <https://discuss.dockstore.org/t/opening-helpdesk-tickets/1506>`__ if you want to participate.

With this approach, Dockstore automatically generates a DOI for GitHub based entries, every time a Git tag is pushed to GitHub. This DOI will be published as part of the Dockstore community.
You do not even need a Zenodo account for this DOI to be created. If you want to make changes to the DOI, you will need a Zenodo account.

* It's automatic. You will have the option to turn it off for specific workflows.
* Happens for both tags that aren't releases as well as tags that are releases.
* Some confusion can occur if tags are renamed.

GitHub-Zenodo Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Zenodo has a feature where you can link your GitHub account, then for specified repositories, you can have Zenodo automatically generate DOIs when GitHub releases are created. Note that a GitHub release is not the
same as a Git tag; GitHub releases require Git tags, but have extra features.

The DOIs created by this integration follow a certain pattern. Dockstore will poll Zenodo GitHub daily to see if any new DOIs have been created by Zenodo.

* It's automatic
* Only works with GitHub releases
