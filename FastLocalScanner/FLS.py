# pyinstaller.exe --uac-admin --onefile -w --add-binary "bin/arp-ping.exe;arp-ping.exe" --add-binary "bin/nbt.exe;nbt.exe" --clean -c FLS.py
from getmac import get_mac_address
import subprocess
import threading
import socket
import os
import re

NUM_THREADES = 255 # 64, 128, 255
ipv4_regex = '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'


# Automating find local ipv4 address
myIp = ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIp = s.getsockname()[0]


print('Fast Local Scanner (v1.0) Made by Whackur')

# Input IP Address
while True:
    if myIp is not '':
        print('Input your IP Address, press ENTER if your IP Address right ' + '[' + myIp + ']' + ' : ',end = '')
        newIp = input()
        chkIpv4 = re.compile(ipv4_regex) # IPv4 Regex
        if chkIpv4.match(newIp):
            myIp = newIp
            break
        elif newIp is '':
            break
    else :
        myIp = input('Input your IP Address : ',end = '')
        if chkIpv4.match(myIp):
            break

# ip to mac address
# def ip_to_mac(myIp):
#     updated_mac = get_mac_address(ip=myIp, network_request=True)
#     return updated_mac

# ARP Request Scan
def arpScan(ipRange,i):
    for idx in range(254): # [0] ~ [253]
        if i == idx % NUM_THREADES:
            batcmd = 'bin\\arp-ping.exe -x -n 1 -w 3000 ' + ipRange[idx]
            result = subprocess.getoutput(batcmd)
            r = result.split('\n') # split by line
            r2 = result.split(' ') # split by word
            if r2[0] == "Reply":
                ipRange[i] = ipRange.append('alive')
                print(r[0])
            else:
                ipRange[i] = ipRange.append('nohost')
            

def icmpRequestScan(ipRange,i):
    for idx in range(254): # [0] ~ [253]
        if i == idx % NUM_THREADES:
            batcmd = 'ping -n 1 ' + ipRange[idx]
            result = subprocess.getoutput(batcmd)
            r = result.split('\n') # split by line
            r2 = result.split(' ') # split by word
            if result[:2] != "),":
                ipRange[i] = ipRange.append('alive')
                print(r[0])
            else:
                ipRange[i] = ipRange.append('nohost')
            

# Get ip_prefix
prefix_range = myIp.split('.')
ip_prefix = prefix_range[:3]
ip_prefix = '.'.join(ip_prefix)

ipRange = [] # Get 'Local IP Range' Array
ipRangeAlive = []
for idx in range(1,255):
    ipRange.append(ip_prefix + '.' + str(idx))
for idx in range(1,255):
    ipRangeAlive.append('alive')



# Threads Array
scanThreads = []
scanThreads2 = []

# ARP Request Threads
for i in range (1, 255): # IP Range 1 ~ 254
    t = threading.Thread(target=arpScan, args = (ipRange,i))
    scanThreads.append(t)

# Start ARP Request Threads
for t in scanThreads:
    t.start()

# Waiting for ARP Request Threads
for t in scanThreads:
    t.join() 

# ICMP Request Threads
for i in range (1, 255): # IP Range 1 ~ 254
    t2 = threading.Thread(target=icmpRequestScan, args = (ipRange,i))
    scanThreads2.append(t2)

# Start Threads
for t2 in scanThreads2:
    t2.start()

# Waiting for Threads
for t2 in scanThreads2:
    t2.join() 




print('\nSearching HostName...')

for i in ipRange:
    if i is not 'nohost':
        os.system('bin\\nbt.exe -f ' + i)

enter = input('Scan Finished!!')