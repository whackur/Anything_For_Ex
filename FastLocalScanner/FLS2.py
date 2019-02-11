from getmac import get_mac_address
import subprocess
import threading

myIp = '192.168.0.19'
NUM_THREADES = 254 # 64, 128, 254

def ip_to_mac(myIp):
    updated_mac = get_mac_address(ip=myIp, network_request=True)
    return updated_mac

def rslt(ipRange,i):
    for idx in range(254): # Change to 254
        if i == idx % NUM_THREADES:
            macAddr = ip_to_mac(ipRange[idx])
            if macAddr != None:
                print(ipRange[idx] + " : " + str(macAddr))

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