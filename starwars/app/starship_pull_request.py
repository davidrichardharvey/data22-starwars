# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:30:09 2021

@author: Andrew Rothwell
"""

import requests


# Returns the HTTP status code from the website to ensure the resource is open
# to requests.
def status_code():
    return requests.get("https://swapi.dev/api/starships/").status_code


# Pulls all starship data from the swapi and returns it as a list.
def pull_starship_data():
    starship_data = []
    for page in range(1, 5):
        url = "https://swapi.dev/api/starships/?page="
        starship_data.append(requests.get(url + str(page)).text)
    return starship_data
