import requests

# This function will take the information from the starships collection.


def read_api_pilot(url):
    response = requests.get(url)
    return response.json()
