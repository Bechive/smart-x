import os
from socket import *
from uuid import getnode
meId = str(getnode())
count = 0;
host =  open('../serverip.txt','r').read().split('\n')[0]
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
