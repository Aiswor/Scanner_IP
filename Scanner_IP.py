import os
import ipaddress
import concurrent.futures

def hacer_ping(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f"{ip} is active")

def main():
    print("Enter the network IP: ")
    ip_red = input()

    print("Enter the mask in long format: ")
    mask = input()

    try:
        red = ipaddress.ip_network(f"{ip_red}/{mask}", strict=False)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(hacer_ping, ip) for ip in red.hosts()]
            for future in concurrent.futures.as_completed(futures):
                pass
    except ValueError as e:
        print(f"Network/mask error: {e}")

if __name__ == "__main__":
    main()
