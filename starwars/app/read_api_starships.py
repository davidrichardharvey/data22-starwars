import requests
# from pprint import pprint

# These functions request from the API all 4 pages of the starships collection. Then displays the data in JSON format.


def read_api_page_one():
    response_page1 = requests.get("https://swapi.dev/api/starships")
    return response_page1.json()


def read_api_page_two():
    response_page2 = requests.get("https://swapi.dev/api/starships/?page=2")
    return response_page2.json()


def read_api_page_three():
    response_page3 = requests.get("https://swapi.dev/api/starships/?page=3")
    return response_page3.json()


def read_api_page_four():
    response_page4 = requests.get("https://swapi.dev/api/starships/?page=4")
    return response_page4.json()


# pprint(read_api_page_one())
# pprint(read_api_page_two())
# pprint(read_api_page_three())
# pprint(read_api_page_four())
