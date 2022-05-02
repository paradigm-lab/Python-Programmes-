# Function is a block of code which only runs when it's called
# You can pass data, known as parameter or without parameter
# Parameter are also called Arguments
# A function can return data as a result

# A fucntion is defined using the def keyword

calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


# Function Definition
def days_to_units(num_of_days, message): 
	print(f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}")
	print(message)

# Function Calling
days_to_units(20, "Awesome")
days_to_units(35, "Great")
