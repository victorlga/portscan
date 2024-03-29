import csv
import socket
import threading
from queue import Queue
import argparse
import ipaddress

# Defining a list of well-known ports
csv_file = open('well_known_ports.csv', 'r')
csv_reader = csv.reader(csv_file)

next(csv_reader)

well_known_ports = {}
for line in csv_reader:

    port_val_not_empty = line[1] and line[0]
    if line[3] not in ('Unassigned', 'Reserved') and port_val_not_empty:

        if '-' in line[1]:
            start, end = line[1].split('-')
            for port in range(int(start), int(end) + 1):
                well_known_ports[port] = line[0]
        else:
            well_known_ports[int(line[1])] = line[0]

# Function to scan a single port
def scan_port(ip, port, timeout=1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(timeout)
    try:
        scanner.connect((ip, port))
        scanner.close()
        if port in well_known_ports:
            print(f"{ip}: Port {port} is open ({well_known_ports[port]})")
        else:
            print(f"{ip}: Port {port} is open")
    except:
        pass

# Function to manage the scanning of multiple ports
def threader():
    while True:
        ip, port = port_queue.get()
        scan_port(ip, port)
        port_queue.task_done()

# Parsing command line arguments
parser = argparse.ArgumentParser(description='Port Scanner')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--host', type=str, help='Host to scan')
group.add_argument('--network', type=str, help='Network to scan in CIDR format (e.g., 192.168.1.0/24)')
parser.add_argument('--start', type=int, help='Start port number', required=True)
parser.add_argument('--end', type=int, help='End port number', required=True)
args = parser.parse_args()

port_queue = Queue()

# Creating threads for parallel scanning
for _ in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# Function to calculate all IPs in a network
def calculate_ips(network_cidr):
    network = ipaddress.ip_network(network_cidr)
    return [str(ip) for ip in network.hosts()]

# Enqueuing the ports and IPs
if args.network:
    for ip in calculate_ips(args.network):
        for port in range(args.start, args.end + 1):
            port_queue.put((ip, port))
elif args.host:
    for port in range(args.start, args.end + 1):
        port_queue.put((args.host, port))

port_queue.join()
