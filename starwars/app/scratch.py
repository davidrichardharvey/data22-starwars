import requests
import json
from pprint import pprint

starships_req = requests.get("https://swapi.dev/api/starships")

# print("json", starships_req.json())
# print("Type", type(starships_req.json()))
starships = starships_req.json()["results"]  # isolates just the data and not other details like count

starships_list = [i for i in starships] # list of each starship dictionary
print('Starship list', starships_list)

pilots = [i['pilots'] for i in starships_list]  # list of each ships pilots
# print('Pilots', pilots)

# takes in pilot api address and outputs content
def pilot_api_read(pilotapi):
    return requests.get(pilotapi)

pilot_list_ordered = [] # ordered list of the pilots, will match origional


# loops through to isolate each individual pilot api, calls it and then makes a list of those apis
def create_pilot_character_list():
    for i in pilots:
        if not i:
            # print('Empty\n')
            pilot_list_ordered.append(i) # adds empty list if blank
        else:
            # print('NEW STARSHIP')
            # print('P api', i)
            starship_pilots = [] # creates empty list for each ship
            for x in i:
                # print('Individual pilot:', x)
                starship_pilots.append(pilot_api_read(x).json()) # adds each pilot character data to list
            # print('Starship pilots list', starship_pilots)
            pilot_list_ordered.append(starship_pilots) # adds total ship pilot charater data to list
            # print('End\n')
    # print(pilot_list_ordered)

create_pilot_character_list()

# replaces the starship list pilots urls with the character lists.
for ship in starships_list:
    ship['pilots'] = pilot_list_ordered[0]
    pilot_list_ordered.pop(0)

print('Updated starship_list:', starships_list)



