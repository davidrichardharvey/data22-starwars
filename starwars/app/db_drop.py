import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def db_drop():
    db.starships.drop()
    starship_dict = db.starships.find()
    return [ship for ship in starship_dict]

