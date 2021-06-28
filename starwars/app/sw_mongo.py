import pymongo
from api_request import get_all_pages_starships

client = pymongo.MongoClient()
db = client['starwars']


def get_persons_objectid():
    people = db.characters.find()
    peoples_urls_dict = {}
    for person in people:
        persons_name = person['name']
        persons_id = person['_id']
        peoples_urls_dict[persons_name] = persons_id  # peoples_url_dict = {persons_name: persons_id}
    return peoples_urls_dict


def drop_starships_collection():
    db.drop_collection('starships')


def create_starships_collection():
    starships_coll = db['starships']
    starships_coll.insert_many(get_all_pages_starships())


# drop_starships_collection()
# create_starships_collection()
