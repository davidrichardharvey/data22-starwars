from starwars.app.api_req import *


#  Creating a test to check the requests package returns a successful API request.
def test_requests_status():
    #  Using the imported req_api function to request data from the api.
    req_info = req_api("https://swapi.dev/api/")
    #  Asserting status code 200 as this denotes a successful request.
    assert req_info.status_code == 200
