import requests
from pprint import pprint
import pymongo
from starwars.app.api_request import api_request
from starwars.app.pilots_update import pilots_update
from starwars.app.starships_update import starships_update
from starwars.app.db_drop import db_drop

client = pymongo.MongoClient()
db = client['starwars']

db_drop()
starships_update(api_request("https://swapi.dev/api/starships"))
starships_update(api_request("https://swapi.dev/api/starships/?page=2"))
starships_update(api_request("https://swapi.dev/api/starships/?page=3"))
starships_update(api_request("https://swapi.dev/api/starships/?page=4"))
pilots_update()
pprint([ship for ship in db.starships.find()])
