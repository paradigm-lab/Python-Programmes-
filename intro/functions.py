# Function is a block of code which only runs when it's called
# You can pass data, known as parameter or without parameter
# Parameter are also called Arguments
# A function can return data as a result

# A fucntion is defined using the def keyword

calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


# Function Definition
# With the return type
def days_to_units(num_of_days): 
    return (f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}")

# Function Calling and storing the return type of the function to the variable
my_var = days_to_units(20)
print(my_var)
