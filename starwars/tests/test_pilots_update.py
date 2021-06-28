from starwars.app.pilots_update import pilots_update


def test_pilots_update():
    assert str(type(pilots_update())) == "<class 'pymongo.cursor.Cursor'>"
