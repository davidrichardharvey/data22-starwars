from starwars.app.api_call import *
from starwars.app.api_call import *


def replace_pilots_ids():
    # Replace pilots with links with ids
    for pilot in starships.find({}, {"name": 1, "pilots": 1, "_id": 1}):

    db.characterz.find({name: 1, _id: 1})
    # for item in pilots_id:
    #   X = pilots(_id)
ids = next(db.starships.aggregate([{$lookup: {from: "characterz", local_field: "pilots", foreign_field: "_id", as: "matched_pilot"}}, {$project: {name: 1, model: 1, "matched_pilot.name": 1}}]))
