import pymongo
from pprint import pprint
import requests
import json

def read_starships_api(api_url):
    response = requests.get(api_url)
    pprint(response.json())

# trying to print all 4 pages at once is proving challenging
read_starships_api('https://swapi.dev/api/starships/?page=1')
read_starships_api('https://swapi.dev/api/starships/?page=2')
read_starships_api('https://swapi.dev/api/starships/?page=3')
read_starships_api('https://swapi.dev/api/starships/?page=4')

# 'https://swapi.dev/api/starships/?page=1'
# 'https://swapi.dev/api/starships/?page=2'
# 'https://swapi.dev/api/starships/?page=3'
# 'https://swapi.dev/api/starships/?page=4'





