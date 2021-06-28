import pymongo
from starwars.app.api_request import api_request
from pprint import pprint
client = pymongo.MongoClient()
db = client['starwars']


def starships_update(requested_data):
    list_of_ships = requested_data.json()["results"]
    db.starships.insert_many(list_of_ships)
    ships = db.starships.find()
    return [ship for ship in ships]



