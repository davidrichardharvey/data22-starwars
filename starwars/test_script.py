from starwars.app.transform_data import *
from starwars.app.get_api import *

Obj = Find_Characters()


def test_find_page_count():
    assert Obj.find_page_count() == 4


def test_api_correct_status_code():
    # Checks that the HTTP status code equals 200
    response = requests.get("https://swapi.dev/api/starships/?page=2")
    assert response.status_code == 200


def test_api_content():
    # Testing the content of the json file, asserting that the contents should be in json format
    # Cannot test the content of the file, instead look at the headers (keys)
    response = requests.get("https://swapi.dev/api/starships/")
    assert response.headers["Content-type"] == "application/json"


def test_delete_old_collection():
    Obj.delete_old_collection()
    assert db.starships.count() == 0

# def test_insert_data_into_db():
#     Obj.insert_data_into_db()
#     assert db.starships.count() == 1