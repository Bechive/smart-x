from pymongo import MongoClient

client = MongoClient()

db = client['trolleysystem']
bays = db['bays']
