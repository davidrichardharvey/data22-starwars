# Use pytest in the terminal to carry out testing
from starwars.app.read_api import read_api


def test_read_api():
    assert read_api("https://swapi.dev/api/starships") == "https://swapi.dev/api/starships"
