import random

secret_number = 0
lives = 0


def set_difficulty():
    global secret_number, lives
    choice = input("Choose difficulty (easy/hard): ")

    if choice == "easy":
        secret_number = random.randint(1, 10)
        lives = 5
        print("Range: 1 to 10. Lives: 5")
    else:
        secret_number = random.randint(1, 100)
        lives = 3
        print("Range: 1 to 100. Lives: 5")


def play_round():
    global lives
    guess = int(input("What is your guess? "))

    if guess == secret_number:
        print("You got it!")
        return True
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")

    lives = lives - 1
    print(f"Lives remaining: {lives}")
    return False


set_difficulty()

while lives > 0:
    won = play_round()
    if won:
        break
else:
    if lives == 0:
        print(f"Game Over! The number was {secret_number}")