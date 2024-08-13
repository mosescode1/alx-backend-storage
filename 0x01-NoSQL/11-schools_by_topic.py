#!/usr/bin/env python3
"""Module
"""


def schools_by_topic(mongo_collection, topic):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: document
    """

    if mongo_collection is None:
        return None

    return mongo_collection.find({"topics": topic})
