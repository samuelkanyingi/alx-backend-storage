#!/usr/bin/env python3
''' inserts a new document '''


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''
    inserts a new document in a collection based on kwargs
    '''
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
