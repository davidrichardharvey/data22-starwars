import pymongo
import requests
from pprint import pprint

get_api = requests.get("https://swapi.dev/api/")

client = pymongo.MongoClient()
sw_db = client['starwars']


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

    starships_json = requests.get("https://swapi.dev/api/starships/").json()

    for i in starships_json["results"]:
        ss_name = i["name"]
        sw_db.starships.insert_one(i)
        print(f"Inserted document for {ss_name}")


if __name__ == "__main__":
    create_starships_collection()
    insert_starships()