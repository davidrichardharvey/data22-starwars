import requests


# These functions read the 4 pages of starships information in json format
def read_starships_api_page1():
    page1 = requests.get('https://swapi.dev/api/starships/?page=1').json()
    return page1


def read_starships_api_page2():
    page2 = requests.get('https://swapi.dev/api/starships/?page=2').json()
    return page2


def read_starships_api_page3():
    page3 = requests.get('https://swapi.dev/api/starships/?page=3').json()
    return page3


def read_starships_api_page4():
    page4 = requests.get('https://swapi.dev/api/starships/?page=4').json()
    return page4


# trying to print all 4 pages at once is proving challenging -
# managed to achieve this by having 4 separate functions to read each of the 4 sets of starships APIs

# There are 4 separate pages of starships:
# 'https://swapi.dev/api/starships/?page=1'
# 'https://swapi.dev/api/starships/?page=2'
# 'https://swapi.dev/api/starships/?page=3'
# 'https://swapi.dev/api/starships/?page=4'
