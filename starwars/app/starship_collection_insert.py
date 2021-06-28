# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:21:52 2021

@author: Andrew Rothwell
"""

from starwars.app.starship_pull_request import transform_starship_data
import pymongo

# Inserts the formatted swapi starship data into a MongoDB collection.

client = pymongo.MongoClient()

db = client['starwars']


def collection_insert():
    db.starships.drop()
    starship_data = transform_starship_data()
    for entry in starship_data:
        db.starships.insert_one(entry)
    return db.starships.count_documents({})
