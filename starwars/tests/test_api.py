import json

from starwars.app.api_request import *



def test_read_from_api():
    # Test to ensure api_call function is successfully making requests from the star wars APi
    assert api_call("https://swapi.dev/api/").status_code == 200


def test_store_api_json():
    # Test to ensure my data is converted and stored in dictionary format
    assert type(api_store("https://swapi.dev/api/")) == dict













