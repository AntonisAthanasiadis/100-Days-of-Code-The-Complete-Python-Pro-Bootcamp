#Understanding data types and manipulating strings

#Understanding strings as arrays
#Prints o, counting starts from 0
print("Hello"[4])

#Concatenates, doesn't calculate!
print("123" + "345")

#But this one calculates, converting to integer!
print(123 + 456)

#Large integers easy visualization
print(123_456_789)

#Float = floating point number
print(3.14159)

#Boolean
print(True)
print(False)

#Calculate the length of certain data types, also concatenate and cast
print("The length of \"Hello\" is: " + str(len("Hello")))

#Printing data types
print(type("abc"))
print(type("3.14"))
print(type("123"))
print(type("True"))

#Cast and add
print(int("123")+int("456"))

#Calculate input string length
name=input("Enter your name: ")
length_of_name = len(name)
print("Number of characters in your name: " + str(length_of_name))
