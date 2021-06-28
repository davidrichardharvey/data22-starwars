import requests

starships_url_1 = "https://swapi.dev/api/starships/?page=1"
starships_url_2 = "https://swapi.dev/api/starships/?page=2"
starships_url_3 = "https://swapi.dev/api/starships/?page=3"
starships_url_4 = "https://swapi.dev/api/starships/?page=4"


def read_api(starships_url):
    starships = requests.get(starships_url)
    return starships


def create_dict(data):
    dictionary = data.json()
    return dictionary






