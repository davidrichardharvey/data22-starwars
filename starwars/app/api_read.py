import requests

# url for each page of the results from the api
starships_url_1 = "https://swapi.dev/api/starships/?page=1"
starships_url_2 = "https://swapi.dev/api/starships/?page=2"
starships_url_3 = "https://swapi.dev/api/starships/?page=3"
starships_url_4 = "https://swapi.dev/api/starships/?page=4"


# function to perform a get request on the api
def read_api(starships_url):
    starships = requests.get(starships_url)
    return starships


# function to create a list of dictionaries from the starship data
def create_list_of_dict(data):
    dictionary = data.json()
    return dictionary["results"]


# function to merge all 4 lists of dictionaries into one list
def merge_lists_of_dicts(starships_1, starships_2, starships_3, starships_4):
    all_starships = starships_1 + starships_2 + starships_3 + starships_4
    return all_starships


# function to change the url for pilots into the character name, argument is list of dictionaries
def change_pilot_to_character_name(all_starships):
    for ship in all_starships:
        for pilot in ship["pilots"]:
            pilot_index = ship["pilots"].index(pilot)
            ship["pilots"][pilot_index] = requests.get(pilot).json()["name"]
    return all_starships


# function to replace character names with objectId's, arguments are list of dictionaries with characters name(all_starships)
# character_dict is dictionary with character name as key and objectID as value
def replace_character_name_for_object_id(all_starships, character_dict):
    for ship in all_starships:
        for pilot in ship["pilots"]:
            for name, objectID in character_dict.items():
                if pilot == name:
                    pilot_index = ship["pilots"].index(pilot)
                    ship["pilots"][pilot_index] = character_dict[name]
    return all_starships
