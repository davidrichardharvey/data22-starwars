from starwars.app.api_call import *
from starwars.app.starships import *
from starwars.app.api_call import *


# There should only be the characterz collection
def test_collection_drop():
    assert current_collection_drop() != db["starships"]

# Review
# There are [10,10,10,4] records inputted into starships collection from the API
# This test shows if they have been inputted and equally pulled correctly
# def test_records_entry():
#     assert insert_starship() == 36


# def test_api():
#     assert url_request() == 200
