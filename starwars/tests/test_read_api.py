from starwars.app.read_api import read_api


def test_read_api():
    assert str(type(read_api())) == "<class 'tuple'>"