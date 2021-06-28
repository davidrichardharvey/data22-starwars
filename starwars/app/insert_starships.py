# creating a function to insert the starships into the collection on mongodb
from starwars.app.read_starships_api import *
from starwars.app.create_starships_collection import *

starships = starwars_db["starships"]


# this function inserts all of the starships, from all 4 pages, into the new starships collection on MongoDB
def insert_starships():
    starships_json_page1 = read_starships_api_page1()
    starships_json_page2 = read_starships_api_page2()
    starships_json_page3 = read_starships_api_page3()
    starships_json_page4 = read_starships_api_page4()

    # this 'if statement' ensures that there are no duplicates added to the starships collection,
    # even if it is called multiple times
    if 'starships' in starwars_db.list_collection_names():
        starships.drop()
    # there are 4 pages of starships,
    # therefore there need to be 4 'for loops' in order to insert all of the required data.
    for starship in starships_json_page1['results']:
        starwars_db.starships.insert_one(starship)
        print("Inserted page 1 documents into starship collection")

    for starship in starships_json_page2['results']:
        starwars_db.starships.insert_one(starship)
        print("Inserted page 2 documents into starship collection")

    for starship in starships_json_page3['results']:
        starwars_db.starships.insert_one(starship)
        print("Inserted page 3 documents into starship collection")

    for starship in starships_json_page4['results']:
        starwars_db.starships.insert_one(starship)
        print("Inserted page 4 documents into starship collection")
