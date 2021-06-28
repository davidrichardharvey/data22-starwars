from starwars.app.obtain_objectID import *

def test_obtain_object_id():
    assert len(obtain_object_id()) == 87


def test_obtain_character_name():
    assert len(obtain_character_name()) == 87
    assert obtain_character_name()[0] == "Ackbar"

def test_dictionary_for_character():
    assert create_character_dict()["Ackbar"]



