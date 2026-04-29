import random

#Names in a list
participants = ["Tony", "Maria", "George"]

#use random.choice to select one name from the list
payer = random.choice(participants)

print(f"The person paying the bill today is: {payer}")