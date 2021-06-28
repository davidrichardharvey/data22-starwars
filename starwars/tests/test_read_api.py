from starwars.app.read_api import read_starships_api

def read_starships_api_type(): # tests if returns the correct type of data
    assert str(type(read_starships_api())) == "<class 'tuple'>"

def starships_to_list():
    assert type() == "list"

def pilots_list():
    assert type() == "list"

def pilot_api_read():


