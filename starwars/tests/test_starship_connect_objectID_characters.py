# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:16:19 2021

@author: Andrew Rothwell
"""

import requests
import json
import pymongo
from starwars.app.starship_connect_objectID_characters import starship_connect_url_characters
from starwars.app.starship_connect_objectID_characters import starship_connect_objectID_characters
client = pymongo.MongoClient()

db = client['starwars']

# Tests that all urls have been replaced with valid character names from the
# swapi.


def test_starship_connect_url_characters():

    url = "https://swapi.dev/api/people/"
    char_list = []

    for page_number in range(1, 10):
        url = "https://swapi.dev/api/people/?page="
        char_data = requests.get(url + str(page_number)).text
        char_data = json.loads(char_data)

        for entry in range(len(char_data["results"])):
            char_list.append(char_data["results"][entry]["name"])

    starship_data = starship_connect_url_characters()

    for starship in starship_data:
            if starship["pilots"] != []:
                for pilot in range(len(starship["pilots"])):
                    assert starship["pilots"][pilot] in char_list


# Tests that the pilot object ids are in the list of object ids from the
# characters database.
def test_starship_connect_objectID_characters():

    characters = db.char_demo.find({}, {"name": 1, "_id": 1})

    char_list = []

    for row in characters:
        char_list.append([str(row['_id']), row['name']])

    char_list = dict(char_list)

    starship_data = starship_connect_objectID_characters()

    for starship in starship_data:
            if starship["pilots"] != []:
                for pilot in range(len(starship["pilots"])):
                    for char_id in char_list:
                        assert starship["pilots"][pilot] in char_list
