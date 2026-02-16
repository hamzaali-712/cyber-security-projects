import random
import string
import math
#In ecryption we always work on indexes of the characters in the alphabet, 
# so we need to define an alphabet that includes all the characters we want to use in our messages.
# In this case, we will include lowercase letters, uppercase letters, punctuation, digits, and space.
# Define the alphabet
alphabet = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits + " ")

def generate_key(alphabet):
    shuffled_alphabets = alphabet.copy()
    random.shuffle(shuffled_alphabets)
    return shuffled_alphabets

print("Generated key:", generate_key(alphabet))
print("Number of possible keys =", math.factorial(len(alphabet)))

def encrypt(text, key, alphabet):
    encrypted = [key[alphabet.index(c)] for c in text]
    return ''.join(encrypted)

def decrypt(text, key, alphabet):
    decrypted = [alphabet[key.index(c)] for c in text]
    return ''.join(decrypted)

# Generate a key
generated_key = generate_key(alphabet)

Message = "Hello World! I am new in this field. My name is Hamza Ali"

# Encrypt
encrypted_message = encrypt(Message, generated_key, alphabet)
print("Encrypted:", encrypted_message)

# Decrypt
decrypted_message = decrypt(encrypted_message, generated_key, alphabet)
print("Decrypted:", decrypted_message)
