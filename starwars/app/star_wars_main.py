from starwars.app.update_starships_collection import *
from starwars.app.read_api_pilot import *
import pymongo
import requests

# from pprint import pprint

client = pymongo.MongoClient()
starwars_db = client['starwars']
starships = starwars_db["starships"]
characters = starwars_db["characters"]

# This function will take the information from the starships collection.


def read_api_pilot(url):
    response = requests.get(url)
    return response.json()


# These functions request from the API all 4 pages of the starships collection. Then displays the data in JSON format.


def read_api_page_one():
    response_page1 = requests.get("https://swapi.dev/api/starships")
    return response_page1.json()


def read_api_page_two():
    response_page2 = requests.get("https://swapi.dev/api/starships/?page=2")
    return response_page2.json()


def read_api_page_three():
    response_page3 = requests.get("https://swapi.dev/api/starships/?page=3")
    return response_page3.json()


def read_api_page_four():
    response_page4 = requests.get("https://swapi.dev/api/starships/?page=4")
    return response_page4.json()


# pprint(read_api_page_one())
# pprint(read_api_page_two())
# pprint(read_api_page_three())
# pprint(read_api_page_four())

# This function will create the new starships collection.


def create_new_collection():
    starships = starwars_db["starships"]
    print(f"New collection {starships} has been created and added to {starwars_db}")
    return starships


# This function will allow for starships to be updated into the new collection using the data that has been extracted.


def update_starships():
    star_wars_starships_one = read_api_page_one()
    star_wars_starships_two = read_api_page_two()
    star_wars_starships_three = read_api_page_three()
    star_wars_starships_four = read_api_page_four()

    if "starships" not in starwars_db.list_collection_names():
        for s in star_wars_starships_one["results"]:
            starwars_db.starships.insert_one(s)
            print("Page 1 documents inserted into collection.")

        for s in star_wars_starships_two["results"]:
            starwars_db.starships.insert_one(s)
            print("Page 2 documents inserted into collection.")

        for s in star_wars_starships_three["results"]:
            starwars_db.starships.insert_one(s)
            print("Page 3 documents inserted into collection.")

        for s in star_wars_starships_four["results"]:
            starwars_db.starships.insert_one(s)
            print("Page 4 documents inserted into collection.")

    else:
        starships.drop()


def update_pilot_url():
    for starship in starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):
        if starship["pilots"]:
            pilot_names = [read_api_pilot(pilot)["name"] for pilot in starship["pilots"]]
            pilot_ids = [next(characters.find({"name": name}))["_id"] for name in pilot_names]
            starwars_db.starships.update_one({"_id": starship["_id"]}, {"$set": {"pilots": pilot_ids}})


def run():
    create_new_collection()
    update_starships()
    update_pilot_url()


if __name__ == "__main__":
    run()
