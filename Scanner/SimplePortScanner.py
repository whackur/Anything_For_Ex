import socket
def checkHost(host, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))
        sock.shutdown(2)
        return "Connected"
    except:
        return "Connection Failed"

if __name__ == "__main__":
    print(checkHost("www.python.org", 80, 5))