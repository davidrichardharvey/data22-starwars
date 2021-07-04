from multi_page_api import *
from starships_refactor import *


def test_request_response():
    # Send a request to the API server and store the response
    # passed
    response = requests.get(starships_url)
    assert response.status_code is 200


def test_number_of_starships():
    # total number of starships should be 36
    assert len(url_results()) is 36


def test_number_of_inserted_starships():
    # total number of starships inserted into the collection should be 36
    assert insert_starships() is 36