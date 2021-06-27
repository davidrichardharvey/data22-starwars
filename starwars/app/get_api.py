import requests
import json
from pprint import pprint
import pymongo

client=pymongo.MongoClient()
db=client['starwars']

class find_starships:

    def __init__(self):
        self.s_ships = None
        self.url="https://swapi.dev/api/starships/?page="
        #An empty list for all starships
        self.total_results = []
        self.page_count=1

    def find_page_count(self):
        response = requests.get(self.url)
        self.s_ships = response.json()
        while self.s_ships['next'] is not None:
            response = requests.get(self.s_ships['next'])
            self.s_ships = response.json()
            self.page_count += 1
        return(self.page_count)

    #A function that stores data from url argument from ALL pages into an empty list
    def get_api(self):

        for page in range(1,self.page_count+1):

            url = self.url + str(page)
            response = requests.get(url)
            self.s_ships = response.json()
            self.total_results = self.total_results + self.s_ships['results']

        return(self.total_results)


    #def get_ships_pilot(selfs):




Obj = find_starships()
Obj.find_page_count()
print(Obj.get_api())


