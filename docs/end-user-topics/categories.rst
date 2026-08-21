Categories
==========

A :ref:`dict categories` is a grouping of Dockstore entries (tools, workflows, and notebooks) that
share the same trait. Entries in a category might relate to the same scientific topic, perform the
same operation, or read/write the same type or format of data. Categories help users discover
entries that are similar to ones they already know about, and let you filter search results down to
entries relevant to a particular area of interest.

An entry can belong to any number of categories, and categories are shown as small labelled
"bubbles" wherever an entry is displayed.

Dockstore-Curated and AI-Curated Categories
--------------------------------------------

Categories come from two sources:

* **Dockstore-curated categories** are created and populated by hand by a Dockstore curator. A
  curator defines the category and manually adds the entries that belong to it.
* **AI-curated categories** are assigned automatically. Dockstore uses an in-house AI to analyze an
  entry's name, description, and files, and classify the entry into the categories it best matches.

AI-curated category bubbles are shown with a grey tint to distinguish them from Dockstore-curated
ones. Hovering over a category bubble shows a tooltip explaining how the category was created, and,
for AI-curated categories, how the entry was placed into it.

.. note::
    Dockstore's use of AI to curate categories follows our :ref:`what-is-dockstore-generative-ai-policy`.
    Only already-public entry information is used, and entry owners can review and correct the AI's
    classifications, as described below.

EDAM and Our Extensions
------------------------

The AI-curated categories are based on `EDAM <https://edamontology.org/>`__, a bioinformatics
ontology that organizes terms describing operations, data, formats, and topics. Dockstore bolsters
EDAM with additional categories, suggested by AI, for concepts that are not present in the ontology.

AI-curated categories are organized into six sets, corresponding to the branches of EDAM that
Dockstore draws on:

* **Operation** -- the analytical operation(s) an entry performs
* **Topic** -- the scientific topic or field an entry relates to
* **Input data** -- the type(s) of data an entry consumes
* **Input format** -- the file format(s) an entry consumes
* **Output data** -- the type(s) of data an entry produces
* **Output format** -- the file format(s) an entry produces

.. note::
    The "topic" category set is unrelated to an entry's :ref:`dict topic`, which is a short,
    free-text description of the entry set in :ref:`dict .dockstore.yml` or the Dockstore UI.

How Categories Are Displayed
-----------------------------

Categories that an entry belongs to are shown as bubbles on the entry's public page. They also
appear alongside entries in search results, where you can use the category facets to filter results
down to entries that belong to one or more particular categories, the same way you would filter by
any other :doc:`search facet <faceted-search>`.

How Entry Owners Can Curate Categories
----------------------------------------

Entry owners can review the AI's category assignments for their own entries. From an entry's private
page, click ``Manage Categories`` to see the categories the AI has proposed and approve or reject the
entry's membership in each one. Rejecting a category removes its bubble from the entry's public page
and search results; approving it confirms the assignment.

Dockstore-curated categories are managed by Dockstore curators rather than entry owners. If you think
an entry should be added to (or removed from) a Dockstore-curated category, reach out to the
Dockstore team, for example via `Discourse <https://discuss.dockstore.org/>`__.
