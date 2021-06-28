import requests


# this function reads the urls in the original starships documents,
# which is required in order to convert them into the matching pilot objectIDs.
def pilot_api_reader(url):
    response = requests.get(url)
    return response.json()
