# List is a collection of ordered, mutable, allows duplicate elements

mylist = ["Banana", "Cherry", "Apple"]
print(mylist)

mylist2 = [5, True, "Apple", "Apple"]
print(mylist2)

print("\n")

item = mylist2[-1]
print(item)

print("\n")

# Iteration throught the list
for i in  mylist2:
    print(i)

print("\n")

# Using the conditional statement to check for the item in the list
if "Banana" in mylist:
    print("Yes")
else:
    print("No")
