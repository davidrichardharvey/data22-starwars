from api_req import req_api
from connect_to_mongodb import *


#  The code below converts the data imported from the api request to json and prints it.
#  I used this to conclude that I would first need to access the "results" key, the value of which contains a list of
#  dictionaries for each starship.
#  From there, I could iterate through each dictionary, gathering the required information.
def api_preview():
    import json
    api = req_api('https://swapi.dev/api/starships/').json()
    data = json.dumps(api)
    print(data)


starships_results_json = req_api('https://swapi.dev/api/starships/').json()['results']


def import_starships():

    #  The API request pulls through
    for ship in starships_results_json:
        db.starships.insert_one(ship)

    print("Imported starships data.")
