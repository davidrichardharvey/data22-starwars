import pymongo

client = pymongo.MongoClient()
starwars_db = client['starwars']


# this function creates a starships collection in the starwars database
def create_starships_collection():
    starships = starwars_db["starships"]
    print('starships collection has been created and added to starwars_db')
    return starships

