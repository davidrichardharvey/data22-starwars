import pymongo

client = pymongo.MongoClient()
db = client['starwars']

people = db.characters.find()
for person in people:
    print(person['_id'], person['name'])
