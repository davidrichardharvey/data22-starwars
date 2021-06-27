from starwars.app.get_api import *
from starwars.app.characters import *

def test_find_page_count():
    Obj = starships()
    assert Obj.find_page_count() == 4

def test_type_get_api():
    Obj = starships()
    assert type(Obj.get_api()) == list

def test_len_get_api():
    Obj = starships()
    Obj.find_page_count()
    assert len(Obj.get_api()) == 36

def test_get_ships_pilot():
    Obj = starships()
    assert type(Obj.get_ships_pilot) == list

def test_locate_url():
    Obj=find_characters()
    Obj.locate_url()
    assert type(Obj.locate_url) == list
