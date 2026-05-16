# Port Scanner - Scans a target for open ports
# Saves results to a report file automatically
# Part of SecureNet Toolkit

import socket
import datetime

def scan_ports(target, start_port, end_port):
    print(f"\n{'='*50}")
    print(f"  Scanning Target: {target}")
    print(f"  Port Range: {start_port} - {end_port}")
    print(f"{'='*50}\n")

    open_ports = []
    start_time = datetime.datetime.now()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            service = get_service_name(port)
            print(f"  [OPEN]   Port {port}  →  {service}")
            open_ports.append((port, service))
        sock.close()

    if not open_ports:
        print("  No open ports found.")

    end_time = datetime.datetime.now()
    duration = (end_time - start_time).seconds

    print(f"\n  Scan complete. {len(open_ports)} open port(s) found.")
    print(f"  Time taken: {duration} seconds\n")

    # Save report to file
    save_report(target, start_port, end_port, open_ports, start_time, duration)

def get_service_name(port):
    """Returns common service name for well-known ports"""
    services = {
        21: "FTP", 22: "SSH", 23: "Telnet",
        25: "SMTP", 53: "DNS", 80: "HTTP",
        110: "POP3", 143: "IMAP", 443: "HTTPS",
        3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
    }
    return services.get(port, "Unknown")

def save_report(target, start_port, end_port, open_ports, scan_time, duration):
    """Saves scan results to a .txt report file"""
    filename = f"scan_report_{target.replace('.', '_')}_{scan_time.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("="*50 + "\n")
        f.write("       SECURENET TOOLKIT - SCAN REPORT\n")
        f.write("="*50 + "\n\n")
        f.write(f"  Target     : {target}\n")
        f.write(f"  Port Range : {start_port} - {end_port}\n")
        f.write(f"  Scan Time  : {scan_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"  Duration   : {duration} seconds\n\n")
        f.write("-"*50 + "\n")
        f.write("  OPEN PORTS\n")
        f.write("-"*50 + "\n")

        if open_ports:
            for port, service in open_ports:
                f.write(f"  [OPEN]  Port {port}  →  {service}\n")
        else:
            f.write("  No open ports found.\n")

        f.write("\n" + "="*50 + "\n")
        f.write(f"  Total open ports: {len(open_ports)}\n")
        f.write("="*50 + "\n")

    print(f"  📄 Report saved as: {filename}\n")

# --- Run the scanner directly ---
if __name__ == "__main__":
    target = input("Enter target IP or domain (e.g. 127.0.0.1): ")
    start  = int(input("Start port (e.g. 1): "))
    end    = int(input("End port (e.g. 100): "))
    scan_ports(target, start, end)