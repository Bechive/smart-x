import os
from pymongo import *
from pymongo import MongoClient

client = MongoClient()
db = client.testlands

cursor = db.cider.find({"trolley": "trolleyuno", "out": "x"})

print cursor.count()



print cursor[cursor.count() - 1]
'''
for document in cursor:
    print document
'''
if cursor.count() == 1:
    print "true"
