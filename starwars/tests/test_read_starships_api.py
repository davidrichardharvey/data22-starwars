from starwars.app.read_starships_api import *


# ModuleNotFoundError - starwars is not a module name
# fixed by opening data22-starwars in pycharm, rather than starwars


# test to see whether the functions print the starships information as a dictionary
def test_read_starships_api_page1():
    assert str(type(read_starships_api_page1())) == "<class 'dict'>"


def test_read_starships_api_page2():
    assert str(type(read_starships_api_page2())) == "<class 'dict'>"


def test_read_starships_api_page3():
    assert str(type(read_starships_api_page3())) == "<class 'dict'>"


def test_read_starships_api_page4():
    assert str(type(read_starships_api_page4())) == "<class 'dict'>"
