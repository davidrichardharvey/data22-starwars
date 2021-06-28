from starwars.app.api_call import *

def test_api_call():
    assert response.status_code == 200

def test_api_read():