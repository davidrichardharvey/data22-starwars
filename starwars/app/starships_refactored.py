import pymongo
import requests
from multi_page_api import *

# Connect to MongoDB and select database
client = pymongo.MongoClient()
db = client["starwars"]


def drop_starship_collection():
    # Ensure collection is not duplicated
    db.starship.delete_many({})
    db.drop_collection("starship")
    print("starship collection has been dropped")


def create_starship_collection():
    # Create a starship collection
    db.create_collection("starship")
    print("starship collection has been created")


# Insert starship collection into database
# Insert all starships from API into "starship" collection
def insert_starships():
    for ship in ship_list:
        db.starship.insert_one(ship)
    print("documents inserted")


def update_pilots_urls():
    ships = db.starship.find({}, {"_id": 1, "name": 1, "pilots": 1})
    for ship in ships:
        # consider only starships with pilots value entries
        if ship["pilots"] != []:
            # make a list of pilot urls with names of pilots
            pilot_names = [requests.get(url_pilot).json()["name"] for url_pilot in ship["pilots"]]
            # make a list of character object ids for names of characters
            pilot_ids = [db.characterz.find({"name": names}).next()['_id'] for names in pilot_names]
            # update starship collection with characters objectids set in place of pilot urls
            db.starship.update_one({'_id': ship['_id']}, {"$set": {"pilots": pilot_ids}})


def run():
    url_results()
    drop_starship_collection()
    create_starship_collection()
    insert_starships()
    update_pilots_urls()

run()
