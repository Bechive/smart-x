from pymongo import MongoClient


client = MongoClient()

db = client['trolleysystem']
#db = client.trolley-system ###for existing db

bays = db['bays']
#bays = db.bays  ###for existing collection

result = db.bays.insert_many([
        {
                "id": "ABCDEF",
                "stock": 0
        },
        {
                "id": "FEDCBA",
                "stock": 2
        }
    ]
)

result.inserted_ids
