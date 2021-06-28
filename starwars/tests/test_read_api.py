from starwars.app.data_update import *

def read_starships_api_type(): # tests if returns the correct type of data
    assert str(type(read_starships_api())) == "<class 'list'>"

def pilots_list():
    assert type(create_pilot_list()) == "list"

def pilot_api_read():


