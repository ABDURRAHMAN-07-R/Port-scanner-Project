import socket
import sys

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Timeout after 1 second
            
            # Attempt to connect
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")
            
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved.")
            sys.exit()
        except socket.error:
            print("Couldn't connect to server.")
            sys.exit()

if __name__ == "_main_":
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <target> <start_port> <end_port>")
        print("Example: python port_scanner.py 192.168.1.1 1 100")
        sys.exit()
    
    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    
    scan_ports(target, start_port, end_port)
