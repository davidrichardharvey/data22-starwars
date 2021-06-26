import requests



def call_api():
    response_one = requests.get("https://swapi.dev/api/starships")
    response_two= requests.get("https://swapi.dev/api/starships/?page=2")
    response_three = requests.get("https://swapi.dev/api/starships/?page=3")
    response_four = requests.get("https://swapi.dev/api/starships/?page=4")
    return response_one, response_two, response_three, response_four



print(call_api())
