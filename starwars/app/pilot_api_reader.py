import requests

# a function that takes the pilots url from the starships collection and is able to read the info
def pilot_api_reader(url):
    response = requests.get(url)
    return response.json()