from starships_import import *
from api_req import *
from pprint import pprint


characters_pilot_query = db['characters'].find({}, {"name": 1, "_id": 1})
chars_list = []


def pilot_and_ids():
    for chars in characters_pilot_query:
        chars_list.append(chars)


#  Some ships did not have a pilot url listed, and instead returns an empty list.
#  This means that the pilot data must be filtered by non-empty lists (!= []) as it's quicker than changing the empty
#  lists to null and using $ne: null with pymongo.
def change_url_to_name():
    for ship in db.starships.find({}, {"name": 1, "pilots": 1, "_id": 1}):
        if ship['pilots'] != []:
            for pilot in ship['pilots']:
                pilot_name = req_api(pilot).json()['name']
                pilot_index = ship['pilots'].index(pilot)
                ship['pilots'][pilot_index] = pilot_name


def change_name_to_objectid():
    for ship in db.starships.find({}, {"name": 1, "pilots": 1, "_id": 1}):
        for pilot in ship['pilots']:
            for dict in chars_list:
                # for name, objectID in dict:
                if pilot == dict['name']:
                    pilot_index = ship['pilots'].index(pilot)
                    ship['pilots'][pilot_index] = dict['ObjectId']


def pilot_info_update():
    pilot_and_ids()
    change_url_to_name()
    change_name_to_objectid()
    results = db['starships']
    print(results)


# _____________________________________________________________________________________
# UNUSED CODE FOR FUTURE REFERENCE.
# _____________________________________________________________________________________

# db.starships.find({}, {'_id': 0})

# api_pilot_query = db["starships"].find({}, {"name": 1, "pilots": 1, "_id": 0})
# api_pilot_info = []
# characters_info = []

# if data_to_import['pilots']:

# pilot_urls = data_to_import['pilots']


# for ship in data_to_import:
#     for pilot in ship["pilots"]:
#         db.starships.update(
#             {pilot.name: '' }
#         )

# for ship in api_pilot_query:
#     for pilot in ship["pilot"]:
#         api_pilot_info = [req_api('https://swapi.dev/api/starships/')['name']]
#
# for pilot_info in characters_pilot_query:
#     for name in pilot_info:
#         characters_info = [next()]

# match api_pilot_query name with characters_pilot_query name
