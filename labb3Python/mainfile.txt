def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
#-----------------------------------

FILE_NAME = "text.txt"

def generate_word_count(name_of_file):
    dictionary = {}
    with open(name_of_file, "r") as r_file:
        for line in r_file:
            striped_line = line.strip('\n').strip(",").strip(".")
            list_of_words = striped_line.split(" ")
            for word in list_of_words:
                if word == '': pass  #if empty
                elif word in dictionary.keys():
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    return dictionary

def word_stats(dictionary):
    antal_ord_i_texten = sum(dictionary.values())
    antal_unika_ord = sum([v for k, v in dictionary.items() if v == 1])
    return antal_ord_i_texten, antal_unika_ord

def most_common_words(dictionary):
    #sorted(dictionary.value, i fallande ordning)[:bara de 10 första i dictionaryn]
    return sorted(dictionary, key=dictionary.get, reverse=True)[:10]

def medelord_frekvensen(dictionary):
    #alla ord/många ord och vilka ord som uppstod så många gånger
    count_of_words = dictionary.values()
    average = round(sum(count_of_words)/len(count_of_words))
    return average, [k for k, v in dictionary.items() if v == average]

def medianord_frekvensen(dictionary):
    count_of_words = sorted(dictionary.values())
    medianen = count_of_words[round(len(count_of_words)/2)]
    return medianen, [k for k, v in dictionary.items() if v == medianen]

def ord_frekvensen(dictionary, antal_ord):
    antalet_upprepninga = sorted(dictionary.values(), reverse=True)[-1]
    percentage = round(antalet_upprepninga/antal_ord *100, 2)
    mest_upprepade_ord = [k for k, v in dictionary.items() if v == antalet_upprepninga][0]
    return mest_upprepade_ord, percentage

def generate_rapport(document_name, dictionary, ord_statistik, common_words, medelord, median, upprepning):
    rapport_name = document_name.replace(".txt", "") + "_rapport.txt"
    with open(rapport_name, 'w') as w_file:
        w_file.write(f"""
filen {FILE_NAME} inehåller {ord_statistik[0]} ord varav {ord_statistik[1]} är unika.

de vanligaste orden är:

ord           antal förekomster
----------------------------------
""")
        for word in common_words:
            w_file.write(f"{word}             {dictionary[word]}\n")
        w_file.write(f"""
---------------------------------------------------------------------------------------

medelord frekvensen är {medelord[0]}, och den frekvensen har följande ord:
""")
        for loop, word  in enumerate(medelord[1]):
            if loop % 7 == 0: w_file.write("\n")
            w_file.write(f"{word}    ")
        w_file.write(f"""
---------------------------------------------------------------------------------------

Medianordfrekvensen i texten är {median[0]}, och den frekvensen har följande ord:
""")
        for loop, word in enumerate(median[1]):
            if loop % 7 == 0: w_file.write("\n")
            w_file.write(f"{word}    ")
        w_file.write(f"""
---------------------------------------------------------------------------------------

det vanligaste ordet är "{upprepning[0]}" och det utgör {upprepning[1]}% av hela texten.
""")



def main():
    dictionary = generate_word_count(FILE_NAME)
    ord_statistik = word_stats(dictionary)
    common = most_common_words(dictionary)
    medelord = medelord_frekvensen(dictionary)
    median = medianord_frekvensen(dictionary)
    upprepning = ord_frekvensen(dictionary, ord_statistik[0])

    generate_rapport(FILE_NAME, dictionary, ord_statistik, common, medelord, median, upprepning)


if __name__ == '__main__':
    main()
