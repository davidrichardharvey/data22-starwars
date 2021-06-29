from starwars.app.data_update import *

def test_read_starships_api_type(): # tests if returns the correct type of data
    assert str(type(read_starships_api())) == "<class 'list'>"

def test_create_pilots_list():
    assert str(type(create_pilot_list())) == "<class 'list'>"
    
def test_pilot_api_read():
    info = pilot_api_read('https://swapi.dev/api/people/4/')
    assert info.status_code == 200
