# -*- coding: utf-8 -*-
from starwars.app.starship_pull_request import status_code
from starwars.app.starship_pull_request import transform_starship_data
"""
Created on Sun Jun 27 18:14:05 2021

@author: Andrew Rothwell
"""


def test_starship_pull_request():

    # Tests that the "status_code" function in the "starship_pull_request.py"
    # file is correctly returning the status_code "200"
    assert status_code() == 200

    # Test that asserts whether the data pulled from the swapi website has
    # been correctly pulled and formatted in a 36 length list of dictionaries.
    assert len(transform_starship_data()) == 36
