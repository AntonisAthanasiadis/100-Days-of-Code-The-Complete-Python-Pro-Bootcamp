#ValueError
try:
    number = int("banana")
except ValueError as e:
    print(f"ValueError Caught: {e}")

#TypeError
try:
    result = "Apple" + 5
except TypeError as e:
    print(f"TypeError Caught: {e}")

#IndexError
try:
    colors = ["red", "blue"]
    wrong_color = colors[5]
except IndexError as e:
    print(f"IndexError Caught: {e}")

#KeyError
try:
    user = {"name": "Tony"}
    email = user["email"]
except KeyError as e:
    print(f"KeyError Caught: '{e}' (Key not found)")

#NameError
try:
    print(total_score)
except NameError as e:
    print(f"NameError Caught: {e}")

#FileNotFoundError
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError Caught: {e}")

#ZeroDivisionError
try:
    calculation = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError Caught: {e}")

print("\nAll errors were successfully caught! The program did not crash.")