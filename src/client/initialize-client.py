import os
from socket import *
meId = raw_input("Enter my id: ")
count = 0;
#host = "127.0.0.1" # set to IP address of target computer
host =  open('../serverip.txt','r').read().split('\n')[0]
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
data = "INIT:"+ meId + ":" + str(count)
UDPSock.sendto(data, addr)
print meId + " initialized with " + str(count) + " trolleys"
