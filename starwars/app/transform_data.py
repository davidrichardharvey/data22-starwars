from starwars.app.get_api import *


class Find_Characters(ExtractStarships):

    def __init__(self):
        super().__init__()
        self.name_url = None
        self.name = []
        self.character_url = []
        self.dict = {}

    def locate_url(self):
        self.name_url = [i['pilots'] for i in self.pilots]
        return self.name_url

    def find_name(self):
        for spaceship in self.name_url:
            for url in spaceship:
                response = requests.get(url)
                self.character_url = response.json()
                self.name.append(self.character_url['name'])

        # print(self.name) #len 30 OK

    def find_obj_id(self):
        for x in self.name:
            list_of_id = db.characters.find({"name": x}, {"_id": 1})
            _id = [pilot["_id"] for pilot in list_of_id]
            self.dict[x] = _id

    def replace_url_with_name(self):
        for x in range(len(self.pilots)):
            name_list = []
            for pilots in self.pilots[x]['pilots']:
                response = requests.get(pilots)
                name = response.json()

                name_list.append(name['name'])
            self.pilots[x]['pilots'] = name_list

    def replace_name_with__id(self):
        for x in range(len(self.pilots)):
            another_list = []
            for key in self.dict.keys():
                # print(key)
                if key in self.pilots[x]['pilots']:
                    another_list.append(self.dict[key])
                    # print(self.dict[key])
            self.pilots[x]['pilots'] = another_list
        print(type(self.pilots))

    def insert_data_into_db(self):

        db.create_collection("starships")
        for x in self.pilots:
            db.starships.insert_one(x)
