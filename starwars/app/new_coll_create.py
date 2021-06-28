from connect_to_mongodb import *
import bson


#  Creating a function to check if the starships collection exists, and creating a new one if it does not.
def create_coll():
    if "starships" not in db.list_collection_names():
        db.create_collection("starships")
    #  If the collection exists, this gets rid of it and creates a fresh one.
    #  This function would not be run if you only wish to append/change an existing collection.
    else:
        db.starships.drop()
        db.create_collection("starships")
