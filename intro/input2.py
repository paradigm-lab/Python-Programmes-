'''
Data Types: Integers, Strings, Boolean, Float

Lists -> To store multiple items in a single variable
      -> A list can contain different data types
      -> Lists are represented using the square brackets []

      Basic List Operations:
      -> Create a list ->  Using the square brackets
      -> Add an item to the list -> Using the append() method 
      -> Remove an item from the list -> using the remove method by specifing the actual item within the list
      -> Change items in the list
      -> Access item of the list -> Using the index number eg: fruits[0]

Sets -> Built-in data type of python a
     -> as with Lists, used to store multiple items of data
     -> Does NOT allow duplicate values
     -> Sets are represented using the curly braces { ... }

      Basic Sets Operations:
      -> Create a list ->  Using the curly braces { ... }
      -> Add an item to the list -> Using the add method
      -> Remove an item from the list -> using the remove method by specifing the actual item within the set
      -> Change items in the list
      -> Access item of the list -> Using the for loop and not the !index
                                 -> When printing the item they are not ordered same as the list 

For loop
      -> Is used for iterating over a sequence (like a list)
      -> So we can execute samething for each item in a list
'''

# Expression an instruction that combines values and operators and always evalutes down to a single value
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"



# Function Definition
# Code Encapsulation to the function to make a clean up of the code
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"

def validate_and_execute():
    #if user_input.isdigit():
    try:    
        # Return value of inner function is the input value for the outer function
        user_input_number = int(num_of_days_element)
        # using the nested if..else.. statement 
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, Please enter a valid positive number")
        else:
            print("You entered a negative number, no conversion for you!")

    except ValueError:
        print("Your input is not a valid number. Don't ruin my program")


user_input = ""
while user_input != "exit":
    # To ask the user for a input 
    # Built-In F(x) are provided by Python language itself 
    user_input = input("Hey user, enter a number of days as a comma separted list and I will convert it to seconds \n")

    list_of_days = user_input.split(", ")
   

    '''
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))
    '''


    # The split() will splits a string into a list
    # By default separator is any whitespace it can be overrided
    # Looping through a list and getting one element at a time and that is why we don't use the index
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
