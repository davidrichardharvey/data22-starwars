import pymongo
import requests
from pprint import pprint

client = pymongo.MongoClient()
starwars_db = client['starwars']


def create_starships_collection():
    starships = starwars_db["starships"]
    print('starships collection has been created and added to starwars_db')
    return starships


print(type(create_starships_collection()))
