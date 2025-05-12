import socket
import re
import ipaddress
port_range_pattern=re.compile("([0-9]+)-([0-9]+)")
min_port=0
max_port=60000
openp=[]
while True:
    ip_add=input("\nEnter the ip address that is to be scanned:")
    try:
        ip_obj=ipaddress.ip_address(ip_add)
        print("VALID IP")
        break
    except:
        print("INVALID IP")

while True:
    print("Enter the range of port: (Eg: 10-120)")
    port_range=input("Enter the range to be scanned:")
    port_range_valid=port_range_pattern.search(port_range.replace(" ",""))

    if port_range_valid:
        min_port=int(port_range_valid.group(1))
        max_port=int(port_range_valid.group(2))
        break
for port in range(min_port,max_port+1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add,port))
            openp.append(port)
    except:
        pass

for port in openp:
    print(f"Port {port} is open on {ip_add}.")

print("Scan Complete")
input("Press Enter to exit...")
