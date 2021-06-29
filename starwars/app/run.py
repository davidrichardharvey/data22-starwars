def run_files():
    current_collection_drop()
    create_starship_collection()
    insert_starship()
    replace_pilots_character_name()
    replace_pilots_objectids()
    collection = db.starships
    print(collection)

print(run_files())