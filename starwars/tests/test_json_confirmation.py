import requests
# This test is used to confirm that the content type of the API URL link, is in fact of a json type
def test_api_content_in_json_form():
    response = requests.get("https://swapi.dev/api/starships/")
    assert response.headers["Content-type"] == "application/json"