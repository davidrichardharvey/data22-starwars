import requests


def read_api(url):
    response = requests.get(url)
    pprint(response.json())


read_api("https://swapi.dev/api/starships")
# "https://swapi.dev/api/starships/?page=2"
# "https://swapi.dev/api/starships/?page=3"
# "https://swapi.dev/api/starships/?page=4"