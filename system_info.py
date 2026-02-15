import os
import socket
print("System Information:")
print("Computer Name:", socket.gethostname())
print("Local IP Address:", socket.gethostbyname(socket.gethostname()))
print("Current User:", os.getlogin())
print("Operating System:", os.name)
print("Platform:", os.sys.platform)
print("Python Version:", os.sys.version)
print("Current Working Directory:", os.getcwd())
print("Day 1 completed successfully!")