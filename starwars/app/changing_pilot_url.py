from starwars.app.insert_starships_data import *
from starwars.app.read_api import *
from starwars.app.pilot_api_reader import *


characters = starwars_db['characters']

# Function that will change the url for pilots into their Object Ids
def change_pilot_url():
    for starship in starwars_db.starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):  #looks for all starships in the starships collection
        if starship["pilots"] != 0:
            pilot_names = [pilot_api_reader(pilot)["name"] for pilot in starship["pilots"]]  # for each pilot in each starship, able to make a list of each pilot's name
            pilot_object_ids = [next(starwars_db.characters.find({"name": name}))["_id"] for name in pilot_names]  # form each pilot in the list of names, finds the object id of that pilot
            starwars_db.starships.update_one({"_id": starship["_id"]}, {"$set": {"pilots": pilot_object_ids}}) # updates the collection to replace the pilot url with respective Object Id
