from starwars.app.api_request import *
from starwars.app.sw_mongo import *
import pymongo


def test_api_call():
    assert api_call() == 200


def test_get_starships():
    assert get_starships()['count'] == 36


def test_get_all_pages_starships():
    assert len(get_all_pages_starships()) == 36


def test_get_all_people():
    assert len(get_all_people()) == 81


def test_create_starships_collection():
    assert starships_coll.find() != None
