import os
from socket import *
from uuid import getnode

#get client name
meName = open('client-name.txt', 'r')
meId = meName.read()
meName.close()

#get host ip
meHost = open('../serverip.txt','r')
host =  meHost.read().split('\n')[0]
meHost.close()

port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input("enter bay count: ")
    if data == "exit":
        break
    data = "REFRESH:" + data + ":" + meId
    UDPSock.sendto(data, addr)
UDPSock.close()
os._exit(0)
