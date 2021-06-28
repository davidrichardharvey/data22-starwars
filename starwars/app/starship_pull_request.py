# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:30:09 2021

@author: Andrew Rothwell
"""

import requests
import json


# Returns the HTTP status code from the website to ensure the resource is open
# to requests.
def status_code():
    return requests.get("https://swapi.dev/api/starships/").status_code


# Pulls all starship data from the swapi, loads it into a usable format, and
# returns it as a list.
def transform_starship_data():

    starship_data_list = []

    for page_number in range(1, 5):
        url = "https://swapi.dev/api/starships/?page="
        starship_data = requests.get(url + str(page_number)).text
        starship_data = json.loads(starship_data)

        for entry in range(len(starship_data["results"])):
            starship_data_list.append(starship_data["results"][entry])

    return starship_data_list
