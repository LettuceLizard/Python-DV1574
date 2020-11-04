"""
fixme(1): add idenfication of evry entry so reading the database gets
easier

limitation(2): cant exit the program pga last entry gets saved in memmory. fixme() add
support for closing the program
"""
import os
import hashlib

def hashing_files_in_folders(folder):
    #Returns a dictionary with filename: binary hash of file
    hash_table = {}
    for dirname, dirpath, filenames in os.walk(folder):
        hash_algoritm = hashlib.md5() #vet nt om detta löser att programmet nt rensar föregående hash
        if filenames != []:
            for file in filenames:
                current_file_path = os.path.join(dirname, file)

                with open(current_file_path, "rb") as r_file:
                    f = r_file.read(8000) #how many bytes the program reads at once
                    while len(f) > 0:
                        hash_algoritm.update(f)
                        f = r_file.read(8000)

                        hash_table[file] = hash_algoritm.hexdigest()
    return hash_table

def get_last_entry(path):
    file_names = os.listdir(path=path)
    if file_names == []: return 0
    return max([int(e[0]) for e in file_names])


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
    #!get the largest lent(dict 1 or 2)
    #!for e in largest dict:
        #!do stuff
