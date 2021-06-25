from starwars.app.StarWarsAPI import read_starships_api # ModuleNotFoundError - starwars is not a module name

def test_read_starships_api():
    assert read_starships_api('https://swapi.dev/api/starships/?page=1') == 'https://swapi.dev/api/starships/?page=1'




