import requests


starships_url = "https://swapi.dev/api/starships/"
ship_list = []


def url_results():
    next_page = starships_url
    while next_page:
        json_return = requests.get(next_page).json()
        for ship in json_return["results"]:
            ship_list.append(ship)
        next_page = json_return["next"]


# pprint(ship_list)  # [{}]
