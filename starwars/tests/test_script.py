from starwars.app.transform_data import *
from starwars.app.get_api import *

Obj = FindCharacters()

# Test if the page count matches the true page count
def test_find_page_count():
    assert Obj.find_page_count() == 4

# Test is the HTTP status code equals 200 and api is correct
def test_api_correct_status_code():
    response = requests.get("https://swapi.dev/api/starships/?page=2")
    assert response.status_code == 200

# Testing the content of the json file, asserting that the contents should be in json format
def test_api_content():
    response = requests.get("https://swapi.dev/api/starships/")
    assert response.headers["Content-type"] == "application/json"

# Test if the starship collection successfully created in database
def test_insert_data_into_db():
    assert "starships" in db.list_collection_names()

