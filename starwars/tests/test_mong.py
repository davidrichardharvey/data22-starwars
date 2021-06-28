import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def test_read_mongodb():
    # Test to ensure connection to MongoDB and ObjectId is being read from MongoDB
    luke = str(next(db.characters.find({'name': "Luke Skywalker"}, {"name": 1}))['_id'])
    assert luke == "60d46857c16c4f04ffee0c88"


