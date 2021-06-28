import requests

# This test to makes sure requests is reading from the Star Wars API URL
# A status code of 200 means the request has succeeded
def test_valid_api_request():
    valid_starwars_api = requests.get("https://swapi.dev/api/")
    assert valid_starwars_api.status_code == 200

# This test to makes sure requests can identify an invalid Star Wars API URL
# A status code of 404 means that the request was unsuccessful & that URL doesn't exist
def test_invalid_api_request():
    invalid_starwars_api = requests.get("https://swapi.dev/apiOLA/")
    assert invalid_starwars_api.status_code == 404

