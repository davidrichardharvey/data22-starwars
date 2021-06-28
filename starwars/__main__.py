from starwars.app.create_starships_collection import create_starships_collection
from starwars.app.insert_starships import insert_starships
from starwars.app.replace_pilot_urls import replace_pilot_urls


def please_work():
    create_starships_collection()
    insert_starships()
    replace_pilot_urls()


if __name__ == '__main__':
    please_work()
