import random

#A list containing three sub-lists
ef_list= ["E", "F"]
letter_list = [
    ["A", "B"],
    ["C", "D"],
    ef_list
]

#Pick a random sub-list
chosen_list = random.choice(letter_list)

#Pick a random letter from that list
letter = random.choice(chosen_list)

print(f"The chosen letter is: {letter}")