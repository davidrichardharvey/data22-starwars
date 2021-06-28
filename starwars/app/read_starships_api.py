import requests


# This functions reads the 4 pages of starships information in json format
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

# pprint(type(read_starships_api()))  # this tells us what type is returned which is the part we are testing for

# trying to print all 4 pages at once is proving challenging -
# managed to achieve this by having all the urls in the function under different variables
# pprint(read_starships_api())

# There are 4 separate pages of starships:
# 'https://swapi.dev/api/starships/?page=1'
# 'https://swapi.dev/api/starships/?page=2'
# 'https://swapi.dev/api/starships/?page=3'
# 'https://swapi.dev/api/starships/?page=4'
