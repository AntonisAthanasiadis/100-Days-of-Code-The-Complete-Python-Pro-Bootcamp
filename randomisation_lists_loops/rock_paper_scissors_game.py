import random

options = ["rock", "paper", "scissors"]

#Get the player's move
user_choice = input("Enter rock, paper, or scissors: ").lower()

#Let the computer pick a move from the list
computer_choice = random.choice(options)

print(f"Computer chose: {computer_choice}")

#Choose the winner
if user_choice == computer_choice:
    print("It is a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock beats scissors.")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Paper beats rock.")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors beats paper.")
else:
    print("You lose! Try again.")