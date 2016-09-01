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

    data = raw_input("enter input: ")
    #bay = raw_input("enter bay: ")
    #trolley = raw_input("enter trolley: ")
    if data == "exit":
        break
    #data = "TRIO>" + bay + ":" + trolley + "<"
    UDPSock.sendto(data, addr)
UDPSock.close()
os._exit(0)
