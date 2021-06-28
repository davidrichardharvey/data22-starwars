import requests

starships_url = "https://swapi.dev/api/starships"


def read_api():
    starships = requests.get(starships_url)
    return starships


def create_dict(data):
    dictionary = data.json()
    return dictionary





#["results"]
print(type(create_dict(read_api())))
print(read_api())
d = create_dict(read_api())
#print(d[4]["pilots"])




