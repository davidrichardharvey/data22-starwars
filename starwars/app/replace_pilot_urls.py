from starwars.app.create_starships_collection import *
from starwars.app.pilot_api_reader import *

starships = starwars_db["starships"]
characters = starwars_db["characters"]


# this function replaces the pilot urls with the matching pilot object IDs
def replace_pilot_urls():
    # this finds all of the starships documents in the starships collection
    for starship in starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):
        # this if loop only runs for starships that have pilots
        if starship["pilots"] != []:
            # pilot_names stores a list of all of the pilot names for each starship
            pilot_names = [pilot_api_reader(pilot)["name"] for pilot in starship["pilots"]]
            # pilot_ids finds and stores the corresponding ObjectIds for the names of the pilots in each starship
            pilot_ids = [next(characters.find({"name": name}))["_id"] for name in pilot_names]
            # This updates the starships collection, replacing the urls with the corresponding pilot ObjectIDs
            starwars_db.starships.update_one({"_id": starship["_id"]}, {"$set": {"pilots": pilot_ids}})

# Here is the aggregate function to show the changes, when run in the mongodb shell,
# This matches the pilot ObjectIDs with the names of the pilots, and prints the names:

# db.starships.aggregate([
# {$lookup: {
# from: "characters",
# localField: "pilots",
# foreignField: "_id",
# as: "matched_pilot"
# }}, {$project: {name: 1, model: 1, "matched_pilot.name": 1}}
# ]).pretty()
