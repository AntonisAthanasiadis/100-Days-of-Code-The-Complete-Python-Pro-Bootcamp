#Basic if else at the rollercoaster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry you have to grow taller before riding the rollercoaster.")

#Learning about the Modulo operator (%)
print(f"10%5 is {10%5}") #result = 0 - no remainder
print(f"10%3 is {10%3}") #result = 1 - one remains after division

#Odd - Even check
number_to_check = int(input("What is the number? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

#Nested if else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 5€.")
    elif age <= 18:
        print("Please pay 5€.")
    else:
        print("Please pay 12€")
else:
    print("Sorry you have to grow taller before riding the rollercoaster.")
