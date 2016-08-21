import os
from socket import *
meId = "ABCDEF"
host = "127.0.0.1" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("enter bay count: ")
    data = "" + data + meId
    UDPSock.sendto(data, addr)
    if data == ("exit:" + meId):
        break
UDPSock.close()
os._exit(0)

#to test a branch
