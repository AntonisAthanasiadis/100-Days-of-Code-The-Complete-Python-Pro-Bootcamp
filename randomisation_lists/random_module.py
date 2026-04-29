import random
import module_training

#Random number between 1 and 10
random_integer = random.randint(1,10)
print(f"Here's a random integer 1-10: {random_integer}")

print(f"My favourite number is {module_training.my_number}")

random_number_0_to_1 = random.random()
print(f"Here's a random number 0-1: {random_number_0_to_1}")

random_float = random.uniform(1, 10)
print(f"Here's a random number 1-10: {random_float}")