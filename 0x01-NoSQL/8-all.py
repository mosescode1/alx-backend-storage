#!/usr/bin/python3
"""Module to list all collection"""


def list_all(mongo_collection):
    """Function that list all collection"""

    if mongo_collection is None:
        return []
    return [doc for doc in mongo_collection.find()]
