import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def db_drop():
    db.starships.drop()
    return [ship for ship in db.starships.find()]
