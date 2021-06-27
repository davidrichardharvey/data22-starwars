from starwars.app.starships_update import starships_update


def test_starships_update():
    assert len(starships_update()) == 10
