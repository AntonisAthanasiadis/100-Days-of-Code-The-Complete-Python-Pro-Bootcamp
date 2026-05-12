def encrypt(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    text = text.lower()

    for char in text:
        #Find the current position of the letter(0 to 25)
        current_index = alphabet.find(char)

        #Calculate the new position
        new_index = (current_index + shift) % 26

        #Find result based on new_index
        result = result + alphabet[new_index]

    return result


def decrypt(text, shift):
    #Decrypting is just encrypting with a negative shift!
    return encrypt(text, -shift)

my_message = "python"
my_shift = 3

secret = encrypt(my_message, my_shift)
original = decrypt(secret, my_shift)

print(f"Original:  {my_message}")
print(f"Encrypted: {secret}")
print(f"Decrypted: {original}")