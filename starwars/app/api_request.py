import requests
from pprint import pprint


def api_call():
    starships_api = requests.get("https://swapi.dev/api/starships/")
    return starships_api.status_code  # successful status code = 200


def get_starships():
    headers = {'Content-Type': 'application/json'}
    response = requests.get("https://swapi.dev/api/starships/", headers=headers)  # get all information from starships
    response_json = response.json()  # starships in JSON format
    return response_json


# pprint(get_starships()['results'])


def get_all_pages_starships():
    headers = {'Content-Type': 'application/json'}
    ships_list = []
    for ship in range(76):
        response = requests.get("https://swapi.dev/api/starships/" + str(ship) + '/', headers=headers)
        # get all information from all starships
        response_json = response.json()  # starships in JSON format
        if response_json.get('detail') == 'Not found':
            pass
        else:
            ships_list.append(response_json)  # add starship's dictionary of details into list: ships_list
    print(len(ships_list))
    return ships_list
