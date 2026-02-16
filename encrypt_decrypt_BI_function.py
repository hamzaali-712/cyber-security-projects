from cryptography.fernet import Fernet

# Generate a key (must be kept secret)
key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Hello World! I am Hamza Ali"

# Encrypt
encrypted = cipher.encrypt(message)

# Decrypt
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
