import socket 

target_domain = "google.com"
sub_domains = ["admin", "test", "dev", "mail"]

for sub in sub_domains:
    full_url = sub + "." + target_domain
    print(full_url)

try:
    ip = socket.gethostbyname(full_url)
    print(f"[+] Found{full_url} -> {ip}")
    
except socket.gaierror:
    pass