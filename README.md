# Python Port Scanner

## Description

This project is a TCP port scanning application developed in Python. The scanner allows for checking the availability of TCP ports on either an individual host or an entire network, identifying known services operating on those ports. Designed to be simple yet effective, the application supports setting a range of ports for scanning and identifying well-known ports with their associated services.

## Prerequisites

Before you begin, make sure you have Python installed on your system. This project has been tested with Python 3.8 or higher. No external libraries are required beyond those that come with the standard Python installation.

## Installation

No specific installation is necessary to run this script. However, you can clone this repository or directly download the script to your local computer. To clone the repository, use the following command:

```
git clone https://github.com/victorlga/portscan.git
```

## How to Use

The application offers flexibility to scan a single host or an entire network. Below are instructions on how to use each functionality:

### Scanning a Specific Host

```
python port_scanner.py --host <host_address_or_IP> --start <start_port> --end <end_port>
```

- `--host`: Specifies the IP address or hostname to be scanned.
- `--start`: The starting port number of the range of ports to be scanned.
- `--end`: The ending port number of the range.

#### Example:

To scan the host `192.168.1.1` from port 80 to 100:

```
python port_scanner.py --host 192.168.1.1 --start 80 --end 100
```

### Scanning an Entire Network

```
python port_scanner.py --network <network_in_CIDR_notation> --start <start_port> --end <end_port>
```

- `--network`: Specifies the network to be scanned in CIDR notation (e.g., `192.168.1.0/24`).
- `--start` and `--end`: Define the port range in the same way as the `--host` option.

#### Example:

To scan the network `192.168.1.0/24` from port 22 to 80:

```
python port_scanner.py --network 192.168.1.0/24 --start 22 --end 80
```

## Features

- TCP port scanning of a host or an entire network.
- Setting a range of ports for scanning.
- Identification of well-known ports and displaying the services associated with those ports.

## License

This project is distributed under the MIT license. See the `LICENSE` file for more details.
