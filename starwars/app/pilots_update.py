import pymongo
import requests

client = pymongo.MongoClient()
db = client['starwars']


def pilots_update():
    # Finds ship data and iterates over it
    ships = db.starships.find()
    pilots = [ship for ship in ships]
    for pilot_list in pilots:
        pilot_info = []
        id_list = []
        # Pulls ship model to identify by later
        ship_model = pilot_list["model"]
        # Pulls urls to request data from
        pilot_urls = pilot_list["pilots"]
        for pilot in pilot_urls:
            # Pulls pilot information
            pilot_info.append(requests.get(pilot).json()["name"])
        for name in pilot_info:
            # Finds pilots object id
            id_list.append(db.characters.find_one({"name": name}, {"_id": 1}))
        # Sets the pilot field to the object id of the pilots
        db.starships.update_one({"model": ship_model}, {"$set": {"pilots": id_list}})
    return db.starships.find({"model": "Twin Ion Engine Advanced x1"}, {"_id": 1})
