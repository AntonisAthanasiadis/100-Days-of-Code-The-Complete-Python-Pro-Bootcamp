# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt","a") as file:
    file.write("\nHow are you?")

with open("new_file.txt", "w") as file:
    file.write("This is a new file.")
