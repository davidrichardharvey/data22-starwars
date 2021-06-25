from starwars.app.api_request import api_call

def test_api_call():
    assert str(api_call()) == '<Response [200]>'
