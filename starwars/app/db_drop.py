import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def db_drop():
    db.starwars.starships.drop()
    return [ship for ship in db.starwars.starships.find()]
