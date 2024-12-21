import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

#print(f"Chars: {chars}")
#print(f"Key: {key}")

#ENCRYPTION

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Orig: {plain_text}")
print(f"Encrypted: {cipher_text}")