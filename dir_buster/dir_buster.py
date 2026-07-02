import requests

target_url = "http://httpbin.org"
directories = ["admin", "hidden", "status", "html"]

for word in directories:
    # Glue the target website and the directory word together with a slash
    full_url = target_url + "/" + word
    
    # Send the web request
    response = requests.get(full_url)
    
    # Check the response (Indented inside the loop!)
    if response.status_code == 200:
        print(f"[+] Found page: {full_url}")
    else:
        print(f"[-] Not found: {full_url}")