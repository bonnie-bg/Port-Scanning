#! /bin/python3
import socket
from IPy import IP

# scan ip addresses
def Scan(target, port_num):
    coverted_ip = check_ip(target)
    print("\n" + "[-_0 Scanning Target] " + str(target))
    for port in range(1, port_num):
        Scan_Port(coverted_ip, port)


# convert domain name to ip address
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        # return ip address of domain name
        return socket.gethostbyname(ip)


# return information from port in bits encoded decoded sa banner.decode()
def Get_banner(s):
    return s.recv(1024)


# scan ports
def Scan_Port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeoutet(0.5)
        socket.connect((ipaddress, port))
        # to retive information from port number opened
        try:
            banner = Get_banner(sock)
            print("[+] Port" + str(port) + " : " + str(banner.decode().strip("\n")))
        except:
            print("[+] Port" + str(port))
    except:
        # """print("[-] Port' + str(port) +' is Closed")"""
        pass


if __name__ == "__main__":
    # run if only portScanner run
    targets = input(
        "[+] Enter IP address Of Terget/s To scan (split multiple targets with ,): "
    )
    port_num = int(input("[+] Enter port range number to scan : "))
    if "," in targets:
        for ip_add in targets.split(","):
            Scan(ip_add.strip(""), port_num)

    else:
        Scan(targets, port_num)
