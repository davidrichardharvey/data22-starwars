# creating a function to insert the starships into the collection on mongodb
from read_starships_api import *
from create_sharships_collection import *


def insert_starships():
    starships_json_page1 = read_starships_api_page1()
    starships_json_page2 = read_starships_api_page2()
    starships_json_page3 = read_starships_api_page3()
    starships_json_page4 = read_starships_api_page4()

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

insert_starships()
