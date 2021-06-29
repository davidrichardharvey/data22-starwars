from starship_coll import *


def update_pilot_information():
    # Function to update the pilot url with the required ObjectId from the characters collection
    ships = sw_db.starships.find({}, {'name': 1, '_id': 0, 'pilots': 1})

    # Loop to check for starships with pilot url
    for pilot in ships:

        # Loop to extract names of pilots url and request data from api
        if pilot['pilots']:
            pilot_names = [api_store(url)['name'] for url in pilot['pilots']]

            # Find pilot ObjectIds that corresponds to pilot names in the characters collection
            pilot_name_id = [next(sw_db.characters.find({"name": nam}))['_id'] for nam in pilot_names]

            # Update starships collection with ObjectIds of pilots from characters collection
            sw_db.starships.update_one({'name': pilot['name']}, {"$set": {"pilots": pilot_name_id}})
    print('starships collection successfully updated')



