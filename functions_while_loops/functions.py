#Hello World (again)
def hello_function():
    print("Hello World")

hello_function()

#Greetings
def greet_user(name):
    print(f"Hello, {name}! Great to see you.")

greet_user("Tony")

#Simple adder
def add_numbers(a, b):
    result = a + b
    return result

sum_total = add_numbers(5, 10)
print(f"The total is: {sum_total}")