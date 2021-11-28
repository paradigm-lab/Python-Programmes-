# Newton-Raphson method

"""
Algorithm
1. Take approximate root for the square root

2. Add the approximate root with the original number divided by the approximate root and divide by 2. xi:=(xi + n / xi) / 2

3. Repeat step 2 until the difference in the approximate root is less than the precision value.

4. The approximate root is the square root we went.

"""

num = float(input("Enter the number to compute the square root:"))

# Assigning the original value to X for the approximation of the number
x = num # Approximate root

# Compute square root using newton-raphson method
for i in range(0, 10):
    x = (x + num / x) / 2
    print("Approximated value:", x)

print("The square root of the number is:", num, "is", x)


