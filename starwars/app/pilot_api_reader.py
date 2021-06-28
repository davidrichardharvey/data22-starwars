import requests


def pilot_api_reader(url):
    response = requests.get(url)
    return response.json()

print(type(pilot_api_reader('https://swapi.dev/api/starships/?page=1')))