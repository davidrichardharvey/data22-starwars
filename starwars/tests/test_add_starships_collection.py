from starwars.app.insert_starships_data import *

# Tests that the starships collection can be found in the starwars database
def test_insert_starships():
    assert 'starships' in starwars_db.list_collection_names()