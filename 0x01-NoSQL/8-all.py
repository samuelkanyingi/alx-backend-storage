#!/usr/bin/env python3
""" list all documents """

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    List all documents in the provided MongoDB collection.
    Returns:
        A list of documents in the collection.
    """
    all_documents = []
    for document in mongo_collection.find({}):
        all_documents.append(document)
    return mongo_collection.find()
