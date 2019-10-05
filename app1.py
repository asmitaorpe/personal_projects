import json
from difflib import get_close_matches

data = json.load(open("data.json"))
all_keys = data.keys()


def the_word():
    word = input("Enter the word: ")
    while word == 'EndDict':
        print("Bye")
        break
    else:
        word = word.lower()                                     # takes care of random upper and lower letters

        if word in data:
            return_meaning(word)
        else:
            word_list = get_close_matches(word, all_keys, 3, 0.8)
            if word_list:
                word1 = word_list[0]
                print("did you mean {}?".format(word1))
                w = input("if yes press y else n: ")
                if w == 'y':
                    return_meaning(word1)
                else:
                    print('Please check the word and enter again!')
                    the_word()  # prompt again for input
            else:
                print('Please check the word and enter again!')
                the_word()  # prompt again for input


def return_meaning(word):
    meaning = data[word]
    print(meaning)
    the_word()


if __name__ == '__main__':
    the_word()