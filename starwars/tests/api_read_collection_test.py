from starwars.app.read_api_starships import *


# Test that checks if the function is printing the correct info from the API
def test_read_api():
    assert str(type(read_api_page_one())) == "<class 'dict'>"
    assert str(type(read_api_page_two())) == "<class 'dict'>"
    assert str(type(read_api_page_three())) == "<class 'dict'>"
    assert str(type(read_api_page_four())) == "<class 'dict'>"
