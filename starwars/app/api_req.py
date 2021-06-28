import requests


#  Simple API request function using requests module.
def req_api(link):
    api = requests.get(link)
    return api


