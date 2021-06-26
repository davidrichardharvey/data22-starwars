from pprint import pprint
import requests


def read_starships_api():
    response1 = requests.get('https://swapi.dev/api/starships/?page=1')
    response2 = requests.get('https://swapi.dev/api/starships/?page=2')
    response3 = requests.get('https://swapi.dev/api/starships/?page=3')
    response4 = requests.get('https://swapi.dev/api/starships/?page=4')
    return response1.json(), response2.json(), response3.json(), response4.json()

pprint(type(read_starships_api())) # this tells us what type is returned which is the part we are testing for

# trying to print all 4 pages at once is proving challenging -
# managed to achieve this by having all the urls in the function under different variables
pprint(read_starships_api())

# There are 4 separate pages of starships:
# 'https://swapi.dev/api/starships/?page=1'
# 'https://swapi.dev/api/starships/?page=2'
# 'https://swapi.dev/api/starships/?page=3'
# 'https://swapi.dev/api/starships/?page=4'


