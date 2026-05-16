# Port Scanner - Scans a target for open ports
# Part of SecureNet Toolkit

import socket

def scan_ports(target, start_port, end_port):
    print(f"\n{'='*50}")
    print(f"  Scanning Target: {target}")
    print(f"  Port Range: {start_port} - {end_port}")
    print(f"{'='*50}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Wait 0.5 seconds per port

        result = sock.connect_ex((target, port))  # Returns 0 if port is open
        if result == 0:
            print(f"  [OPEN]   Port {port}")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("  No open ports found.")

    print(f"\n  Scan complete. {len(open_ports)} open port(s) found.\n")

# --- Run the scanner ---
if __name__ == "__main__":
    target = input("Enter target IP or domain (e.g. 127.0.0.1): ")
    start  = int(input("Start port (e.g. 1): "))
    end    = int(input("End port (e.g. 100): "))
    scan_ports(target, start, end)