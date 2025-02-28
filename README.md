#Python Multi-threaded Port Scanner
This script scans for open ports on a target IP address or hostname, allowing the user to choose between:
- Scanning only common ports (faster).
- Scanning all well-known ports (1-1023) (slower but thorough).
It uses multi-threading to speed up the scanning process.

USAGE:
The tool can be run through command line via: 
- python scanner.py 192.168.1.1  # Uses command-line argument.
- python scanner.py # Enter Hostname/IP during script prompt.

Modules in use:
- sys: Handles command-line arguments.
- socket: Allows network communication (checking if ports are open).
- threading: Enables multi-threaded scanning (faster performance).
- datetime: Records the scan start time.

Common Ports List:
- 22: "SSH" # Remote login and secure command execution. Often attacked via brute-force login attempts.
- 23: "Telnet" # Legacy remote login protocol, not encrypted, making it a security risk.
- 25: "SMTP" # Used for sending emails. Open SMTP ports can be exploited for spamming.
- 53: "DNS" # Translates domain names (e.g., google.com) into IPs. Attackers target it for DNS poisoning and DDoS reflection attacks.
- 80: "HTTP" # Standard web traffic. A common target for website attacks (e.g., SQL Injection, Cross-Site Scripting).
- 110: "POP3" # Used for retrieving emails from a mail server. Hackers can intercept login credentials if not encrypted.
- 143: "IMAP" # Alternative to POP3, allowing email access from multiple devices. Can be exploited if weak credentials are used.
- 443: "HTTPS" # Secure version of HTTP using SSL/TLS encryption. Attackers might try SSL vulnerabilities or misconfigurations.
- 3389: "RDP" # Used for remote access to Windows machines. A prime target for ransomware and brute-force attacks.
Why these are important:
- Attackers scan these first. Since they are standard services, attackers look for misconfigured or outdated versions.
- Brute-force attacks. Services like SSH (22) and RDP (3389) are frequent targets for password-cracking attempts.
- Sensitive data exposure. If unencrypted versions of services (Telnet, HTTP, POP3) are open, data could be intercepted.

Port Scan Function:
- AF_INET # Specifies IPv4 addresses.
- SOCK_STREAM # Uses TCP (Transmission Control Protocol).
- Maxium response wait time of 1 second to prevent hanging.
- s.connect_ex() # Returns a non-zero value if the port is closed or unreachable.
- Doesnt scan for UDP because UDP doesn’t always respond (even if the port is open).

Why use Threads?:
Without Threads (Single-threaded Execution)
- Each port scan waits for the previous one to complete.
- Takes too long because each connection attempt takes time.
With Threads (Multi-threaded Execution)
- Each port scan runs in parallel.
- Faster since multiple ports are checked at the same time.
- Waits until all threads finish before exiting


