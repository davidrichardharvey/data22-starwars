# -*- coding: utf-8 -*-
from starwars.app.starship_pull_request import status_code
from starwars.app.starship_pull_request import pull_starship_data
"""
Created on Sun Jun 27 18:14:05 2021

@author: Andrew Rothwell
"""


def test_starship_pull_request():

    # Tests that the "status_code" function in the "starship_pull_request.py"
    # file is correctly returning the status_code "200"

    assert status_code() == 200

    # Test that the starship pull request has pulled all the correct data by
    # checking if the list of dictionaries is 4 values in length, meaning it
    # has correctly stored all 4 pages of the swapi starship data.

    assert len(pull_starship_data()) == 4
