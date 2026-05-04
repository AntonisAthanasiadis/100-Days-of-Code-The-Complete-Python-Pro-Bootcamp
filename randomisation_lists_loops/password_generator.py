import random
#Create a list of letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', '_']

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

#easy mode
password = ""
print("Starting easy mode")
#concatenate characters to blank string
for char in range(0, nr_letters):
    password = password + random.choice(letters)
    print(password)

for char in range(0, nr_symbols):
    password = password + random.choice(symbols)
    print(password)

for char in range(0, nr_numbers):
    password = password + random.choice(numbers)
    print(password)
print(f"Final password on easy mode is {password} \n")

#hard mode - harder to crack
password_list = []
print("Starting hard mode")
#append characters to list
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
    print(password_list)

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
    print(password_list)

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
    print(password_list)

#Shuffle list
random.shuffle(password_list)
print(password_list)

#Convert list to String
hard_password = ""
for char in password_list:
    hard_password += char

print(f"Final password on hard mode is {hard_password}")
