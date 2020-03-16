import socket
import argparse

def printGreen(text): print(f"\033[92m {text}\033[00m") 
def printRed(text): print(f"\033[91m {text}\033[00m") 

'''
Creates a generator object with all the ports to be checked
'''
def createPortsGenerator(port_input_list):
    for port_input in port_input_list:
        if not ('-' in port_input):
            yield int(port_input)
            
        else:
            lowest = int(port_input.split('-')[0])
            highest = int(port_input.split('-')[1])

            for port in range(lowest,highest+1):
                yield port

parser = argparse.ArgumentParser(description='Check if given port/ports at given host is/are open.')

parser.add_argument('host', help='The hostname or IP')
parser.add_argument('-t', '--timeout', default=2, type=int, help="The connection timeout (seconds)")
parser.add_argument('-p', '--ports', nargs='+', required=True, help="The ports to be checked. Ranges can be defined with '-'")

args = parser.parse_args()

ip_or_name = args.host
ip = ""

if ip_or_name.replace(".","").isalpha():
    try: 
        ip = socket.gethostbyname(ip_or_name)
        print(f"Host IP: {ip}")
    except socket.gaierror:
        print(f"Could not resolve host '{ip_or_name}'")
else:
    ip = ip_or_name

portsgen = createPortsGenerator(args.ports)

print(f"Connecting to '{ip_or_name}'")
for port in portsgen:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(args.timeout)
        s.connect((ip,port))
        print(f"{ip}:{port} - ", end='')
        printGreen("Open")
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except socket.timeout:
        print(f"{ip}:{port} - ", end='')
        printRed("Closed")
    except socket.error as err:
        print(f"Could not create socket: {err}")

print("")