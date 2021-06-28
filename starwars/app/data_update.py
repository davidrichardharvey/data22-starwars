import requests
from pprint import pprint
import json


# reads the starships db, isolates just the data and returns a list of starships. Each element is a dictionary
def read_starships_api():
    starships_req = requests.get("https://swapi.dev/api/starships")
    starships = starships_req.json()["results"]  # isolates just the data and not other details like count
    return starships


# creates a list of pilots for each ship. If empty will be blank
def create_pilot_list(starships):
    pilots = [i['pilots'] for i in starships]  # list of each ships pilots
    return pilots


# takes in pilot api address and outputs content
def pilot_api_read(pilot_api):
    return requests.get(pilot_api)





# creates an ordered list of the pilot character data. Calls the api url.
def create_pilot_character_list(pilots):
    pilot_character_ordered = []  # ordered list of the pilots, will match original
    for crew in pilots:
        if not crew:  # if no crew
            pilot_character_ordered.append(crew)  # adds empty list
        else:  # if crew
            starship_pilots = []  # creates empty list for each ship
            for pilot in crew:  # allows for multiple pilots per ship
                starship_pilots.append(pilot_api_read(pilot).json())  # adds each pilot character to its ship list
            pilot_character_ordered.append(starship_pilots)  # adds total ship to ordered list
    return pilot_character_ordered


# updates the list of starship pilots urls with the character lists.
def update_starships(starships, pilot_character_ordered):
    for ship in starships:
        ship['pilots'] = pilot_character_ordered[0]
        pilot_character_ordered.pop(0)

def run_all():
    starships = read_starships_api()
    pilots = create_pilot_list(starships)
    pilot_character_ordered = create_pilot_character_list(pilots)
    update_starships(starships, pilot_character_ordered)
    return starships
