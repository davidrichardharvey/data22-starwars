import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def db_drop():
    db.starships.drop()
    return db.starships.find_many()
