Overhauling Dockstore Tools
===========================

This documentation explains:

* How Dockstore tools worked historically before the 1.12 release
* How tools registered with GitHub Apps work differently
* How Dockstore envisions future support for tools


Dockstore Tools Prior to 1.12
-----------------------------

In a very broad sense, we defined a tool on Dockstore as a CWL or WDL program that performs a single task in a unique Docker container. Dockstore tool versions were based on the Docker image's tags and we required
that the image be owned by the Dockstore user. However, working on GitHub App registration for tools caused a lot of internal discussion because we realized that Dockstore tool support was confusing.

For starters, we created distinctions between tools and workflows even when one did not exist in one language's specification.
When Dockstore was created, CWL was the first descriptor language we supported. CWL does have a very clear distinction between a tool and a workflow and we followed it.
WDL was the next language Dockstore supported, but it does not have separate concepts for tools and workflows. At the time, we decided to create our own definition;
we defined WDL tools as a WDL descriptor file that contained a single task and a WDL workflow as one that had more than one task.

Secondly, the requirement that the Docker image tied to the Dockstore tool must be owned by the user is problematic for three different reasons:

#. Neither CWL or WDL require that a Docker image be specified (although using one is best practice)
#. If you do specify a Docker image, it is not necessary that it be one you created or owned. It is perfectly valid to use someone else's Docker image.
#. Even when an image was specified the user, Dockstore did not enforce that the image registered was actuall the one referenced in the descriptor file.


GitHub App Tools
----------------

In the 1.12 release, Dockstore introduced a new registration path for tools via GitHub Apps. We introduced this feature for two main reasons:

#. Allow Dockstore tools to be automatically synced with the work that has been pushed to GitHub and
#. Let users register a tool without needing to specify a Docker image that the user owned

But, we also saw this feature as an opportunity to start eliminating some of the confusion surrounding Dockstore tools. GitHub App tools will:

* Be the recommended way of registering tools
* Not support WDL
* Have versioning based on the versioning on GitHub


Future of Dockstore Tools
-------------------------

Dockstore wants to continue simplifying and automating the registration process for tools. Eventually we want to:

* Completely eliminate WDL tools and only support WDL workflows in order to match the language specification
* Deprecate the other tool registration methods (traditional tools)
* Continue to display already published tools that were created using the traditional registration methods


