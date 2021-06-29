from api_request import *
import pymongo

client = pymongo.MongoClient()
sw_db = client['starwars']

# requesting and storing all the pages of the starships data from api in json format
starships_json_page1 = api_store("https://swapi.dev/api/starships/")
starships_json_page2 = api_store("https://swapi.dev/api/starships/?page=2")
starships_json_page3 = api_store("https://swapi.dev/api/starships/?page=3")
starships_json_page4 = api_store("https://swapi.dev/api/starships/?page=4")


def starships_collection():
    # Function to check for existing starships collection within the star wars database
    # And drop any existing starships collection
    if sw_db.list_collection_names().__contains__('starships'):
        sw_db.starships.drop()
        print('starships collection dropped')
    else:
        print('starship collection does not exist')


def starships_insert():
    # Function to create new starships collection
    if 'starships' not in sw_db.list_collection_names():
        starship = sw_db['starships']
        print('New starships Collection created')

        # This section inserts each page of the starships data from the api into the starships collection
        starship_name = []
        for ship in starships_json_page1['results']:
            starship.insert_one(ship)
            starship_name.append(ship['name'])

        for ship in starships_json_page2['results']:
            starship.insert_one(ship)
            starship_name.append(ship['name'])

        for ship in starships_json_page3['results']:
            starship.insert_one(ship)
            starship_name.append(ship['name'])

        for ship in starships_json_page4['results']:
            starship.insert_one(ship)
            starship_name.append(ship['name'])

        print(starship_name)