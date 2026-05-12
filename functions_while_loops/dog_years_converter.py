def dog_year_converter(dog_name, dog_age):
    # A dog that is 2 years old is roughly 14 in 'human years'
    human_equivalent = dog_age * 7
    print(f"{dog_name} is {dog_age} years old, which is {human_equivalent} in human years.")

# Now the parameters accurately represent the input
dog_year_converter("Tony", 3)
dog_year_converter("Elsa", 5)