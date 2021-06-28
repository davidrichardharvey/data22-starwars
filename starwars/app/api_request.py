import requests
import json
from pprint import pprint


def api_call():
    starships_api = requests.get("https://swapi.dev/api/starships/")
    return starships_api.status_code
