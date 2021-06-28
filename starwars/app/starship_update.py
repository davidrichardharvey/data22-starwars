from api_request import *
import pymongo
from bson.objectid import ObjectId


client = pymongo.MongoClient()
sw_db = client['starwars']


starships_json = api_call("https://swapi.dev/api/starships/")
# chars = sw_db.characters.find({}, {'name': 1, '_id': 1})
#
# for char in chars:
#     print(char)

#delete old starship collection
