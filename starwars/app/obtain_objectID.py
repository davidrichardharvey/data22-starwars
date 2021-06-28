import pymongo

client = pymongo.MongoClient()
db = client["starwars"]


def obtain_object_id():
    objectID = []
    people = db.characters.find()
    for person in people:
        objectID.append(person["_id"])
    return objectID


def obtain_character_name():
    character_name = []
    people = db.characters.find()
    for person in people:
        character_name.append(person["name"])
    return character_name


def create_character_dict(character_name, objectID):
    character_dict = {character_name()[i]: objectID()[i] for i in range(len(character_name()))}
    return character_dict


