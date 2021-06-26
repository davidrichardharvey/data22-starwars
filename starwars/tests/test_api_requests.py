import requests

def test_read_from_api():
    # Test to make sure requests is reading from the starwars api url

    starwars_api = requests.get("https://swapi.dev/api/")
    starships_api = requests.get("https://swapi.dev/api/starships")

    assert starwars_api.status_code == 200
    assert starships_api.status_code == 200


if __name__ == "__main__":
    test_read_from_api()