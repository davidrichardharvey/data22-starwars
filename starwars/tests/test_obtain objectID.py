from starwars.app.obtain_objectID import *


def test_obtain_object_id():
    assert len(obtain_object_id()) == 87


def test_obtain_character_name():
    assert len(obtain_character_name()) == 87
    assert obtain_character_name()[0] == "Ackbar"


obj = obtain_object_id()
char = obtain_character_name()
character_dict1 = create_character_dict(char, obj)

def test_dictionary_for_character():
    assert str(create_character_dict(char, obj)["Ackbar"]) == str(obj[0])



