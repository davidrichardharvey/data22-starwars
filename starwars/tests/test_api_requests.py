import requests

def test_valid_api_requests():
    # Test to make sure requests is reading from the starwars api url

    # Pages that should exist
    starwars_api = requests.get("https://swapi.dev/api/")
    starships_api = requests.get("https://swapi.dev/api/starships")

    assert starwars_api.status_code == 200
    assert starships_api.status_code == 200


def test_invalid_api_requests():
    # Test to check for invalid urls

    # Invalid URL's
    inv_starwars_api = requests.get("https://swapi.dev/apiwf/")
    inv_starships_api = requests.get("https://swapi.dev/api/star$hipz")

    assert inv_starwars_api.status_code == 404
    assert inv_starships_api.status_code == 404