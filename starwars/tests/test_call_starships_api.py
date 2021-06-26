from starwars.app.call_starships_api import call_starships_api

# test to see whether the function successfully calls the starships api
def test_call_starships_api():
    assert str(call_starships_api()) == '(<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>)'
