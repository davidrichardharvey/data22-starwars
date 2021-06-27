from starwars.app.db_drop import db_drop


def test_db_drop():
    assert db_drop() == []
