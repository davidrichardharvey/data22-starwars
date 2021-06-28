import requests


def api_call():
    starships_api = requests.get("https://swapi.dev/api/starships/")
    return starships_api.status_code  # successful status code = 200


def get_all_pages_starships():
    headers = {'Content-Type': 'application/json'}
    ships_list = []
    for ship in range(76):
        # get all information from all starships
        response = requests.get("https://swapi.dev/api/starships/" + str(ship) + '/', headers=headers)
        response_json = response.json()  # starships in JSON format
        if response_json.get('detail') == 'Not found':
            pass
        else:
            ships_list.append(response_json)  # add starship's dictionary of details into list: ships_list
    return ships_list


def get_ships_pilots():
    ships_list = get_all_pages_starships()  # list of dictionaries of details for all starships
    ships_pilots_dict = {}  # dictionary: {ship's name: list of ship's pilots}
    for ship in ships_list:
        ship_name = ship['name']
        # add a key-value pair to ships_pilots_dict. {ship's name: empty list of pilots}
        ships_pilots_dict[ship_name] = []
        if ship['pilots'] == []:  # if ship has no pilots, pass
            pass
        else:
            ship_pilots = ship['pilots']
            # update key-value pair in ships_pilots_dict to {ship's name: list of pilots}
            ships_pilots_dict[ship_name] = ship_pilots
    return ships_pilots_dict  # return dictionary of ships with list of pilots for each ship


def get_all_people():
    headers = {'Content-Type': 'application/json'}
    people_list = []
    for person in range(83):
        # get all information from all people
        response = requests.get("https://swapi.dev/api/people/" + str(person) + '/', headers=headers)
        response_json = response.json()  # people's details in JSON format
        if response_json.get('detail') == 'Not found':
            pass
        else:
            people_list.append(response_json)  # add person's dictionary of details into list: people_list
    return people_list


def get_peoples_url():
    list_of_people = get_all_people()  # list of dictionaries of details for all people
    peoples_url_dict = {}  # dictionary: {peron's url: person's name}
    for person in list_of_people:
        persons_url = person['url']
        persons_name = person['name']
        # add a key-value pair in peoples_url_dict: {person's url: person's name}
        peoples_url_dict[persons_url] = persons_name
    return peoples_url_dict  # return dictionary of people with their name and url string for each person


people_url_dict = get_peoples_url()
