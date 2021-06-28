import pymongo
people_names = []
objectID = []


client = pymongo.MongoClient()
db = client["starwars"]


people = db.characters.find()

for person in people:
    people_names.append(person["name"])
    objectID.append(person["_id"])

res = {people_names[i]: objectID[i] for i in range(len(people_names))}
print(type(res))

for key, value in res.items():
    print(key)

