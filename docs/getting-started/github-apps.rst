Dockstore GitHub App
====================

.. note::
    The Dockstore GitHub App is currently only used for Dockstore
    Services, which are in beta mode. Usage of Dockstore GitHub App will be
    expanded in future releases to encompass workflows and tools, so the concepts
    here will eventually apply to all Dockstore entities.


Overview
--------

This document gives a high level overview of the GitHub Apps and the Dockstore
GitHub App in particular. For details on configuring and using the Dockstore
GitHub App with services, please walk through the
`Getting Started with Services <../getting-started/getting-started-with-services>`_ tutorial.

With the Dockstore GitHub App, authors do not need to manually refresh their
services on Dockstore to get the latest changes from GitHub. Dockstore will
automatically update whenever the service is updated on GitHub.

GitHub Apps
-----------

`GitHub apps <https://developer.github.com/apps>`_ are a GitHub feature used to
improve the interaction between external applications and GitHub. Users can
grant a GitHub app specific permissions on the repos and/or
organizations of their choosing. When events occur on the GitHub repos, e.g.,
creating a new release, the GitHub App issues notifications.

Why have a Dockstore GitHub App?
--------------------------------

Without a GitHub App, Dockstore does not know when you have modified a GitHub
repository.

For example, take the case when you first add a tool or workflow to Dockstore
from GitHub.  Dockstore indexes the repository -- it reads the the relevant
repository content, branches, and releases from GitHub. When you subsequently
make changes to your GitHub repo, such as push new commits, create new branches
and/or publish new releases, Dockstore is unaware of those changes. You are
responsible for going to Dockstore, finding the tool/workflow that corresponds
to the GitHub repo, and manually refreshing the tool/workflow by either clicking
the Refresh button or making an API call to the Dockstore API.

Due to the manual nature of this process, it is easy for Dockstore to get out of
sync with the linked GitHub repository.

How the Dockstore GitHub App works
----------------------------------

With the Dockstore GitHub App, the synchronization is done automatically. When
you publish a new release of a service on GitHub, Dockstore is notified,
and Dockstore updates its copy of the service. After you publish a new release
of a service on GitHub, a new version of the service will be present in
Dockstore shortly afterwards.

See Also
--------

- `Getting Started with Services <../getting-started/getting-started-with-services>`_
