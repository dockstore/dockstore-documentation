Creating Snapshots and Requesting DOIs
=============================================

Introduction
------------------
Starting in Dockstore 1.7.0, users can create snapshots and Digital
Object Identifiers (DOIs) for their workflows. The ‘Snapshot’ and
‘Request DOI’ actions can be found on the versions tab of any published
workflow on the ‘My Workflows’ page. These features are specific to
individual versions of a workflow entry.

.. image:: /assets/images/docs/snapshot_doi/snapshot_doi_versiontab.png



Connect Zenodo Account
----------------------
A Zenodo account is required to issue a DOI to a workflow version.
You can link your account with your Zenodo credentials on the
`accounts page <https://dockstore.org/accounts?tab=accounts>`__.

.. image:: /assets/images/docs/snapshot_doi/link_zenodo.png


Create Snapshot
----------------
A snapshot is a point-in-time capture of the descriptor(s), test parameter file(s),
and metadata associated with a workflow version. Snapshotting a version will also
make the version immutable. Users will be prompted to confirm before generating a snapshot.
**Taking a snapshot cannot be undone**.