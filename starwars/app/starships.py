# number of entries inputted into collection ==36
# make sure collection is empty
# As a user I want to replace all "pilots" keys with a list of ObjectIDs from characters collection
# return all pilots keys
# get all ObjectIDs
# create a list of ObjectIDs form characters collection
from starwars.app.api_call import *


# Drop starships collection
def current_collection_drop():
    db.drop_collection("starships")
    # print("collection, starships has been dropped")

# Check if starships collection exists
def create_starship_collection():
    if "starships" not in db.list_collection_names():
        starship_collection = db.create_collection("starships")
        print("starship collection has been created")


# [{}, {}, {}]
# Insert all starships into "starship" collection
def insert_starship():
    # for result in
    db.starships.insert_many(data_list)
    return db["starships"]


characters_names = db.characterz.find({}, {"name": 1, "_id": 1})
pilot_names = db.starships.find({}, {"_id": 1, "name": 1, "pilots": 1})
characters_list = []


# Replace only available starships with pilots
def replace_pilots_character_name():
    for characters in characters_names:
        characters_list.append(characters)
        # pilot_names = db.starships.find({}, {"_id": 1, "name": 1, "pilots": 1})
        for ship in pilot_names:
            if ship["pilots"] != []:
                for url in ship["pilots"]:
                    pilots_name = api_call(url).json()["name"]
                    pilot_index = ship["pilots"].index(url)
                    ship["pilots"][pilot_index] = pilots_name


# Replace each pilot urls with character object ids
def replace_pilots_objectids():
    # pilots_names = []
    # pilots_object_ids = []
    for ship in pilot_names:
        for pilot in ship["pilots"]:
            for char in characters_list:
                if pilot == char["name"]:
                    pilot_index = ship["pilots"].index(pilot)
                    ship["pilots"][pilot_index] = char["ObjectId"]
    #         pilots_names.append(requests.get(pilot).json()["name"])
    #         for name in pilots_names:
    #             pilots_object_ids.append(name[({"name": name}, {"_id": 1})])
    #             db.starships.update_one({"_id": pilot["_id"]}, {"$set": {"pilots": pilots_object_ids}})
    # return pilots_object_ids


# main file
def update():
    current_collection_drop()
    create_starship_collection()
    insert_starship()
    replace_pilots_character_name()
    replace_pilots_objectids()
    collection = db.starships
    print(collection)


print(update())



