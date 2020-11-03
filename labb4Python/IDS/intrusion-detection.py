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

os.chdir('../')

FOLDER_TO_CHECK = os.getcwd()
CHECK_TIME = 40


last_entry = ids.get_last_entry(PATH_TO_DATABASE)
print(last_entry)

while True:
    dict1 = ids.hashing_files_in_folders(FOLDER_TO_CHECK)
    #fixa så att koden funkar när databasen är tom
    tempdict = ids.read_from_database(last_entry, PATH_TO_DATABASE)
    ids.write_to_database(dict1, datetime.now(), last_entry, PATH_TO_DATABASE)
    print(tempdict)
    #!compare dict1 with previous database entry

    sleep(CHECK_TIME)
