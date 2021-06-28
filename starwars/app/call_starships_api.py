# This is a function that calls the starships API
import requests


def call_starships_api():
    response1 = requests.get('https://swapi.dev/api/starships/?page=1')
    response2 = requests.get('https://swapi.dev/api/starships/?page=2')
    response3 = requests.get('https://swapi.dev/api/starships/?page=3')
    response4 = requests.get('https://swapi.dev/api/starships/?page=4')
    return response1, response2, response3, response4


# print(call_starships_api())
