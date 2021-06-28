import pymongo
from bson.objectid import ObjectId

# Function that will add the starships collection to MongoDB
client = pymongo.MongoClient()
starwars_db = client['starwars']
starships = starwars_db["starships"]

def add_collection():
    if 'starships' not in starwars_db.list_collection_names():
        starwars_db["starships"]
    else:
        starships.drop()
