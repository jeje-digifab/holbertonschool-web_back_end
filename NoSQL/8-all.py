#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection
    to list documents from.

    Returns:
    list: A list of all documents in the collection.
    """
    return list(mongo_collection.find())
