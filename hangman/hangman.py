import random
from words import words
import string

#print(words)

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    # This loop iterator in the list to find the word with no the - character or the space
    while '-' in word or ' ' in word: 
        word = random.choice(words)

    return word


def hangman():

    word = get_valid_word(words)
    word_letters = set(word) # This will be keeping track of the words which have been gussed
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # We will use this set to keep track of what the user has guess

    lives = 6

    while len(word_letters) > 0 and lives > 0:    
        # letter used
        # ' '.join(['a', 'b', 'cd']) ---> 'a b c d'
        print("You have", lives, "lives left and you hava used these letters: ", " ".join(used_letters))

    
        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        

        #getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # Takes awa a life if wrong
                print("Letter is not in word.")
        

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try aganin.")

    # gets here when len(word_letter) == 0 OR  when lives == 0
    if lives == 0:
        print("You died, sorry, The word was", word)
    else:
        print("You guessed the word", word, "!!")


hangman()
