import socket
import subprocess
import datetime

#input
target=input("Enter the target domain(eample.com): ")
print("\nStarting Reconnaissance on " + target)

report=[]
now= datetime.datetime.now()

#resolveIP
try:
    ip=socket.gethostbyname(target)
    print("\n[+] IP Address: " + ip)
    report.append("IP Address: " + ip)
except:
    print("\n[-] Could not resolve IP address for " + target)
    report.append("Could not resolve IP address for " + target)

#DNS Information
try:
    print("\n[+] DNS Lookup:")
    dns_info = socket.gethostbyname_ex(target)
    print(dns_info)
    report.append("DNS Lookup: " + str(dns_info))
except:
    print("\n[-] Could not perform DNS lookup for " + target)
    report.append("Could not perform DNS lookup for " + target)

#MIXED record
try:
    print("\n[+] MX Records:")
    mx_records = subprocess.check_output(["nslookup", "-type=mx", target]).decode()
    print(mx_records)
    report.append("MX Records: " + mx_records)
except:
    print("\n[-] Could not retrieve MX records for " + target)
    report.append("Could not retrieve MX records for " + target)

#MX record
try:
    print("\n[+] NS Records:")
    ns_records = subprocess.check_output(["nslookup", "-type=ns", target]).decode()
    print(ns_records)
    report.append("NS Records: " + ns_records)
except:
    print("\n[-] Could not retrieve NS records for " + target)
    report.append("Could not retrieve NS records for " + target)
    
#Ping Test 
try:
    print("\n[+] Ping Test:")
    ping_result = subprocess.check_output(["ping", "-c", "4", target]).decode()
    print(ping_result)
    report.append("Ping Test: " + ping_result)
except:
    print("\n[-] Could not perform ping test for " + target)
    report.append("Could not perform ping test for " + target)

#Basic Port Scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389,3306]
open_ports = []
print("\n[+] Scanning Common Ports:")
for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
        open_ports.append(port)
    sock.close()
report.append("Open Ports: " + str(open_ports))

#Save Report
with open("recon_report.txt", "w") as f:
    f.write(f"Reconnaissance Report for {target}\n")
    f.write(f"Generated on: {now}\n\n")
    for item in report:
        f.write(item + "\n")
print("\nReconnaissance completed. Report saved to recon_report.txt")
