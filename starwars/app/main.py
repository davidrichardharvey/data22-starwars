from bson.objectid import ObjectId
import pymongo
import requests
from pprint import pprint

client = pymongo.MongoClient()
sw_db = client['starwars']
starships = sw_db["starships"]   # starwars.starships
characters = sw_db["characters"] # starwars.characters


def request_url(url):
    # Quick way to get api from url into json format
    return requests.get(url).json()


def create_starships_collection():
    # Create the new updated starships collection
    if "starships" not in sw_db.list_collection_names():
        sw_db["starships"]
        print("Starships collection has been created.")
    else:
        # Drop the collection so that it is remade in the next stage, this avoids data duplication
        starships.drop()
        print("Starships collection already exists.")


def insert_starships():
    # Gets starship information from the starwars api url and inserts into starships collection
    starships_json = request_url("https://swapi.dev/api/starships/")

    for i in starships_json["results"]:
        ss_name = i["name"]
        sw_db.starships.insert_one(i)

        print(f"Inserted document for {ss_name}")


def replace_pilot_info():
    # Replaces the pilot urls in starships with object ids from characters
    for i in starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):
        if i["pilots"] != []:
            # Make list of pilot names
            pilot_names = [request_url(pilot)["name"] for pilot in i["pilots"]]
            # Make a list of the pilot object ids from the characters collection
            pilot_obj_ids = [next(characters.find({"name": name}))["_id"] for name in pilot_names]
            # Update query to change the pilots array containing urls to an array containing object ids
            sw_db.starships.update_one({"_id": i["_id"]}, {"$set":{"pilots": pilot_obj_ids}})

            print("Pilots {0} have been updated for the {1} starship".format(", ".join(pilot_names), i["name"]))


def run():
    create_starships_collection()
    insert_starships()
    replace_pilot_info()

if __name__ == "__main__":
    run()