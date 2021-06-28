from starwars.app.create_starships_collection import create_starships_collection


# test to see whether the function successfully creates the starships collection
# use pytest -v in the terminal to see a clearly structured test and outcome
def test_create_starships_collection():
    assert str(type(create_starships_collection())) == "<class 'pymongo.collection.Collection'>"

