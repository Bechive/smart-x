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

count = int(raw_input("How many bays: "))
i = 0

print "Waiting to receive bays..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    if data.split(':')[0] == "INIT":
        result = db.bays.insert_one(
            {
                "id": data.split(':')[1],
                "stock": data.split(':')[2]
            }
        )
        result.inserted_id

    print "Received message: " + data
    i = i + 1
    if i == count:
        break
UDPSock.close()
os._exit(0)
