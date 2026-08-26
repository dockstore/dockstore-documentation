Categories
==========

A :ref:`dict category` is a grouping of Dockstore entries (tools, workflows, and notebooks) that
share the same trait. Entries in a category might relate to the same scientific topic, perform the
same operation, or input/output the same type of data or format.

Dockstore places entries into categories to help users to better
understand the entries, find entries relevant to a particular area of interest,
and discover entries that are similar to those they already know about.

An entry can belong to any number of categories.

How Categories Are Displayed
-----------------------------

In the Dockstore UI, the categories that an entry belongs to are shown as small "bubbles" that are labelled with the category name.  These appear on entry's page,
and also in search results, where you can use the category-related search facets to filter results
by one or more particular categories, in the same way you would filter using any other :doc:`search facet <faceted-search>`.

AI and Dockstore-Curated Categories
-----------------------------------

Categories come from two sources:

* **AI-curated categories** are derived from the `EDAM <https://edamontology.org/>`__ ontology.  Dockstore populates these categories automatically, using an AI model to
  analyze each entry's name, description, and files, and classify the entry into the categories that
  it best matches.
* **Dockstore-curated categories** are created and populated by hand by a Dockstore curator. A
  curator defines the category and manually adds the entries that belong to it.

AI-curated category bubbles are shown with a grey tint to distinguish them from Dockstore-curated
ones. Hovering over a category bubble shows a tooltip that explains how the category was created
and how the entry was placed into it.

.. note::
    Dockstore's use of AI to curate categories follows our :ref:`approach to AI <what-is-dockstore-generative-ai-policy>`.
    Only already-public entry information is used, and entry owners can review and correct the AI's
    classifications, as described below.

EDAM and Our Extensions
------------------------

Dockstore derives its AI-curated categories from `EDAM <https://edamontology.org/>`__, a bioinformatics
ontology that organizes concepts by operation, topic, data type, and data format.  To improve coverage, Dockstore includes
additional AI-suggested categories not found in the original EDAM ontology.

The AI-curated categories are organized into six sets, each corresponding to a subontology of EDAM:

* **Operation**: operations an entry performs
* **Topic**: scientific subject or field an entry relates to
* **Input Format**: file formats an entry consumes
* **Input Data**: types of data an entry consumes
* **Output Format**: file formats an entry produces
* **Output Data**: types of data an entry produces

.. note::
    The "topic" category set is unrelated to an entry's :ref:`dict topic`, which is a short,
    free-text description of the entry set in :ref:`dict .dockstore.yml` or the Dockstore UI.

Entry Owners Can Curate the AI
------------------------------

Entry owners can review the AI categorizations of their own entries.  On an entry's private
page, click ``Manage Categories`` to view the entry's categories and approve or reject each AI-curated membership.
**Approving** confirms the membership and marks it as approved by the owner.
**Rejecting** permanently removes the entry from the category.

Dockstore-curated categories are managed exclusively by Dockstore curators. If you think
an entry should be added to (or removed from) a Dockstore-curated category, reach out to the
Dockstore team, for example via `Discourse <https://discuss.dockstore.org/>`__.

.. discourse::
    :topic_identifier: 12032
