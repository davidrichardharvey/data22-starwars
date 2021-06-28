from api_request import *
from sw_mongo import *
from pprint import pprint

# See data on all available starships
pprint(get_all_pages_starships())

# Drop, create and insert data into starships collection
drop_starships_collection()
create_starships_collection()
insert_starships_info()

# Replace pilot's urls with names
replace_url_with_name()

# Get pilots' ObjectIds
get_persons_objectid()

# Replace pilot's names with ObjectIds
replace_name_with_id()
