from starwars.app.read_api_starships import *
from starwars.app.create_new_collection import *

client = pymongo.MongoClient()
starships = starwars_db["starships"]
starwars_db = client['starwars']

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

