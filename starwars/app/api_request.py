import requests


def api_request():
    starships = requests.get("https://swapi.dev/api/starships")
    return starships.status_code
