#This is a module that constist of several function(Default)
import random

#range takes place from 0 to number - 1
#r = random.randrange(-5, 11)


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
    


#The randint function what it does it include 11 to the random generating 
random_number = random.randint(0, top_of_range)
#print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. \n")
        continue

    if user_guess == random_number:
        print("You got it! \n")
        break
    elif user_guess > random_number:
        print("You were above the number! \n")
    else:
        print("You were below the number! \n")


print()
print("You got it in", guesses, "guesses")

