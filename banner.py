import pyfiglet
import requests

# Print banner
text = "Injection Checker"
banner = pyfiglet.figlet_format(text)
print(banner)

# Print menu
print("1: SQL Injection Checker")
print("2: XSS Injection Checker")
print("3: Command Injection Checker")

# Take user input for choice
x = input("Enter your choice [1/2/3]: ")

# SQL Injection Checker
if x == '1':
    url = input("[+] Enter the target URL: ")
    print("URL entered: ", url)

    # Payload for SQL injection
    payloads = ["admin' 1=1 or 1' "]

    for payload in payloads:
        modified_url = url + payload
        response = requests.get(modified_url)
        
        if response.status_code == 200:
            print("[+] Target URL is not vulnerable to SQL injection")
        else:
            print("[!] Target URL is vulnerable to SQL injection")

# XSS Injection Checker
elif x == '2':
    url = input("[+] Enter the target URL: ")
    print("URL entered: ", url)

    # Payload for XSS injection
    payloads = ["<script>alert('xss')</script>"]

    for payload in payloads:
        modified_url = url + payload
        response = requests.get(modified_url)
        
        if response.status_code == 200:
            print("[+] Target URL is not vulnerable to XSS injection")
        else:
            print("[!] Target URL is vulnerable to XSS injection")

# Command Injection Checker
elif x == '3':
    url = input("[+] Enter the target URL: ")
    print("URL entered: ", url)

    # Payload for Command injection
    payloads = ["/dir", "/ipconfig"]

    for payload in payloads:
        modified_url = url + payload
        response = requests.get(modified_url)
        
        if response.status_code == 200:
            print("[+] Target URL is not vulnerable to Command injection")
        else:
            print("[!] Target URL is vulnerable to Command injection")
else:
    print("Invalid choice")	
