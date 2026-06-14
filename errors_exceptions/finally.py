try:
    with open("secret_code.txt", "r") as file:
        print(file.read())
except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    print("Thank you for using my app!")