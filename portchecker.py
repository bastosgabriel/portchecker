import socket

# AF_INET: Host is a string representing either a hostname in 
# Internet domain notation like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5'
# SOCK_STREAM: The default socket type. Uses a TCP protocol connection

def printGreen(text): print(f"\033[92m {text}\033[00m") 
def printRed(text): print(f"\033[91m {text}\033[00m") 

'''
Creates a generator object with all the ports to be checked
'''
def createPortsGenerator(port_input):
    port_input_list = port_input.split(',')
    #port_list = []

    for port_input in port_input_list:
        if not ('-' in port_input):
            #port_list.append(port_input)
            yield int(port_input)
        else:
            lowest = int(port_input.split('-')[0])
            highest = int(port_input.split('-')[1])

            for port in range(lowest,highest+1):
                # port_list.append(port)
                yield port

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.settimeout(20)
    print("Socket created.\n")
except socket.error as err: 
    print(f"Socket creation failed: {err}")

print("#--------------------------------------------------------#")
print("# IP/Hostname examples:                                  #")
print("# www.google.com, 216.58.222.100                         #")
print("# Check single ports examples:                           #")
print("# 79,95,7172                                             #")
print("# For port ranges use '-':                               #")
print("# 70-90 -> will check all ports from 70 to 90 (inclusive)#")
print("#--------------------------------------------------------#\n")


while True:
    ip_or_name = input("IP/Hostname: ")
    ip = ""

    if ip_or_name.replace(".","").isalpha():
        try: 
            ip = socket.gethostbyname(ip_or_name)
            print(f"Host IP: {ip}")www.google.com
    portsgen = createPortsGenerator(input("Ports: "))

    print(f"Connecting to '{ip_or_name}'")
    for port in portsgen:
        try:
            s.connect((ip,port))
            print(f"{ip}:{port} - ", end='')
            printGreen("Open")
        except socket.error:
            print(f"{ip}:{port} - ", end='')
            printRed("Closed")
    print("")