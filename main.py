import random

print("Hello user , welcome to Hangman game :) ")
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
# step 1 : choise a word :
word = random.choice(words)


# step 2 : generate a place for letters :
def build_place(word):
    places = ""
    for i in range(0, len(word)):
        places += "_"
    return places


places = build_place(word)
