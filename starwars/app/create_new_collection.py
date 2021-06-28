import pymongo

client = pymongo.MongoClient()
starwars_db = client['starwars']

# This function will create the new starships collection.


def create_new_collection():
    starships = starwars_db["starships"]
    print(f"New collection {starships} has been created and added to {starwars_db}")
    return starships
