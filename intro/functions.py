# Function is a block of code which only runs when it's called
# You can pass data, known as parameter or without parameter
# A function can return data as a result

# A fucntion is defined using the def keyword

calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"

# Function Definition
def days_to_units(): 
	print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")
	print("All good!")


# Function Calling
days_to_units()
