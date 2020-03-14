import socket

# AF_INET: Host is a string representing either a hostname in 
# Internet domain notation like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5'
# SOCK_STREAM: The default socket type. Uses a TCP protocol connection

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket created.")
except socket.error as err: 
    print(f"Socket creation failed: {err}")

while True:
    ip_or_name = input("IP/Hostname: ")
    ip = ""

    if ip_or_name.replace(".","").isalpha():
        try: 
            ip = socket.gethostbyname(ip_or_name)
            print(f"Host IP: {ip}")
        except socket.gaierror:
            print(f"Could not resolve host '{ip_or_name}'")

    port = int(input("Port: "))

    try:
        s.connect((ip,port))
        print(f"{ip}:{port} - Open")
    except socket.error:
        print(f"{ip}:{port} - Closed")
