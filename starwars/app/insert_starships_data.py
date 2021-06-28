import pymongo
from bson.objectid import ObjectId
from starwars.app.read_api import *


client = pymongo.MongoClient()
starwars_db = client['starwars']
starships = starwars_db["starships"]

# Function that will add the starships collection to MongoDB
def insert_starships():
    sw_starships_one = read_api_page_one()
    sw_starships_two = read_api_page_two()
    sw_starships_three = read_api_page_three()
    sw_starships_four = read_api_page_four()
    if 'starships' in starwars_db.list_collection_names(): # Stops replicating data in collections by dropping it and re-inserting
        starships.drop()
    for i in sw_starships_one['results']:
        starwars_db.starships.insert_one(i)
    for i in sw_starships_two['results']:
        starwars_db.starships.insert_one(i)
    for i in sw_starships_three['results']:
        starwars_db.starships.insert_one(i)
    for i in sw_starships_four['results']:
        starwars_db.starships.insert_one(i)

