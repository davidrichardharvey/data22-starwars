from starwars.app.api_read import *


def test_read_from_api():
    assert read_api(starships_url_1).status_code == 200
    assert read_api(starships_url_2).status_code == 200
    assert read_api(starships_url_3).status_code == 200
    assert read_api(starships_url_4).status_code == 200


def test_create_dict():
    assert type(create_dict(read_api(starships_url_1))) is dict
    assert type(create_dict(read_api(starships_url_2))) is dict
    assert type(create_dict(read_api(starships_url_3))) is dict
    assert type(create_dict(read_api(starships_url_4))) is dict

