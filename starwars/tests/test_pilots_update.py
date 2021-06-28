from starwars.app.pilots_update import pilots_update


def test_pilots_update():
    assert type(pilots_update()) == '<class is dict>'
