#Rocket launch loop
count = 5

while count > 0:
    print(f"Counting down: {count}")
    count = count - 1

print("Blast off!")

#Password Loop
password = ""

while password != "python123":
    password = input("Enter the secret password: ")

    if password != "python123":
        print("Wrong! Try again.")

print("Access granted!")

#Break
while True:
    user_input = input("Type 'exit' to stop the loop: ")

    if user_input == "exit":
        break  

    print(f"You typed: {user_input}")

print("Loop finished.")