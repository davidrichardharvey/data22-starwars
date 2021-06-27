# -*- coding: utf-8 -*-
from starwars.app.starship_pull_request import status_code
"""
Created on Sun Jun 27 18:14:05 2021

@author: Andrew Rothwell
"""
'''

Tests that the "status_code" function in the "starship_pull_request.py" file
is correctly returning the status_code "200"

'''


def test_starship_pull_request():

    assert status_code() == 200
