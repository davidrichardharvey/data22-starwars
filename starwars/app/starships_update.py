import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def starships_update(requested_data):  # The argument is the api_request function
    # Takes the requested data and puts it into a list
    list_of_ships = requested_data.json()["results"]
    # Inserts the requested data into the repository
    db.starships.insert_many(list_of_ships)
    ships = db.starships.find()
    # Returns repository for tests
    return [ship for ship in ships]



