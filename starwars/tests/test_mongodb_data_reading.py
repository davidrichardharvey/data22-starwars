import pymongo
from pprint import pprint

def test_mongodb_connection():
    # Make sure mongodb database is running on localhost and can be accessed using pymongo
    client = pymongo.MongoClient()
    
    assert client.HOST == "localhost"
    assert client.PORT == 27017


def test_retrieve_character_id():
    # Test to check that character ID's can be retrieved with pymongo
    client = pymongo.MongoClient()
    db = client["starwars"]

    # Collect document data for Han Solo by the name field and get ID
    han_solo_id = str(next(db.characters.find({"name": "Han Solo"}))["_id"])

    assert han_solo_id == "60d4655011180bd60f431c91"
