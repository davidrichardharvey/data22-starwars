# create a function that adds the starships collection once and only once
import pymongo
import requests
from pprint import pprint

client = pymongo.MongoClient()
starwars_db = client['starwars']
starships = starwars_db["starships"]  # starships collection
characters = starwars_db["characters"]  # characters collection


def create_starships_collection():
    print('starships collection has been created and added to starwars_db')
    return starwars_db["starships"]


create_starships_collection()
