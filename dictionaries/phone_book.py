#Creating the dictionary
phone_book = {
    "Tony": "2107777777",
    "George": "2310123456",
    "Maria": "2108888888"
}

#Printing the dictionary
print(f"Current Phone Book: {phone_book}")

#Adding a new entry
phone_book["Kostas"] = "2310999999"
print(f"Added Kostas: {phone_book}")

#Accessing a specific value

maria_number = phone_book["Maria"]
print(f"Maria's number is: {maria_number}")

#Checking if a key exists
if "Tony" in phone_book:
    print("Tony is in the phone book.")

#Removing an entry
removed_number = phone_book.pop("George")
print(f"Removed George. His number was: {removed_number}")
print(f"Updated Book: {phone_book}")

#Emptying the dictionary

phone_book.clear()
print(f"Dictionary cleared. New contents: {phone_book}")