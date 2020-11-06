"""
fixme(1): create exclusion folders
fixme(): make the code work when very_secure_database is empty
"""

"""
DOCS:
hashing_files_in_folders(takes the folder u want check)
    Returns:
    a dictionary in the following format filenames:hash(md5)

write_to_database({filnames:hash}, Time, last_entry(file with the largest number))
    Returns: last_entry+1'


"""

import os
from time import sleep
import ids_functions as ids
from datetime import datetime

PATH_TO_DATABASE = os.path.join(os.getcwd(), 'very_secure_database')

os.chdir('../')

FOLDER_TO_CHECK = os.getcwd()
CHECK_TIME = 40


last_entry = ids.get_last_entry(PATH_TO_DATABASE)

while True:
    dict1 = ids.hashing_files_in_folders(FOLDER_TO_CHECK) # den kommer alltid vara samma
    ids.write_to_database(dict1, datetime.now(), last_entry, PATH_TO_DATABASE)
    dict2 = ids.read_from_database(last_entry, PATH_TO_DATABASE)
    #*fixme() compare_files compares the same dictionary
    ids.compare_files(dict1, dict2, last_entry)

    last_entry += 1
    sleep(CHECK_TIME)
