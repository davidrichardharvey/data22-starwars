from starwars.app.api_request import *



def test_read_from_api():
    # Test to ensure api_call function is successfully making requests from the star wars APi
    assert api_call("https://swapi.dev/api/").status_code == 200

    # Test to ensure print function is printing data from api_call in json format
    assert type(api_call("https://swapi.dev/api/").json()) == dict










