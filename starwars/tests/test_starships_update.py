from starwars.app.starships_update import starships_update
from starwars.app.api_request import api_request


def test_starships_update():
    assert len(starships_update(api_request())) == 10
