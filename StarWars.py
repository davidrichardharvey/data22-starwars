import pymongo
from pprint import pprint
import requests

response = requests.get("https://swapi.dev/api/starships")
pprint(response.json())

# client = pymongo.MongoClient()
# db = client['starwars']
