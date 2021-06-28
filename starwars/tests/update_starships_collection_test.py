from starwars.app.update_starships_collection import *


def update_starships_collection_test():
    assert "starships" in starwars_db.list_collection_names()
