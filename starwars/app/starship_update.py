from api_request import *
import pymongo


client = pymongo.MongoClient()
sw_db = client['starwars']
starships_api = api_call("https://swapi.dev/api/starships")
starships_json = api_store("https://swapi.dev/api/starships/")


def starships_collection():
    # Function to check for starships collection within the starwars database
    # And drop existing collection
    if sw_db.list_collection_names().__contains__('starship_demo'):
        sw_db.starship_demo.drop()
        print('Starship_demo collection dropped')
    else:
        print('Collection does not exist')


def starships_insert():
    # Function to create new starship collection insert data from the api
    if 'starship_demo' not in sw_db.list_collection_names():
        starship = sw_db['starship_demo']
        print('New Starships Collection created')
        for i in starships_json['results']:
            starship.insert_one(i)
            starship_name = i['name']
            print(starship_name)


starships_collection()
starships_insert()