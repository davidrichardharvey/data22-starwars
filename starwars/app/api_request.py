import requests
from pprint import pprint


def api_request(url):
    starships = requests.get(url)
    return starships



