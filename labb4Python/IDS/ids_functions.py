"""
fixme(1): add idenfication of evry entry so reading the database gets
easier

fixme(): add support for saving the date when the file is created

limitation: dont think the code works when there is no very_secure_database
folder

error(): the code has different hash values on files that has not been
changed
"""
import os
import hashlib

def hashing_files_in_folders(folder):
    #Returns a dictionary with filename: binary hash of file
    hash_table = {}
    for dirname, dirpath, filenames in os.walk(folder): #os.walk är en recursive funktion se os.walk documentationen
        hash_algoritm = hashlib.md5()
        if filenames != []:
            for file in filenames:
                current_file_path = os.path.join(dirname, file)
                with open(current_file_path, "rb") as r_file:
                    f = r_file.read(8000)
                    while len(f) > 0:
                        hash_algoritm.update(f)
                        f = r_file.read(8000)
                        hash_table[file] = hash_algoritm.hexdigest()
    return hash_table

def get_last_entry(path):
    file_names = os.listdir(path=path)
    if file_names == []: return 0
    return max([int(e.strip('.txt')) for e in file_names])


def write_to_database(dictionary, time, last_entry, path):
    filename = f"{str(last_entry+1)}.txt"
    with open(os.path.join(path, filename), 'w') as w_file:
        for k, v in dictionary.items():
            w_file.write(f"{k}:{v}\n")

def read_from_database(entry, path):
    dictionary = {}
    filename = str(entry) + '.txt'
    with open(os.path.join(path, filename), 'r') as r_file:
        for line in r_file:
            temp = line.strip('\n').split(':')
            dictionary[temp[0]] = temp[1]
    return dictionary

def compare_files(dict1, dict2, last_entry):
    shared_values = [k for k in dict1 if dict1.get(k) == dict2.get(k)]
    all_keys = list(dict1.keys()) + list(dict2.keys())
    unique_keys = list(set(all_keys))
    keys_to_check = [e for e in unique_keys if e not in shared_values]

    for element in keys_to_check:
        #!check if element was removed
        if element in dict2.keys() and element not in dict1.keys():
            print(f"the folowing element was REMOVED: {element}")
        #!check if element was added
        elif element not in dict2.keys() and element in dict1.keys():
            print(f"the folowing element was ADDED: {element}")
        elif dict1[element] != dict2[element]:
            print()
            print(dict1[element], dict2[element])
            print(f"the folowing element was CHANGED: {element}")
        else:
            print(f"ERROR WITH THE ELEMENT: {element}")
    print()
