import os
from socket import *
meId = raw_input("Enter my id: ")

#set id name clientside
meName = open('client-name.txt', 'w')
meName.write(meId)
meName.close()


count = 0 #number of inital trolleys

host =  open('../serverip.txt','r').read().split('\n')[0]
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
data = "INIT:"+ meId + ":" + str(count)
UDPSock.sendto(data, addr)
print meId + " initialized with " + str(count) + " trolleys"
UDPSock.close()
os._exit(0)
