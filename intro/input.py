# Expression an instruction that combines values and operators and always evalutes down to a single value
calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


# Function Definition
def days_to_units(num_of_days):
	print(f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}")

# To ask the user for a input 
# Built-In F(x) are provided by Python language itself
user_input = input("Hey user, enter a number of days and I will convert it to hours! \n")
print(user_input)
