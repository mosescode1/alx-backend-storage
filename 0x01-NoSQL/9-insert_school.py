#!/usr/bin/python3
"""Module to insert to collection"""


def insert_school(mongo_collection, **kwargs):
    """Function insering to collection"""

    value = mongo_collection.insert_one(kwargs);
    return value.inserted_id
