#this needs to modify the count
from pymongo import MongoClient

client = MongoClient()
db = client.trolleysystem

result = db.bays.update_one(
    {"id": "ABCDEF"},
    {"$set": {"stock": 10}}
)

print result.matched_count
