import os 
import psutil
import subprocess
import socket
import platform

#CPU Information
def get_cpu_info():
    print("Gathering CPU information...")
    print("CPU Usage: {}%".format(psutil.cpu_percent(interval=1)))
    print("CPU Cores: {}".format(psutil.cpu_count()))
    cpu_info = {}
    cpu_info['Physical Cores'] = psutil.cpu_count(logical=False)
    cpu_info['Total Cores'] = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    cpu_info['Max Frequency'] = f"{cpu_freq.max:.2f}Mhz"
    cpu_info['Min Frequency'] = f"{cpu_freq.min:.2f}Mhz"
    cpu_info['Current Frequency'] = f"{cpu_freq.current:.2f}Mhz"
    return cpu_info

#RAM Information
def get_ram_info():
    print("Gathering RAM information...")
    ram_info = {}
    virtual_mem = psutil.virtual_memory()
    ram_info['Total'] = f"{virtual_mem.total / (1024 ** 3):.2f} GB"
    ram_info['Available'] = f"{virtual_mem.available / (1024 ** 3):.2f} GB"
    ram_info['Used'] = f"{virtual_mem.used / (1024 ** 3):.2f} GB"
    ram_info['Percentage'] = f"{virtual_mem.percent}%"
    return ram_info

#Disk Information
def get_disk_info():
    print("Gathering Disk information...")
    disk_info = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.device] = {
                'Total': f"{usage.total / (1024 ** 3):.2f} GB",
                'Used': f"{usage.used / (1024 ** 3):.2f} GB",
                'Free': f"{usage.free / (1024 ** 3):.2f} GB",
                'Percentage': f"{usage.percent}%"
            }
        except PermissionError:
            continue
    return disk_info

#Network Information
def get_network_info():
    print("Gathering Network information...")
    network_info = {}
    addrs = psutil.net_if_addrs()
    for interface, addr_list in addrs.items():
        for addr in addr_list:
            if addr.family == socket.AF_INET:   # <- use socket.AF_INET
                network_info[interface] = {
                    'IP Address': addr.address,
                    'Netmask': addr.netmask,
                    'Broadcast': addr.broadcast
                }
    return network_info

#running processes
def get_process_info():
    print("Gathering Process information...")
    process_info = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        process_info.append(proc.info)
    return process_info

#System Information
def get_system_info():
    print("Gathering System information...")
    system_info = {}
    system_info['Platform'] = os.name
    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    return system_info

#Main Menu
def main():
    print("System and Network Status Checker")
    print("=================================")
    while True:
        print("\nOptions:")
        print("1. Check CPU Information")
        print("2. Check RAM Information")
        print("3. Check Disk Information")
        print("4. Check Network Information")
        print("5. Check Running Processes")
        print("6. Check System Information")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            cpu_info = get_cpu_info()
            for key, value in cpu_info.items():
                print(f"{key}: {value}")
        elif choice == "2":
            ram_info = get_ram_info()
            for key, value in ram_info.items():
                print(f"{key}: {value}")
        elif choice == "3":
            disk_info = get_disk_info()
            for partition, info in disk_info.items():
                print(f"Partition: {partition}")
                for key, value in info.items():
                    print(f"  {key}: {value}")
        elif choice == "4":
            network_info = get_network_info()
            for interface, info in network_info.items():
                print(f"Interface: {interface}")
                for key, value in info.items():
                    print(f"  {key}: {value}")
        elif choice == "5":
            process_info = get_process_info()
            for proc in process_info:
                print(f"PID: {proc['pid']}, Name: {proc['name']}, User: {proc['username']}")
        elif choice == "6":
            system_info = get_system_info()
            for key, value in system_info.items():
                print(f"{key}: {value}")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()