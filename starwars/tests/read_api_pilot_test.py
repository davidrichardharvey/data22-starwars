from starwars.app.read_api_pilot import *


# Test to see whether the function prints the starships information as a dictionary.


def test_pilot_api_reader():
    assert str(type(read_api_pilot('https://swapi.dev/api/starships/?page=1'))) == "<class 'dict'>"
