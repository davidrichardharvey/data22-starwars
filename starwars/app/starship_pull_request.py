# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:30:09 2021

@author: Andrew Rothwell
"""

import requests


def status_code():
    return requests.get("https://swapi.dev/api/starships/").status_code
