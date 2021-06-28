import requests

starships_url_1 = "https://swapi.dev/api/starships/?page=1"
starships_url_2 = "https://swapi.dev/api/starships/?page=2"
starships_url_3 = "https://swapi.dev/api/starships/?page=3"
starships_url_4 = "https://swapi.dev/api/starships/?page=4"


def read_api(starships_url):
    starships = requests.get(starships_url)
    return starships


starships_1 = read_api(starships_url_1)
starships_2 = read_api(starships_url_2)
starships_3 = read_api(starships_url_3)
starships_4 = read_api(starships_url_4)


def create_list_of_dict(data):
    dictionary = data.json()
    return dictionary["results"]


starships_1_list = create_list_of_dict(starships_1)
starships_2_list = create_list_of_dict(starships_2)
starships_3_list = create_list_of_dict(starships_3)
starships_4_list = create_list_of_dict(starships_4)


def merge_lists_of_dicts(starships_1, starships_2, starships_3, starships_4):
    all_starships = starships_1 + starships_2 + starships_3 + starships_4
    return all_starships


all_starship_data = merge_lists_of_dicts(starships_1_list, starships_2_list, starships_3_list, starships_4_list)


def change_pilot_to_character_name(all_starships):
    for ship in all_starships:
        for pilot in ship["pilots"]:
            pilot_index = ship["pilots"].index(pilot)
            ship["pilots"][pilot_index] = requests.get(pilot).json()["name"]
    return all_starships


