

def square_number(number):
    return number ** 0.5

num = float(input("Enter the number to compute the square root:"))
answer = square_number(num)
print("The square root of", num, "is", answer, sep=" ")

# Writing a program to test for the function
def test_square_number():
    assert square_number(4) == 2.0
    assert square_number(64) == 8.0
    assert square_number(100) == 10.0
    print("YOUR CODE IS WORKING CORRECTLY")

# Calling the test function.
#test_square_number()


