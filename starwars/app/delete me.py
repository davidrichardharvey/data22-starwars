import requests
import pymongo
people_names = []
objectID = []


client = pymongo.MongoClient()
db = client["starwars"]


people = db.characters.find()

#obtains object id and name list

for person in people:
    people_names.append(person["name"])
    objectID.append(person["_id"])

#creates dictionary with object id and name

res = {people_names[i]: objectID[i] for i in range(len(people_names))}
print(res)

print(res["Ackbar"])








starships_url = "https://swapi.dev/api/starships"


def read_api():
    starships = requests.get(starships_url)
    return starships


def create_dict(data):
    dictionary = data.json()
    return dictionary["results"]



print(read_api())
d = create_dict(read_api())
print(d[4]["pilots"])

list = []

#replaces url with pilot name
for i in d:
    for f in i["pilots"]:
        a = i["pilots"].index(f)
        i["pilots"][a] = requests.get(f).json()["name"]

print(d[4]["pilots"])
print(d)

# replaces names in pilots with object id's
for i in d:
    for f in i["pilots"]:
        for key, value in res.items():
            if f == key:
                a = i["pilots"].index(f)
                i["pilots"][a] = res[key]

print(d[4]["pilots"])
