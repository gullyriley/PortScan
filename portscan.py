import sys
import socket
import threading
from datetime import datetime

# Define common ports
common_ports = {
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3389: "RDP"
}

# Get target from user input
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    target = input("Enter the target hostname or IP address: ").strip()
    if not target:
        print("Please add a target hostname or IP address")
        sys.exit()

# Ask user for scan type
print("\nSelect scan type:")
print("1 - Scan common ports (fast)")
print("2 - Scan all ports 1-1023 (slow)")
choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    ports_to_scan = list(common_ports.keys())  # Scan only common ports
elif choice == "2":
    ports_to_scan = range(1, 1024)  # Scan full range 1-1023
else:
    print("Invalid choice. Exiting.")
    sys.exit()

print("=" * 45)
print(f"Scanning Target: {target}")
print(f"Scanning started: {datetime.now()}")
print("=" * 45)

# Function to scan a single port
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        service = common_ports.get(port, "Unknown Service")
        print(f"Port {port} ({service}) is open")
    s.close()

# Start multi-threaded scan
threads = []
for port in ports_to_scan:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Scan complete!")
