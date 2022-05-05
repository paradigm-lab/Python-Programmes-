# Expression an instruction that combines values and operators and always evalutes down to a single value
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


# Function Definition
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"
    elif num_of_days == 0: 
        return "Your entered a 0, Please enter a valid positive number" 
    else:
        return "You entered a negative value, so no conversion for you!"


# To ask the user for a input 
# Built-In F(x) are provided by Python language itself
user_input = input("Hey user, enter a number of days and I will convert it to hours! \n")

if user_input.isdigit():
    # Return value of inner function is the input value for the outer function
    calculated_value = days_to_units(int(user_input))
    print(calculated_value)
else:
    print("Your input is not a number. Don't ruin my program")
