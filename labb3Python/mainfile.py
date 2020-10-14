def generate_word_count(name_of_file):
    dict = {}
    with open(name_of_file, "r") as r_file:
        for line in r_file:
            striped_line = line.strip('\n').strip(",").strip(".")
            list_of_words = striped_line.split(" ")
            for word in list_of_words:
                if word == '': pass  #if empty
                elif word in dict.keys():
                    dict[word] += 1
                else:
                    dict[word] = 1
    return dict

def most_common_words(dict):
    print(sorted(dict, key=dict.get, reverse=True)[:10])

def main():
    dict = generate_word_count("text.txt")
    common = most_common_words(dict)


if __name__ == '__main__':
    main()
