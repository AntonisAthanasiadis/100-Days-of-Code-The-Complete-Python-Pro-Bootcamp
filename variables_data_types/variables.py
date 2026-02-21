#Using variables, and some more strings

name = "Tony"
print("Your name is " + name)

name_length=len(name)
print("Your name contains " + str(name_length) + " characters\n")

#Variable swapping
glass1="juice"
glass2="milk"
print("Before swapping")
print("Glass 1 now contains " + glass1)
print("Glass 2 now contains " + glass2)

temp = glass1
glass1 = glass2
glass2 = temp

print("After swapping")
print("Glass 1 now contains " + glass1)
print("Glass 2 now contains " + glass2)