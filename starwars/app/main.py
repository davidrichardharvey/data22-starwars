import pymongo
import requests
from pprint import pprint

get_api = requests.get("https://swapi.dev/api/")

client = pymongo.MongoClient()
db = client['starwars']

