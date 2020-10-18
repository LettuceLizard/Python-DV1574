"""
fixme(1): create exclusion folders
"""

import ids_functions as ids
import os
import datetime

FOLDER = "/home/epic/Uppgifter/labb4Python"
EXCLUDE_FOLDERS = ['IDS'] #(1) Not working

last_entry = 0

os.chdir(FOLDER)

dict1 = ids.hashing_files_in_folders(FOLDER)
last_entry = ids.write_to_database(dict1, str(datetime.datetime.now()), last_entry) # not a loop last entry not working
