import requests
import json
from pprint import pprint


def api_call():
    starships_api = requests.get("https://swapi.dev/api/starships/")
    return starships_api.status_code


def get_starships():
    headers = {'Content-Type': 'application/json'}
    response = requests.get("https://swapi.dev/api/starships/", headers=headers)
    response_json = response.json()
    return response_json
