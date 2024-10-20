# Encryption Program in Python

import random
import string

chars =  " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()


random.shuffle(key)

# Encryption Program
plain_text = input("Enter your text to be encrypted! ")
encrypt_message = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypt_message += key[index]

print(f"Your original text was: {plain_text}")
print(f"The encrypted text is: {encrypt_message}")
# Decryption Program
dencrypt_message = input("Enter your text to be encrypted! ")
plain_text = ""

for letter in dencrypt_message:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Your decrypted text was: {dencrypt_message}")
print(f"The text is: {plain_text}")



