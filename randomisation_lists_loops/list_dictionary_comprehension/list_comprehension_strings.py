words = ["Python", "Is", "Incredibly", "Fun"]
initials = [word[0] for word in words]
print(initials)

sentence = "hello world"
no_vowels = [char for char in sentence if char not in "aeiou"]
clean_string = "".join(no_vowels)
print(clean_string)

fruits = ["apple", "banana", "kiwi", "pear", "mango", "fig"]
long_fruits = [f for f in fruits if len(f) > 4]
print(long_fruits)