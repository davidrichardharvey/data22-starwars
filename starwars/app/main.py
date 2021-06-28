import pymongo
import requests

client = pymongo.MongoClient("mongodb://localhost:27017/")
sw_db = client['starwars']  # "starwars" database is set up

starships = sw_db["starships"]  # "starships" collection is set up
characters = sw_db["characters"]  # "characters" collection is set up


# Note that the "starwars" database isn't actually created until it has content

# This function sends a GET request to the specified URL
def get_url(url):
    return requests.get(url)


# This function converts the URL request into JSON format
def get_json_format(url):
    return get_url(url).json()


def create_starships_collection():
    # Create the new updated starships collection
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


# Gets function gets takes in the Star Wars API URL and converts it into json format (using get_json_format() function)
# Then all of the starship information (that is online), is inserted into the "starships" collection
def insert_starship_data():
    starships_json_format = get_json_format("https://swapi.dev/api/starships/")
    for i in starships_json_format["results"]:
        ss_name = i["name"]
        sw_db.starships.insert_one(i)
        print(f"The document for {ss_name} has been inserted")

insert_starship_data()

# Replaces the pilot URL's in "starships" collection with the ObjectId's from "characters" collection
# Note: The characters collection is populated in this function & it's contents is stored in a list

def replace_pilot_url_with_object_id():
    for i in starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):
        if i["pilots"] != []:
        # Since not all of the "starship" documents have a list of URL's (values) present in their respective "pilot" (keys)
        # This function makes sure to account for this
        # List of pilot names is made here
            pilot_names = [get_json_format(pilot)["name"] for pilot in i["pilots"]]
        # List of the pilot's ObjectId's from the "characters" collection is made here
        # Note: the "characters" collection is not actually defined as a collection within MongoDB Compass
            pilot_obj_ids = [next(characters.find({"name": name}))["_id"] for name in pilot_names]
        # Update query to change the pilots array containing urls to an array containing object
        # The "starships" collection is updated, so that the "pilot" array field is (that previously contained URL's)
        # is replaced with the corresponding "pilot" ObjectId value
            sw_db.starships.update_one({"_id": i["_id"]}, {"$set": {"pilots": pilot_obj_ids}})

# if __name__ == "__main__":
#     create_starships_collection()
#     insert_starship_data()
#     replace_pilot_url_with_object_id()

