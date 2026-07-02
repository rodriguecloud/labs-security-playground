import os

def ping_host():
    """
    This function takes a host address as input and attempts to ping it.
    VULNERABILITY: Uses os.system with direct string concatenation.
    """
    host = input("Enter the host address to ping: ")
    
    # SECURITY RISK: An attacker can inject arbitrary commands using ';' or '&&'
    # Malicious input example: "8.8.8.8; cat /etc/passwd"
    command = "ping -c 1 " + host
    
    print(f"Executing: {command}")
    # os.system passes the string directly to the system shell
    os.system(command)

if __name__ == "__main__":
    ping_host()
