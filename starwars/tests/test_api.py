from starwars.app.api_request import api_call


def test_api_call():
    assert api_call() == 200
