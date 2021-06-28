from new_coll_create import *
from list_pilot_info import *


def run_application():
    connect_to_db()
    create_coll()
    import_starships()
    pilot_info_update()

run_application()