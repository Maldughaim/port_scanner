import socket
from _datetime import datetime

def greating():
    ip = input('Enter target ip: ')
    option = int(input('1.to scan port range\n2.to scan specific port numbers\n0.to exit\n'))
    ports = []
    if option == 1:
        while True:
            f = int(input('Enter the first port: '))
            l = int(input('Enter the last port: '))
            if f in range(0, 65536, 1) and l in range(0, 65536, 1) and f < l:
                break
            print("Invalid range")

        for i in range(f, (l+1)):
            ports.append(i)

        portscan(ip,ports)

    elif option == 2:
        p = 0

        while True:
            p = int(input('Enter port number: '))
            if p in range(0, 65536, 1):
                ports.append(p)
                break

            print('Invalid input')

        portscan(ip,ports)

    elif option == 0:
        exit(0)

    else:
        print('Invalid input')
        greating()


def portscan(ip, ports):
    try:
        print(f'Scanning {ip} at {datetime.now()}')

        for port in ports:
            sock = socket.socket()
            sock.settimeout(1)
            res = sock.connect_ex((ip,port))

            if res == 0:
                print(f'port {port} is open     |    {datetime.now()}')

            sock.close()

    except socket.error:
        print("Could not connect to the server")

greating()
