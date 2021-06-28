from starwars.app.pilot_api_reader import *


# test to see whether the function prints the starships information as a dictionary
def test_pilot_api_reader():
    assert str(type(pilot_api_reader('https://swapi.dev/api/starships/?page=1'))) == "<class 'dict'>"
