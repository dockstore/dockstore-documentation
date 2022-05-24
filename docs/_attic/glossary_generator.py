#  This script is run using `make glossary`, and generates glossary.rst
# (or whatever you set glossary_outfile to). 


from glossary_entries import *  # imports all the entries from glossary_entries.py as GlossEntry objects
from glossarpy.GreatGloss import GreatGloss
from glossarpy.GlossEntry import GlossEntry
import gc  # gc = garbage collector; we can use this to get instances of particular objects
import os  # used to delete old versions of glossary_outfile and glossary_outfile

glossary_outfile = "dictionary.rst"  # this one gets rendered
contents_outfile = "_attic/glossary_entries_list_dynamic.txt"  # does not get rendered, just for quick reference

try:
    os.remove(glossary_outfile)
    os.remove(contents_outfile)
except OSError:
    pass

dockstore_dictionary = GreatGloss("Dockstore Dictionary")
for glossary_object in gc.get_objects():
    if isinstance(glossary_object, GlossEntry):
        dockstore_dictionary.add_entry(glossary_object)
dockstore_dictionary.sort_entries()
dockstore_dictionary.write_toc(contents_outfile, format="txt", skipSource=False, sourcefile=__file__)
dockstore_dictionary.write_glossary(glossary_outfile, sourcefile=__file__)
