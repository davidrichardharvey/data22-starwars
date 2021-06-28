import pymongo
import requests
import sys

client = pymongo.MongoClient("mongodb://localhost:27017/")
sw_db = client['starwars']  # "starwars" database is set up

starships = sw_db["starships"]  # "starships" collection is set up
characters = sw_db["characters"]  # "characters" collection is set up


# Note that the "starwars" database isn't actually created until it has content

# This function sends a GET request to the specified URL
def get_url(url):
    return requests.get(url)


# This function converts the URL request into a JSON format (dictionary in Python --> key:value pairs)

def get_json_format(url):
    return get_url(url).json()


# This function is responsible for updating & populating the "starwars" collection
def create_starships_collection():
    # If the term "starships" is not one of the collection names in the starwars database
    # Then, create a new collection called "starships" in the "starwars" database
    if "starships" not in sw_db.list_collection_names():
        sw_db["starships"]
        print("The starships collection has been created.")
        # If there's already a collection called "starships" in the "starwars" database
        # drop that existing collection. This is to avoid data duplication in later stages
    else:
        starships.drop()
        print("The starships collection already exists.")


# This function gets takes in the Star Wars API URL and converts it into json format (using get_json_format() function)
# Then all of the starship information (that is online), is inserted into the "starships" collection
def insert_starships_data():
    starships_json_format = get_json_format("https://swapi.dev/api/starships/")
    for i in starships_json_format["results"]:  # The documents are extracted from the "results" array
        ss_name = i["name"]
        sw_db.starships.insert_one(i)
        # A single document is inserted into the "starships" collection, one after the other
        print(f"The document for {ss_name} has been inserted")


# This the function insert_starships_data() is run at this stage
insert_starships_data()


# Replaces the pilot URL's in "starships" collection with the ObjectId's from "characters" collection
# Note: The characters collection is populated in this function & it's contents is stored in a list

# Since not all of the "starships" documents have a list of URL's (values) present
# in their respective "pilot" (keys)
# This function makes sure to account for this
def replace_pilot_url_with_object_id():
    for i in starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):
        # This if statement ignores documents with empty "pilot" keys
        if i["pilots"]:
            # List of pilot names is made here
            pilot_names = [get_json_format(pilot)["name"] for pilot in i["pilots"]]
            # List of the pilot's ObjectId's from the "characters" collection is made here
            # Note: the "characters" collection is not actually defined as a collection within MongoDB Compass
            pilot_obj_ids = [next(characters.find({"name": name}))["_id"] for name in pilot_names]
            # Update the existing "starships" collection to change the pilots array containing urls
            # to an array containing object
            # The "starships" collection is updated, so that the
            # "pilot" array field is (that previously contained URL's)
            # is replaced with the corresponding "pilot" ObjectId value
            sw_db.starships.update_one({"_id": i["_id"]}, {"$set": {"pilots": pilot_obj_ids}})


# This function takes in all the function's needed to carry out the ETL process needed
# to complete the Star Wars mini project

def run_entire_main():
    create_starships_collection()
    insert_starships_data()
    replace_pilot_url_with_object_id()


# By including sys.exit() method, this stops a StopIteration error from occurring
sys.exit()
