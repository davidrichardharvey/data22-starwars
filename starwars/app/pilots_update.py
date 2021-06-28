import pymongo
import requests
from pprint import pprint

client = pymongo.MongoClient()
db = client['starwars']


def pilots_update():
    ships = db.starships.find()
    pilots = [ship for ship in ships]
    for pilot_list in pilots:
        pilot_info = []
        id_list = []
        ship_model = pilot_list["model"]
        pilot_urls = pilot_list["pilots"]
        for pilot in pilot_urls:
            pilot_info.append(requests.get(pilot).json()["name"])
        for name in pilot_info:
            id_list.append(db.characters.find_one({"name": name}, {"_id": 1}))
        db.starships.update_one({"model": ship_model}, {"$set": {"pilots": id_list}})
    return db.starships.find({"model": "Twin Ion Engine Advanced x1"}, {"_id": 1})
