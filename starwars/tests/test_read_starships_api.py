from starwars.app.read_starships_api import read_starships_api
# ModuleNotFoundError - starwars is not a module name


# test to see whether the function prints the starships information as a tuple
def test_read_starships_api():
    assert str(type(read_starships_api())) == "<class 'tuple'>"


