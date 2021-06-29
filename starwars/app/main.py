from starwars.app.data_update import *
from starwars.app.mongodb_update import *

updated_data = run_all()
drop_startships()
create_starships_collection()
update_starships_collection(updated_data)
