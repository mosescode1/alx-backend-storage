#!/usr/bin/python3
"""Module to list all collection"""


def list_all(mongo_collection):
    """Function that list all collection"""
    return  [doc for doc in mongo_collection.find()]

