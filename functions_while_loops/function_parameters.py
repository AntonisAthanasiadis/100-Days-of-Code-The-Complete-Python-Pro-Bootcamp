def greet():
    print("Hello!")
    print("How do you do?")
    print("Isn't the weather nice?")

greet()

#Function with inputs
name = input("What is your name? ")
def greet_with_name(user_name):
    print("Hello, " + name + "!")
    print("How do you do?")
    print("Isn't the weather nice?")

greet_with_name(name)