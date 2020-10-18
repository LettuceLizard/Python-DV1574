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
    hash_algoritm = hashlib.md5()
    hash_table = {}
    for dirname, dirpath, filenames in os.walk(folder):
        if filenames != []:
            for file in filenames:
                current_file_path = os.path.join(dirname, file)

                with open(current_file_path, "rb") as r_file:
                    f = r_file.read(8000) #how many bytes the program reads at once
                    while len(f) > 0:
                        hash_algoritm.update(f)
                        f = r_file.read(8000)

                        hash_table[file] = hash_algoritm.hexdigest()
            hash_algoritm = hashlib.md5() #vet nt om detta löser att programmet nt rensar föregående hash
    return hash_table



def write_to_database(dictionary, time, last_entry): #2
    with open("IDS/very_secure_database.txt", "a") as a_file:
        a_file.write(f"Entry: {last_entry+1} | Time: {time} \n")
        for k, v in dictionary.items():
            a_file.write(f"{k}: {v}\n")
        a_file.write("-------------------------------------")
    return last_entry+1

def read_from_database(only_last_entry=True):
    if only_last_entry:
        pass
