from starwars.app.insert_starships_data import *


def test_insert_starships():
    assert 'starships' in starwars_db.list_collection_names()