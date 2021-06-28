from starwars.app.api_read import *
from starwars.app.obtain_objectID import *


def test_read_from_api():
    assert read_api(starships_url_1).status_code == 200
    assert read_api(starships_url_2).status_code == 200
    assert read_api(starships_url_3).status_code == 200
    assert read_api(starships_url_4).status_code == 200


def test_create_list_of_dict():
    assert type(create_list_of_dict(read_api(starships_url_1))) is list
    assert type(create_list_of_dict(read_api(starships_url_2))) is list
    assert type(create_list_of_dict(read_api(starships_url_3))) is list
    assert type(create_list_of_dict(read_api(starships_url_4))) is list


def test_merge_list_of_dict():
    dict1 = [{1: 2}, {2: 3}]
    dict2 = [{1: 2}, {2: 3}]
    dict3 = [{1: 2}, {2: 3}]
    dict4 = [{1: 2}, {2: 3}]
    assert len(merge_lists_of_dicts(dict1, dict2, dict3, dict4)) == 8


def test_change_pilot_to_character_name():
   assert change_pilot_to_character_name(all_starship_data)[4]["pilots"][1] == "Han Solo"


def test_replace_character_name_with_object_id():
   assert replace_character_name_for_object_id(all_starship_data_names1, character_dict1)[4]["pilots"][1] == character_dict1["Han Solo"]



