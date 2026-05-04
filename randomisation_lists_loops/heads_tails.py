import random

#Generate a random number: 0 or 1
coin_result = random.randint(0, 1)

#Convert number into result
if coin_result == 0:
    print("Heads")
else:
    print("Tails")