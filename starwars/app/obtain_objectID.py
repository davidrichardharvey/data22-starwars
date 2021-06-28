import pymongo

# Below code allows the use of the starwars database from mongoDB, also you need to ensure you have the mongo deamon running
client = pymongo.MongoClient()
db = client["starwars"]


# function to obtain objectID of characters from the characters collection in mongoDB and put them in a list
def obtain_object_id():
    objectID = []
    people = db.characters.find()
    for person in people:
        objectID.append(person["_id"])
    return objectID


# function to obtain name of characters from the characters collection in mongoDB and put them in a list
def obtain_character_name():
    character_name = []
    people = db.characters.find()
    for person in people:
        character_name.append(person["name"])
    return character_name


# function to create a dictionary with character names as keys and objectID's as values
def create_character_dict(character_name, objectid):
    character_dict1 = {character_name[i]: objectid[i] for i in range(len(character_name))}
    return character_dict1



