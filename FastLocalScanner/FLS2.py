from getmac import get_mac_address
import subprocess, threading
import socket, os, re
from pythonping import ping
import io
from contextlib import redirect_stdout

NUM_THREADES = 255 # 64, 128, 255
ipv4_regex = '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'


# Automate finding local ipv4 address
def getMyIp():
    myIp = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myIp = s.getsockname()[0]
    return myIp

# Input IP 
def inputIp(myIp):
    while True:
        print('Input your IP Address, press ENTER if your IP Address right ' + '[' + myIp + ']' + ' : ',end = '')
        newIp = input()
        if newIp == '':
            return myIp
        chkIpv4 = re.compile(ipv4_regex) # IPv4 Regex
        if chkIpv4.match(newIp): # Check IPv4 Regex
            return newIp

# Initialize All IP Lists
def getAllIpLists(myIp):
    prefix_range = myIp.split('.')
    ip_prefix = prefix_range[:3]
    ip_prefix = '.'.join(ip_prefix)

    allIpLists = []
    for i in range(1,255):
        allIpLists.append({'IP':ip_prefix + '.' + str(i), 'Alive':False, 'HostName':''})
    return allIpLists

# Ping Sweep Scan
def pingScan():
    for ip in range(3):
        # standard output redirect
        with io.StringIO() as buf, redirect_stdout(buf):
            doPing = ping(allIpLists[ip].get('IP'), count=1)
            print(doPing)
            output = buf.getvalue()

        r = output.split(' ') # split by space
        r = r[0:2]
        
        if r[1] == 'from':
            print(' '.join(r) + ' ' + allIpLists[ip].get('IP'))
            allIpLists[ip].update({'Alive':True})

def macScan():
    for ip in range(3):
        # standard output redirect
        with io.StringIO() as buf, redirect_stdout(buf):
            getMac = get_mac_address(ip=allIpLists[ip].get('IP'))
            print(getMac,end = '')
            output = buf.getvalue()
        if output != 'None':
            print(allIpLists[ip].get('IP') + ' has mac address ' + output)
            allIpLists[ip].update({'Alive':True})
            allIpLists[ip].update({'MAC':output})

myIp = getMyIp()
myIp = inputIp(myIp)
allIpLists = getAllIpLists(myIp)
pingScan()
macScan()

print(allIpLists)