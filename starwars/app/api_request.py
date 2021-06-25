import requests

def api_call():
    return requests.get("https://swapi.dev/api/")

print(api_call())
