

name = input("Type your name: ")
print("Welcome", name, "to this adventure! \n")


answer = input("You are on a dirt road, it has came to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()
    
    if answer == "swim":
        print("You swam accross and were eaten by an alligator. \n")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game. \n")

    else: 
        print("Not a valid option. You lose. \n")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    
    if answer == "back":
        print("You go back and lose\n")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN! \n")
        elif answer == "no":
            print("You ignore the stranger and they are offended and YOU LOSE. \n")    
        else:
            print("Not a valid option. You lose. \n")
    

    else: 
        print("Not a valid option. You lose. \n")
    


else: 
    print("Not a valid option. You lose. \n")

print("Thank you for trying", name)


