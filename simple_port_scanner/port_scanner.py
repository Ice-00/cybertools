#Ask user for ip address 
#Define a list of ports i want to scan 
# Create a loop to go through each port 
# Inside the loop try to connect to that specific port 
# if it works print that the port is open 
# close the connection and move to the next port 

import socket 
#1 SETUP
target_ip = "127.0.0.1"

print(f"Scanning Target:{target_ip}.....")

#2 The Walthrough
for port in range(1,101):
    s = socket.socket()
    s.settimeout(0.5)

    result = s.connect_ex((target_ip,port))

#3 The report 
if result == 0:
    print(f"[+]Port {port} is open")
    s.close()

print("Scan complete.")


