import requests
from pprint import pprint


def api_call(url):
    # Function for API requests
    req = requests.get(url)
    return req


def print_req(arg):
    # Function to pretty print data from api_call in json format
    req = arg
    return pprint(req.json())
