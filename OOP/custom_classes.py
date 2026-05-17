class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user_1 = User("Tony", 25)
user_1.id_num = "AA123"

print(user_1.id_num)
print(user_1.name)
print(user_1.age)