from getmac import get_mac_address
import subprocess
import threading
import socket
import os

myIp = '192.168.0.19'
NUM_THREADES = 254 # 64, 128, 254

# socket.gethostbyaddr(ip) # Net-Bios Name Query
# print(socket.gethostbyaddr(r2[4])) # Net-Bios Name Query

def ip_to_mac(myIp):
    updated_mac = get_mac_address(ip=myIp, network_request=True)
    return updated_mac


def rslt(ipRange,i):
    for idx in range(254): # Change to 254
        if i == idx % NUM_THREADES:
            batcmd = 'bin\\arp-ping.exe -x -w 3000 ' + ipRange[idx]
            result = subprocess.getoutput(batcmd)
            r = result.split('\n') # split by lines
            r2 = result.split(' ') # split by words
            if r2[0] == "Reply":
                print(r[0])
            else :
                ipRange[i] = 'nohost'


# Get ip_prefix
prefix_range = myIp.split('.')
ip_prefix = prefix_range[:3]
ip_prefix = '.'.join(ip_prefix)

ipRange = [] # Get 'Local IP Range' Array
macList = []

for idx in range(1,255):
    ipRange.append(ip_prefix + '.' + str(idx))

for i in range (NUM_THREADES):
    t = threading.Thread(target=rslt, args = (ipRange,i))
    t.start()
t.join() # waiting for thread

print('\nSearching HostName...')

for i in ipRange:
    if i is not 'nohost':
        os.system('bin\\') # http://www.unixwiz.net/tools/nbtscan.html