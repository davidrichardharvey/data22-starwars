import requests
from pprint import pprint
import json


# starships_req = requests.get("https://swapi.dev/api/starships","https://swapi.dev/api/starships//?page=2")

def read_starships_api():  # reads all 4 pages of the starships db
    page_1 = str(requests.get("https://swapi.dev/api/starships"))
    page_2 = str(requests.get("https://swapi.dev/api/starships//?page=2"))
    page_3 = str(requests.get("https://swapi.dev/api/starships//?page=3"))
    page_4 = str(requests.get("https://swapi.dev/api/starships//?page=4"))
    all_page = page_1 + page_2 + page_3 + page_4
    print(all_page)
    return all_page


print(read_starships_api())
# print(read_starships_api())

# # pprint(starships_req.json("https://swapi.dev/api/starships"))
#
# print("Status code ", starships_req.status_code)
# print("Headers ", starships_req.headers)
