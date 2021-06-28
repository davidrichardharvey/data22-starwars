from starwars.app.get_api import *


class FindCharacters(ExtractStarships):

    def __init__(self):
        super().__init__()
        self.name_url = None  # A variable that will contain a list. Each element will contain the pilots/pilot URL
        # Each element represents a starship
        self.name = []  # A list that will contain the names of each pilot
        self.object_id = {}  # A dictionary that will contain pilots names and their corresponding object id's

    # A function to create a list of URL's for every pilot
    def locate_url(self):
        self.name_url = [i['pilots'] for i in self.pilots]

    # A function to find the names corresponding to each URL
    def find_name(self):
        for spaceship in self.name_url:
            for url in spaceship:
                response = requests.get(url)
                name = response.json()
                self.name.append(name['name'])

    # A function to find the object id's corresponding to each name
    def find_obj_id(self):
        for x in self.name:
            list_of_id = db.characters.find({"name": x}, {"_id": 1})
            _id = [pilot["_id"] for pilot in list_of_id]
            self.object_id[x] = _id

    # A function to replace each URL with the corresponding name
    def replace_url_with_name(self):
        for x in range(len(self.pilots)):
            name_list = []
            for pilots in self.pilots[x]['pilots']:
                response = requests.get(pilots)
                name = response.json()

                name_list.append(name['name'])
            self.pilots[x]['pilots'] = name_list

    # A function to replace each name with the corresponding object id
    def replace_name_with__id(self):
        for x in range(len(self.pilots)):
            another_list = []
            for key in self.object_id.keys():
                # print(key)
                if key in self.pilots[x]['pilots']:
                    another_list.append(self.object_id[key])
                    # print(self.dict[key])
            self.pilots[x]['pilots'] = another_list

    # A function to insert the updated object id's into a new collection
    def insert_data_into_db(self):

        db.create_collection("starships")
        for x in self.pilots:
            db.starships.insert_one(x)
        print("Data successfully inserted into starwars database--> starships collection")