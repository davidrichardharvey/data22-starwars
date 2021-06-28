import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def db_drop():
    # This function will clear the repository
    db.starships.drop()
    return [ship for ship in db.starships.find()]
