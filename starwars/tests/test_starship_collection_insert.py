# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:14:05 2021

@author: Andrew Rothwell
"""
from starwars.app.starship_collection_insert import collection_insert
import pymongo

client = pymongo.MongoClient()

db = client['starwars']


# Tests if the collection inserted into MongoDB is 36 fields long.
def test_starship_collection_length():
    assert collection_insert() == 36
