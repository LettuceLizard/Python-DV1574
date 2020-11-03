"""
fixme(1): create exclusion folders
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

#run from the previous folder
os.chdir('../../')

FOLDER_TO_CHECK = os.getcwd()

#!get the last entry on each startup

while True:
    dict1 = ids.hashing_files_in_folders(FOLDER_TO_CHECK)
    last_entry = ids.temp_write_to_database(dict1, datetime.now(), last_entry, PATH_TO_DATABASE)

    sleep(10)
# last_entry = ids.write_to_database(dict1, str(datetime.now()), last_entry, PATH_TO_DATABASE) # not a loop last entry not working
