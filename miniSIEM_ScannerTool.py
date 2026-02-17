import socket
import datetime

#config
target=input("Enter the target IP address: ")
common_ports={ 
              21:"FTP",
              22:"SSH",
              23:"Telnet",
              80:"HTTP",
              443:"HTTPS",
              3389:"RDP"}
open_ports=[]
risk_level="Low"
print("\nStarting Scan...\n")

#port scan
for port in common_ports:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex((target,port))
    if result==0:
        print("\n[OPEN] Port",port,"(",common_ports[port],") is open.")
        open_ports.append(port)
    else:
        print("\n[CLOSED] Port",port,"(",common_ports[port],") is closed.")
    sock.close()

#risk analysis
if 23 in open_ports:
    risk_level="High(Telnet is insecure)"
elif 21 in open_ports or 3389 in open_ports:
    risk_level="Medium(RDP exposed)"
elif len(open_ports) >=3:
    risk_level="MEDIUM(Multiple ports open)"
else:
    risk_level="Low"

#logging
now=datetime.datetime.now()
log_data = f"""
==== SCAN REPORT ====
Time: {now}
Target: {target}
Open Ports: {open_ports}
Risk Level: {risk_level}
=====================
"""
with open("scan_report.txt","a") as log_file:
    log_file.write(log_data)
print("\nScan Completed!")
print("\nScan completed! Risk Level:",risk_level)
print("Report saved to scan_report.txt")
