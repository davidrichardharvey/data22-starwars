import pymongo

client = pymongo.MongoClient()


def drop_collection(collection_name):
    db = client["starwars"]
    newcol = db[collection_name]
    newcol.drop()


def create_new_collection(collection_name):
    db = client["starwars"]
    newcol = db[collection_name]
    return newcol


def add_to_collection(newcol, list_of_documents):
    return newcol.insert_many(list_of_documents)


