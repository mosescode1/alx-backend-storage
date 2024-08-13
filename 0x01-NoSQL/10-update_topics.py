#!/usr/bin/python3
"""Module that updates"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a document that matches the 'name'.
    If no matching document is found, a new document is inserted with the given 'name' and 'topics'.

    Parameters:
    mongo_collection: pymongo.collection.Collection
        The MongoDB collection to update.
    name: str
        The name of the document to update.
    topics: list
        The new topics to set for the document.

    Returns:
    None
    """
    result = mongo_collection.update_one(
        {"name": name},             
        {"$set": {"topic": topics}},  
        upsert=True
    )

