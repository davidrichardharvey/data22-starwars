import pymongo
from api_request import *

client = pymongo.MongoClient()
db = client['starwars']


def drop_starships_collection():
    db.drop_collection('starships')


def create_starships_collection():
    starships_coll = db['starships']


def insert_starships_info():
    db['starships'].insert_many(get_all_pages_starships())
    return db['starships']


# drop_starships_collection()
# create_starships_collection()
# insert_starships_info()


def get_persons_objectid():
    people = db.characters.find()
    peoples_ids_dict = {}
    for person in people:
        persons_name = person['name']
        persons_id = person['_id']
        peoples_ids_dict[persons_name] = persons_id  # peoples_ids_dict = {persons_name: persons_id}
    return peoples_ids_dict


peoples_ids_dict = get_persons_objectid()
print(peoples_ids_dict)


def replace_url_with_name():
    for ships in db['starships'].find():
        ships_name = ships['name']
        if ships['pilots'] == []:
            pass
        else:
            new_list = []
            for pilot in ships['pilots']:
                new_list.append(people_url_dict.get(str(pilot)))
            new_dict = {'pilots': new_list}
            update = {'$set': new_dict}

            db.starships.update_one({'name': ships_name}, update)

    return db['starships']


# pilots_names_on_ships = replace_url_with_name()
# print(pilots_names_on_ships)


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

            db.starships.update_one({'name': ships_name}, update)

    return db['starships']


pilots_ids_on_ships = replace_name_with_id()
print(pilots_ids_on_ships)
