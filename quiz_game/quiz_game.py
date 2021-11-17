
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print()

print("Okay! Let's play :)")
score = 0

print()

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stands for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stands for? ").lower()

if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print()
print("You got ", score, " question correct!");
print("You got " + str(((score/4) * 100)) + "%.")

