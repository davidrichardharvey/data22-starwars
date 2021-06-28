import pymongo

client = pymongo.MongoClient()
db = client['starwars']


# drops any existing collections called starships to avoid repeats
def drop_startships():
    db.starships.drop()


# creates starships
def create_starships_collection():
    starships = db["starships"]
    return starships


# updates startships collection with updated data
def update_starships_collection(data):
    db.starships.insert(data)
