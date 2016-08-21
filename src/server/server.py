import os
from socket import *
from pymongo import MongoClient

host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

client = MongoClient()
db = client.trolleysystem

print "Waiting to receive baycount..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    if data == "exit":
        break
    print "Received message: " + data
    if data.split(':')[0] == "REFRESH":
        result = db.bays.update_one(
            {"id": data.split(':')[2]},
            {"$set": {"stock": data.split(':')[1]}}
        )
UDPSock.close()
os._exit(0)
