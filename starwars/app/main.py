from starwars.app.data_update import *
from starwars.app.mongodb_update import *

updated_data = run_all()
print('Updated starships:', updated_data)
drop_startships()
create_starships_collection()
update_starships(updated_data)
