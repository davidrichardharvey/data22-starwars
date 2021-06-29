import requests
from pprint import pprint
import json


def api_call(url):
    # Function for API requests
    req = requests.get(url)
    return req


def api_store(url):
    # Function to store API requests in dictionary format
    req = requests.get(url)
    return req.json()


def print_req(arg):
    # Function to print data from api_call in json format
    req = arg
    return pprint(req.json())


