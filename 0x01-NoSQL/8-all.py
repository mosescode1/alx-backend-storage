#!/usr/bin/env python3
"""Module to list all collection"""


def list_all(mongo_collection):
    """Function that list all collection"""

    if mongo_collection is None:
        return []
    return mongo_collection.find()
