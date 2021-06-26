from starwars.app.call_api import call_api


def test_call_api():
    assert str(call_api()) == '(<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>)'