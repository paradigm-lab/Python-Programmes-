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
        user_input_number = int(user_input)
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
    user_input = input("Hey user, enter a number of days and I will convert it to hours! \n")
    validate_and_execute()
