# To print the underroot of a number
sqr = sqr = int(input("Enter the number to compute the square root: "))
unr = 0
cond = True
while(cond):
    if unr * unr  == sqr:
        print(f"The underroot of a number is: {unr}")
        cond = False
    else: 
        unr += 1
# End of the program
