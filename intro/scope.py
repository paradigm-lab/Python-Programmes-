# Scope: A variable is only available from inside the region it's created
#	Global Variable = Variables available from within any scope
#	Local Variable = Variables created inside function
#		                 Can only be used inside the function
# 	Internal Variable = Variables which are passed in the function parameter


calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


# Function Definition
def days_to_units(num_of_days, message): 
	print(f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}")
	print(message)


def scope_check(num_of_days):
	print(name_of_unit)
	print(num_of_days)


# Function Calling
scope_check(7)
