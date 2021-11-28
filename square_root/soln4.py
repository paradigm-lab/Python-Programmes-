# Finding the square root of a number using Newton's Method.

num = float(input("Enter the number to compute the square root: "))
approx = 0.5 * num
better = 0.5 * (approx + num/approx)

while (better != approx):
    approx = better
    better = 0.5 * (approx + num / approx)

print("The square root of", num, "is", better, sep=" ")
