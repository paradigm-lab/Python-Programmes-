# Finding the square root of a number using Newton's Method.

num = float(input("Enter the number to compute the square root: "))
approx = 0.5 * num
print("Approx:", approx)
better = 0.5 * (approx + num/approx)
print("Better:", better)

while (better != approx):
    approx = better
    print("Approx:", approx)
    better = 0.5 * (approx + num / approx)
    print("Better:", better)
print("The square root of", num, "is", better, sep=" ")
