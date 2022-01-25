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


print("\n")

# Using the len function to print the length of my list
print(len(mylist))


print("\n")

# Using the append method to add the item in the last possition of the list
mylist.append("Lemon")
print(mylist)


print("\n")

# Using the insert method to add the item to the specific location
mylist.insert(1, "Blueberry")
print(mylist)


print("\n")


# Used the pop method to remove the item in the list
out = mylist.pop()
print(out)
print(mylist)
