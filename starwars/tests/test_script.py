from starwars.app.get_api import *

def test_find_page_count():
    Obj = find_starships()
    assert Obj.find_page_count() == 4

def test_type_get_api():
    Obj = find_starships()
    assert type(Obj.get_api()) == list

def test_len_get_api():
    Obj = find_starships()
    Obj.find_page_count()
    assert len(Obj.get_api()) == 36
