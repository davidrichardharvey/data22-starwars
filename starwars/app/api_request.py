import requests
from pprint import pprint


def api_request():
    starships = requests.get("https://swapi.dev/api/starships")
    return starships

