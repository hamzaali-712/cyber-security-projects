import socket
import subprocess
import datetime
import platform
import threading
import whois

# =========================
# CONFIG
# =========================
common_ports = [21,22,23,25,53,80,110,143,443,3389,3306,8080]
open_ports = []
lock = threading.Lock()

# =========================
# INPUT
# =========================
target = input("Enter target domain (example.com): ")
print("\nStarting Advanced Recon on", target)

report = []
now = datetime.datetime.now()

# =========================
# IP RESOLUTION
# =========================
try:
    ip = socket.gethostbyname(target)
    print("[+] IP Address:", ip)
    report.append("IP Address: " + ip)
except:
    print("[-] Could not resolve IP.")
    report.append("IP resolution failed.")
    ip = None

# =========================
# DNS LOOKUP
# =========================
try:
    dns_info = socket.gethostbyname_ex(target)
    print("[+] DNS Info:", dns_info)
    report.append("DNS Info: " + str(dns_info))
except:
    print("[-] DNS lookup failed.")

# =========================
# WHOIS LOOKUP
# =========================
try:
    w = whois.whois(target)
    print("[+] WHOIS Info Found")
    report.append("WHOIS Info:\n" + str(w))
except:
    print("[-] WHOIS lookup failed.")

# =========================
# PING TEST (Auto Detect OS)
# =========================
try:
    print("[+] Ping Test:")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    ping = subprocess.check_output(["ping", param, "4", target]).decode()
    print(ping)
    report.append("Ping Result:\n" + ping)
except:
    print("[-] Ping failed.")
    report.append("Ping failed.")

# =========================
# PORT SCANNING (MULTITHREADED)
# =========================
def scan_port(port):
    global open_ports
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            with lock:
                open_ports.append(port)
                print(f"[+] Port {port} is OPEN")
                banner_grab(port)
        sock.close()
    except:
        pass

# =========================
# BANNER GRABBING
# =========================
def banner_grab(port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore")
        print(f"[+] Banner on port {port}:\n{banner}")
        report.append(f"Banner {port}:\n{banner}")
        sock.close()
    except:
        pass

if ip:
    print("\n[+] Starting Port Scan...")
    threads = []
    for port in common_ports:
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

report.append("Open Ports: " + str(open_ports))

# =========================
# SAVE REPORT
# =========================
with open("advanced_recon_report.txt", "w", encoding="utf-8") as f:
    f.write("Advanced Reconnaissance Report\n")
    f.write("Target: " + target + "\n")
    f.write("Generated on: " + str(now) + "\n\n")
    for item in report:
        f.write(item + "\n\n")

print("\nRecon Completed.")
print("Report saved as advanced_recon_report.txt")