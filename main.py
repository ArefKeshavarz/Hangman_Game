import random

import Shapes
import Words

print("Hello user , welcome to Hangman game :) ")
words = Words.words
HANGMANPICS = Shapes.HANGMANPICS

number_of_wrong_answer = 0

# step 1 : choise a word :
word = random.choice(words)


# step 2 : generate a place for letters :
def build_place(word):
    places = ""
    for i in word:
        places += "_"
    return places


places = build_place(word)

# step 3 : ask letter from user and checking :
print(places)


def check_letter(letter, word, places, numebr_of_wrong_answer):
    if (letter in word):
        index_of_letter = word.index(letter)
        places = list(places)
        places[index_of_letter] = letter
        places = "".join(places)
        if (not ('_' in places)):
            print(places)
            print("----------------------------")
            print(">>> you win ... ")
            exit()
        else:
            return (places, numebr_of_wrong_answer)
    else:
        numebr_of_wrong_answer += 1
        print(HANGMANPICS[numebr_of_wrong_answer])
        if (numebr_of_wrong_answer == 6):
            print("------------------------------")
            print(">>> you lost ... ")
            exit()
        return (places, numebr_of_wrong_answer)


while number_of_wrong_answer <= 6:
    letter = input("please guess letter : ")
    places, number_of_wrong_answer = check_letter(letter, word, places, number_of_wrong_answer)
    print(f"{places}")

# -------------------------  finish  -------------------------
