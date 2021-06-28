from starwars.app.api_read import *
from starwars.app.obtain_objectID import *

if __name__ == '__main__':
    # read each page of the starships data
    starships_1 = read_api(starships_url_1)
    starships_2 = read_api(starships_url_2)
    starships_3 = read_api(starships_url_3)
    starships_4 = read_api(starships_url_4)

    # put each starship page into a list of dicts
    starships_1_list = create_list_of_dict(starships_1)
    starships_2_list = create_list_of_dict(starships_2)
    starships_3_list = create_list_of_dict(starships_3)
    starships_4_list = create_list_of_dict(starships_4)

    # merge all lists of dicts into one list
    all_starship_data = merge_lists_of_dicts(starships_1_list, starships_2_list, starships_3_list, starships_4_list)

    # changing all pilots from url to character name
    all_starship_data_names = change_pilot_to_character_name(all_starship_data)

    # obtaining objectID and character name for each character, then putting them into lists
    char_name = obtain_character_name()
    obj_id = obtain_object_id()

    # creating a dictionary where the key is character name and value is objectID
    create_character_dict(char_name, obj_id)

    # change all character names to objectID within pilots
    # replace_character_name_for_object_id(all_starship_data_names, character_dict)
