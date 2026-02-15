import os
import socket
print("System Information:")
print("Computer Name:", socket.gethostname())
print("Local IP Address:", socket.gethostbyname(socket.gethostname()))
print("Current User:", os.getlogin())
print("Day 1 completed successfully!")