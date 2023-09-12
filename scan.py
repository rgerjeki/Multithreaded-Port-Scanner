import socket
from concurrent.futures import ThreadPoolExecutor

def scan_local_ports():
    target = '127.0.0.1'
    ports = list(range(1, 1025))  # Scans ports from 1 to 1024
    open_ports = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda port: (port, scan_port(target, port)), ports)

    for port, is_open in results:
        if is_open:
            print(f"Port {port} is open on localhost!")
            open_ports.append(port)

    return open_ports

def scan_port(target, port):
    try:
        with socket.create_connection((target, port), timeout=1) as s:
            s.close()
        return True
    except:
        return False

if __name__ == "__main__":
    open_ports = scan_local_ports()
    
    if open_ports:
        print(f"Open ports on localhost: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found on localhost within the range 1-1024.")
