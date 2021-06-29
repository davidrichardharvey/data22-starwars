import pymongo
import bson


client = pymongo.MongoClient()
db = client['starwars']
characters = db['starwars']


def test_read_mongodb():
    # Test to ensure connection to MongoDB and ObjectId is being read from MongoDB
    # Test to find Luke Skywalker with his ObjectId from the characters collection in MongoDB
    # And to check its format (bson)
    find_with_id = db.characters.find_one({'name': 'Luke Skywalker'}, {'_id': 1})
    assert type(find_with_id['_id']) == bson.objectid.ObjectId


def test_starship_update():
    # Test to ensure pilot field is updated within MongoDB with pilot ObjectId
    ship = db.starships.find_one({'name': 'Millennium Falcon'}, {'_id': 0})['pilots']
    assert type(ship[0]) == bson.objectid.ObjectId


