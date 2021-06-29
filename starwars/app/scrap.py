# def replace_pilots_objectids():
#     # Replace pilots with url links with ids
#     for pilot in db.list_collection_names("starships").find({}, {"_id": 1, "name": 1, "pilots": 1}):
#         if pilot["pilots"]:
#             for pilot in pilot["pilots"]:
#                 print({pilot["name"]: pilot["pilots"]})
#                 # p_names = [response1["name"]]
# print(replace_pilots_objectids())
    # db.characterz.find({name: 1, _id: 1})
    # # for item in pilots_id:
    # #   X = pilots(_id)


# ids = next(db.starships.aggregate([{$lookup: {
# from: "characterz", local_field: "pilots", foreign_field: "_id", as: "matched_pilot"}}, {$project: {name: 1, model: 1,                                                                                              "matched_pilot.name": 1}}]))





# print(replace_pilots_ids())
# def replace_ids():
#     ships = db.starships.find()
#     pilots = [ship for ship in ships]  # ship is pilot   # ships is db.starships....
#     for pilot_list in pilots:
#         pilot_info = []
#         id_list = []
#         ship_model = pilot_list["model"]
#         pilot_urls = pilot_list["pilots"]
#         for pilot in pilot_urls:
#             pilot_info.append(requests.get(pilot).json()["name"])
#         for name in pilot_info:
#             id_list.append(db.characterz.find_one({"name": name}, {"_id": 1}))
#     return db.starships.find({"model": "Millennium Falcon"}, {"_id": 1})
#


def replace_pilots_objectids():
    # pilots_names = []
    # pilots_object_ids = []
    for ship in pilot_names:
        for pilot in ship["pilots"]:
            for char in characters_list:
                if pilot == char["name"]:
                    pilot_index = ship["pilots"].index(pilot)
                    ship["pilots"][pilot_index] = char["ObjectId"]
    #         pilots_names.append(requests.get(pilot).json()["name"])
    #         for name in pilots_names:
    #             pilots_object_ids.append(name[({"name": name}, {"_id": 1})])
    #             db.starships.update_one({"_id": pilot["_id"]}, {"$set": {"pilots": pilots_object_ids}})
    # return pilots_object_ids