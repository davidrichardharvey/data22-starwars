import requests
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


# A function that deletes any previous starship documents from the database
def delete_old_collection():
    db.starships.drop()


class ExtractStarships:

    def __init__(self):
        self.page_data = None  # A variable that with temporarily hold data from each page
        self.url = "https://swapi.dev/api/starships/?page="
        self.total_starships = []  # A list that will contain ALL starships
        self.page_count = 1  # Page count with increase dependant on the number of pages from root
        self.pilots = None  # A variable that will hold starships WITH pilots

    # A function that find the total number of pages for the following function
    def find_page_count(self):
        response = requests.get(self.url)
        self.page_data = response.json()
        while self.page_data['next'] is not None:
            response = requests.get(self.page_data['next'])
            self.page_data = response.json()
            self.page_count += 1
        return self.page_count

    # A function that stores data from url argument from ALL pages into an empty list
    def get_api(self):
        for page in range(1, self.page_count + 1):
            url = self.url + str(page)
            response = requests.get(url)
            self.page_data = response.json()
            self.total_starships = self.total_starships + self.page_data['results']

        return self.total_starships

    # A function that gets starships with pilots only
    def get_ships_with_pilots(self):
        self.pilots = [i for i in self.total_starships if not (i['pilots'] == [])]
