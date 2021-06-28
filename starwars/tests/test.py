from starwars.app.api_read import read_api, create_dict

def test_read_from_api():
    assert read_api() == "<Response [200]>"


def test_create_dict():
    assert type(create_dict(read_api())) is dict

