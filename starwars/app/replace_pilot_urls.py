from starwars.app.create_starships_collection import *
from starwars.app.pilot_api_reader import *

starships = starwars_db["starships"]
characters = starwars_db["characters"]


def replace_pilot_urls():
    for starship in starships.find({}, {"_id": 1, "name": 1, "pilots": 1}):
        if starship["pilots"] != []:
            pilot_names = [pilot_api_reader(pilot)["name"] for pilot in starship["pilots"]]
            pilot_ids = [next(characters.find({"name": name}))["_id"] for name in pilot_names]
            starwars_db.starships.update_one({"_id": starship["_id"]}, {"$set": {"pilots": pilot_ids}})


# Here is the aggregate function to show the changes, when run in the mongodb shell:

# db.starships.aggregate([
# {$lookup: {
# from: "characters",
# localField: "pilots",
# foreignField: "_id",
# as: "matched_pilot"
# }}, {$project: {name: 1, model: 1, "matched_pilot.name": 1}}
# ]).pretty()
