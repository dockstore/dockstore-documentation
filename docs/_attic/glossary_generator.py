# This script is run using `make glossary`, and generates glossary.rst


from glossary_entries import *  # imports all the entries from glossary_entries.py as GlossEntry objects
from glossarpy.GreatGloss import GreatGloss
from glossarpy.GlossEntry import GlossEntry
import gc  # gc = garbage collector; we can use this to get instances of particular objects

outfile = "glossary.rst"  # this one gets rendered
contents = "_attic/glossary_entries_list_dynamic.txt"  # does not get rendered, just for quick reference

dockstore_dictionary = GreatGloss("Dockstore Dictionary")
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        dockstore_dictionary.add_entry(glossary_object)
dockstore_dictionary.sort_entries()
dockstore_dictionary.write_toc(contents)
dockstore_dictionary.write_glossary(outfile)
