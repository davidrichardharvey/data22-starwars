import pymongo
from pprint import pprint
import requests

# response = requests.get("http https://swapi.dev/api/starships")
# print(response.json())

client = pymongo.MongoClient()
db = client['starwars']
