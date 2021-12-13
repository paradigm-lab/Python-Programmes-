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

madlibs = "Computer programming is so {}! It makes me so excited all the time because \
I love to {}. Stay hydrated and {} like you are {}!".format(adj, verb1, verb2, famous_person)

print(madlibs)


