# input request test is fine

import json
import requests
import pymongo


# Connect to MongoDB and select database
client = pymongo.MongoClient()
db = client["starwars"]


# Test to ensure requests are successful from the API
def api_call(url):
    response = requests.get(url)
    return response


# Return all the results from all the pages
# Create a list of all results
# Return format [{}]
data_list = []


def api_request():
    total_results = []
    for page_number in range(1, 5):
        url = "https://swapi.dev/api/starships/?page="
        response = requests.get(url + str(page_number)).text
        response_data = json.loads(response)
        total_results = total_results + response_data["results"]
        for result in range(len(response_data["results"])):
            data_list.append(response_data["results"][result])

    return data_list


print(api_request())


def url_request(response):
    return requests.get(response).json()
