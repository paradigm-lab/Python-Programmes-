"""
String concatenation is the way of putting strings together.



youtuber = "Collins Boniface"

# A few ways to do this 
print("Subscribe to " + youtuber) # Concatenating the string using the + sign
print("Subscribe to {}".format(youtuber)) # using the curly braces and calling the format method
print(f"Subscribe to {youtuber}") # using an f string

"""

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlibs = "Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {}!".format(famous_person)

print(madlibs)


