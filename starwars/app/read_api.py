import requests
from pprint import pprint

# Function that reads the starships collection and displays it in PyCharm.
def read_api_page_one():
    response_page1 = requests.get("https://swapi.dev/api/starships") # gets the starship info from page 1
    return response_page1.json()

def read_api_page_two():
    response_page2 = requests.get("https://swapi.dev/api/starships/?page=2") # gets the starship info from page 2
    return response_page2.json()

def read_api_page_three():
    response_page3 = requests.get("https://swapi.dev/api/starships/?page=3") # gets the starship info from page 3
    return response_page3.json()

def read_api_page_four():
    response_page4 = requests.get("https://swapi.dev/api/starships/?page=4") # gets the starship info from page 4
    return response_page4.json()
