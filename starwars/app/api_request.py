import requests


def api_request(url):
    # Calls the information from the stated url
    starships = requests.get(url)
    return starships
