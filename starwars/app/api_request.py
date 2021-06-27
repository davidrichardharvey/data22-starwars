import requests
from pprint import pprint
import json


def api_request():
    starships = requests.get("https://swapi.dev/api/starships")
    return starships

a= api_request()
pprint(a.json()["results"])
