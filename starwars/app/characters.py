
from get_api import *
import pymongo
client=pymongo.MongoClient()
db=client['starwars']

class find_characters(starships):

    def __init__(self):
        super().__init__()
        self.name_url=None
        self.name=[]
        self.character_url=[]
        self.ob_id=None
        self.counter=0

    def locate_url(self):
        self.name_url = [i['pilots'] for i in self.pilots]
        print(self.name_url) ##len 15 with elemtns in each of these OK


    def find_name(self):

        for spaceship in self.name_url:
            for url in spaceship:

                response = requests.get(url)
                self.character_url = response.json()
                self.name.append(self.character_url['name'])

        print(self.name) #len 30 OK

    def find_obj_id(self):

        id=db.characters.find({"name":{"$in": self.name}},{"_id":1})
        self.ob_id=[pilot["_id"] for pilot in id]
        print(self.ob_id) ##len 19

    # def replace_url_with_object(self):
    #
    #     for x in range(len(self.pilots)):
    #         print(self.pilots[x]['pilots'], len(self.pilots[x]['pilots']))
    #
    #         print(self.ob_id)
    #         self.pilots[x]['pilots']=self.ob_id[self.counter:len(self.pilots[x]['pilots'])+self.counter]
    #         print(self.pilots[x]['pilots']) ###some objects are pilots on multiple starships
    #
    #         self.counter+= len(self.pilots[x]['pilots'])
    #         print(self.counter)
    #         print(self.pilots)




Obj3=find_characters()
Obj3.find_page_count()
Obj3.get_api()
Obj3.get_ships_pilot()
Obj3.locate_url()
Obj3.find_name()
Obj3.find_obj_id()
