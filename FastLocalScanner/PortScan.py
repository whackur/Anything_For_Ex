# This script runs on Python 3
import socket, threading


def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output.append(port_number)
        TCPsock.close()
    except:
        output[port_number] = ''



def scan_ports(host_ip, delay):

    threads = []        # To run TCP_connect concurrently
    output = []         # For printing purposes
    ports = [20,21,22,23,25,53,80,135,443,445,3306,3389,8080]            # Port Lists



    # Spawning threads to scan ports
    for i in ports:
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(len(ports)):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(len(ports)):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(len(ports)):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])



def main():
    host_ip = input("Enter host IP: ")
    # delay = int(input("How many seconds the socket is going to wait until timeout: "))   
    delay = 200 # ms
    scan_ports(host_ip, delay)

if __name__ == "__main__":
    main()