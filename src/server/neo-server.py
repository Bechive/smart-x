
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


print "Server started..."
while True:
    inputType = ""
    bayNo = ""
    trolleyNo = ""
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received(" + data +")\n"
    try:
        inputType = data.split(">")[0]
        data = (data.split(">")[1]).split("<")[0]
        if inputType == "TRIO":
            bayNo = data.split(":")[0]
            trolleyNo = data.split(":")[1]
            print "inputType="+inputType+", bayNo="+bayNo+", trolleyNo="+trolleyNo+"\n"



        if inputType == "INIT":
            bayNo = data
            print "inputType="+inputType+", bayNo="+bayNo+"\n"
            result = db.bays.insert_one(
                {
                    "id": bayNo,
                    "stock": 0
                }
            )
            result.inserted_id



    except :
        print "invalid message"
UDPSock.close()
os._exit(0)


'''
    if data.split(':')[0] == "REFRESH":
        result = db.bays.update_one(
            {"id": data.split(':')[2]},
            {"$set": {"stock": data.split(':')[1]}}
    )
    result.inserted_id
'''
