from collections import defaultdict
import os
from pymongo import *
from pymongo import MongoClient
import datetime

'''
makeCollection
addElement - collection, element
printOutCollection - collection
printOutDb
incorrectInp
exit

####COMMANDS FOR MONGO SHELL
show dbs
use <db>
db.dropDatabase()
db.<collection>.find()
'''
client = MongoClient()
db = client.testlands

###TEST PLACE###
print "cidddder" in db.collection_names()
#print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
###TEST PLACE###

def printInstruct():
    print("mc - make collection\nae - add element\npo - print out\npoc - nprint out collection\nexit")


def makeCollection():
    print("make collection")
    bayId = raw_input("bay id>")
    collection = db[bayId]
    result = collection.insert_one(
    {
        "trolley": "null",
        "in": "null",
        "out": "null"
    }
    )
    result.inserted_id

def addElement():
    print("adding element")
    bayId = raw_input("bayId id>")

    if not bayId in db.collection_names(): #check if bayId exists
        print("not a valid bay")
        return


    trolleyId = raw_input("trolley id>")
    collection = db[bayId]

    cursor = db[bayId].find({"trolley": trolleyId, "out": "x"})

    print cursor.count()
    toIn = (cursor.count() == 0)
    print toIn
    cursor.close()
    if toIn: #if the trolley doesn't exist or has an end date
        result = collection.insert_one(
        {
            "trolley": trolleyId,
            "in": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "out": "x"
        }
        )
        result.inserted_id

    if toIn == False : #if the trolley exist and it  doesn't have an end date
        result = collection.update_one(
            {"trolley": trolleyId, "out": "x"},
            {"$set": {"out": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
        )

def printOutCollection():
    #TODO
    print("print collection")
    print  db.getCollections()

def printOutDb():
    #TODO
    print("print db")

def incorrectInp():
    print("Invalid input")

def exit():
    os._exit(0)

options = {"mc": makeCollection,
    "ae": addElement,
    "po": printOutDb,
    "poc": printOutCollection,
    "exit": exit}

options = defaultdict(lambda: incorrectInp, options)

while True:
    printInstruct()
    inp = raw_input("Next>")
    print("\n")
    options[inp]()
    print("\n")
