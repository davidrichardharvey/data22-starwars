import pymongo
from api_request import *

client = pymongo.MongoClient()
db = client['starwars']


def drop_starships_collection():
    db.drop_collection('starships')


def create_starships_collection():
    starships_coll = db['starships']


def insert_starships_info():
    """ Insert the list of dictionaries of details for every available starship into the starships collection """
    db['starships'].insert_many(get_all_pages_starships())
    return db['starships']


def get_persons_objectid():
    people = db.characters.find()
    peoples_ids_dict = {}
    for person in people:
        persons_name = person['name']
        persons_id = person['_id']
        # peoples_ids_dict = {persons_name: persons_id, persons_name: persons_id, ...}
        peoples_ids_dict[persons_name] = persons_id
    return peoples_ids_dict


peoples_ids_dict = get_persons_objectid()


def replace_url_with_name():
    for ships in db['starships'].find():
        ships_name = ships['name']
        if ships['pilots'] == []:
            pass
        else:
            new_list = []
            for pilot in ships['pilots']:
                new_list.append(people_url_dict.get(str(pilot)))  # [pilot1_name, pilot2_name, ...]
            new_dict = {'pilots': new_list}
            update = {'$set': new_dict}

            # {'name': 'A-wing', 'pilots': ['https://swapi.dev/api/people/29/']}
            # updates to
            # {'name': 'A-wing', 'pilots': ['Arvel Crynyd']}
            db.starships.update_one({'name': ships_name}, update)

    return db['starships']


def replace_name_with_id():
    for ships in db['starships'].find():
        ships_name = ships['name']
        if ships['pilots'] == []:
            pass
        else:
            new_list = []
            for pilot in ships['pilots']:
                new_list.append(peoples_ids_dict[str(pilot)])
            new_dict = {'pilots': new_list}
            update = {'$set': new_dict}

            # {'name': 'A-wing', 'pilots': ['Arvel Crynyd']}
            # updates to
            # {'name': 'A-wing', 'pilots': [ObjectId("60d772621bc3b3961b61a88b")]}
            db.starships.update_one({'name': ships_name}, update)

    return db['starships']
