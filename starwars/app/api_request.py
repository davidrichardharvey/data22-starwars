import requests
from pprint import pprint
import json


def api_request():
    starships = requests.get("https://swapi.dev/api/starships")
    return starships

