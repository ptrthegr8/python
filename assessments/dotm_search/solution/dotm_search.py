# Python program to iterate through all files in a directory.
# Find out which files have an embedded '$' character within the content of each file.
# The files are all Microsoft word template docs of type .dotm

import os
import pprint
import zipfile

# TODO Make these command line args
doc_path = 'C:\\users\\amadar\\Documents\\L3'

file_list = os.listdir(doc_path)
pp = pprint.PrettyPrinter(indent=4, width=120)
# pp.pprint(file_list)
DOC_FILENAME = 'word/document.xml'
MAGIC = b' $'

# Iterate over each file
for file in file_list:
    # Construct the full file path
    full_path = os.path.join(doc_path, file)
    # print('----- Examining file ', full_path)
    if zipfile.is_zipfile(full_path):
        with zipfile.ZipFile(full_path) as z:
            # what are the contents of this zipfile?
            names = z.namelist()
            # we are interested in the specific archive doc named 'word/document.xml' 'r'=ReadOnly
            if DOC_FILENAME in names:
               # print('...... Found an archived xml file named', )
                with z.open(DOC_FILENAME, 'r') as doc:
                    # read the xml contents line by line, looking for our magic character string
                    for line in doc:
                        if MAGIC in line:
                            print('Found Magic sequence in file {}'.format(full_path))
                            # pp.pprint(line)

# We are done.