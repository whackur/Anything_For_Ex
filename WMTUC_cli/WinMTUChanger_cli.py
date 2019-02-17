import os
from subprocess import getoutput

def getIfNum():
    batcmd = 'powershell.exe \"Get-WMIObject Win32_networkadapter | Select-Object InterfaceIndex\"'
    r = getoutput(batcmd)
    r = r.split('\n') # split by line
    r2 = []
    r3 = []

    for i in r:
        for repeat in range(10):
            j = i.replace(' ','')
        r2.append(j)

    for i in r2:
        if i.isnumeric():
            r3.append(i)
    return r3

def changeReg():
    ifNums = getIfNum()
    currentValue.setText(mtu) # For Display Current Value
    for ifNum in ifNums:
        if persistent == True:
            print('netsh interface ipv4 set subinterface %s mtu=%s store=persistent' %(ifNum, mtu))
            os.system('netsh interface ipv4 set subinterface %s mtu=%s store=persistent' %(ifNum, mtu))
        else:
            print('netsh interface ipv4 set subinterface %s mtu=%s' %(ifNum, mtu))
            os.system('netsh interface ipv4 set subinterface %s mtu=%s' %(ifNum, mtu))

def initMtu():

    mtu = 1500
    persistent = True
    changeReg()

def changePersistent():
    if checkBox.isChecked():
        persistent = True
        print(persistent)
    else:
        persistent = False
        print(persistent)

mtu = input('MTU Change : ')
ifNum = getIfNum()

