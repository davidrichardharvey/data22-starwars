# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:48:58 2021

@author: Andrew Rothwell
"""

# Takes the pilots from the swapi and assigns the pilot urls to names instead.

import requests
import json
from starwars.app.starship_pull_request import transform_starship_data
import pymongo

client = pymongo.MongoClient()

db = client['starwars']


def starship_connect_url_characters():
    starship_data = transform_starship_data()
    for starship in starship_data:
        if starship["pilots"] != []:
            for pilot in range(len(starship["pilots"])):
                url = "https://swapi.dev/api/people/"
                char_id = starship["pilots"][pilot].split("/")[-2]
                char_data = requests.get(url + str(char_id)).text
                char_data = json.loads(char_data)
                starship["pilots"][pilot] = char_data["name"]

    return starship_data

# Find associated names for all pilots and replace with their objectIDs from
# Mongo instead.


def starship_connect_objectID_characters():

    characters = db.char_demo.find({}, {"name": 1, "_id": 1})

    char_list = []

    for row in characters:
        char_list.append([str(row['_id']), row['name']])

    starship_data = starship_connect_url_characters()
    for starship in starship_data:
        if starship["pilots"] != []:
            for pilot in range(len(starship["pilots"])):
                for row in char_list:
                    if starship["pilots"][pilot] == row[1]:
                        starship["pilots"][pilot] = row[0]

    return starship_data
