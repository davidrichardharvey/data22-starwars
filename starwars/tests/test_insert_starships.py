from starwars.app.create_starships_collection import starwars_db


# test to see whether the function successfully inserts the starship documents into the starships collection
# this test works because the starship collection only becomes visible once documents have been added to it
# use pytest -v in the terminal to see a clearly structured test and outcome
def test_insert_starships_collection():
    assert 'starships' in starwars_db.list_collection_names()




