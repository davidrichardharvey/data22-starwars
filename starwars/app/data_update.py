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


pilot_list_ordered = []  # ordered list of the pilots, will match original


# loops through to isolate each individual pilot api, calls it and then makes a list of those apis
def create_pilot_character_list(pilots):
    for i in pilots:
        if not i:  # if no crew
            pilot_list_ordered.append(i)  # adds empty list
        else:  # if crew
            starship_pilots = []  # creates empty list for each ship
            for x in i:  # allows for multiple pilots per ship
                starship_pilots.append(pilot_api_read(x).json())  # adds each pilot character to its ship list
            pilot_list_ordered.append(starship_pilots)  # adds total ship to ordered list


# replaces the starship list pilots urls with the character lists.
def update_starships(starships):
    for ship in starships:
        ship['pilots'] = pilot_list_ordered[0]
        pilot_list_ordered.pop(0)

def run_all():
    starships = read_starships_api()
    pilots = create_pilot_list(starships)
    create_pilot_character_list(pilots)
    update_starships(starships)
    print('Updated startships:', starships)
