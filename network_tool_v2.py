import os
import socket
import platform

print("=== Welcome to the Network Tool v2.0! ====\n")

# System Information
print("[*] Gathering System Information:")
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
system_name = platform.system()

print(f"Hostname: {hostname}")
print(f"Local IP Address: {local_ip}")
print(f"System Name: {system_name}")

# Target input
target = input("Enter website (example: google.com): ")

try:
    # Resolve target IP
    target_ip = socket.gethostbyname(target)
    print(f"IP address of {target}: {target_ip}")

    print("\n=================\n")

    # Ping execution
    print("[*] Pinging the target...")

    if system_name == "Windows":
        os.system(f"ping -n 4 {target}")
    else:
        os.system(f"ping -c 4 {target}")

except socket.gaierror:
    print("Unable to resolve the target. Please check the website address and try again.")

print("\n=================\n")
print("Scan completed successfully!")
print("Thank you for using the Network Tool v2.0! Goodbye!")
print("===========================================")

