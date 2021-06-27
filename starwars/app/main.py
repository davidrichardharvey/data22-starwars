from bson.objectid import ObjectId
import pymongo
import requests
from pprint import pprint

client = pymongo.MongoClient()
sw_db = client['starwars']


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
        sw_db["starships"].drop()
        print("Starships collection already exists.")


def insert_starships():

    starships_json = request_url("https://swapi.dev/api/starships/")

    for i in starships_json["results"]:
        ss_name = i["name"]
        sw_db.starships.insert_one(i)
        print(f"Inserted document for {ss_name}")


def replace_pilot_info():
    starships = sw_db["starships"]
    characters = sw_db["characters"]

    for i in starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):
        pilot_names = []
        pilot_obj_ids = []
        if i["pilots"] != []:
            # Make list of pilot names
            for pilot in i["pilots"]:
                pilot_name = request_url(pilot)["name"]
                pilot_names.append(pilot_name)
            
            for name in pilot_names:
                pilot_obj_id = next(characters.find({"name": name}))["_id"]
                pilot_obj_ids.append(pilot_obj_id)

           
            sw_db.starships.update_one({"_id": i["_id"]}, {"$set":{"pilots": pilot_obj_ids}})



if __name__ == "__main__":
    create_starships_collection()
    insert_starships()
    replace_pilot_info()