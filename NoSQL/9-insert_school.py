#!/usr/bin/env python3
"""
Write a Python function that inserts a new document in a collection
based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a single document into the specified MongoDB collection and
    returns the inserted document's ID.

    Parameters:
    -----------
    mongo_collection : pymongo.collection.Collection
        The MongoDB collection into which the document will be inserted.
    **kwargs : dict
        The key-value pairs representing the document to be inserted.

    Returns:
    --------
    inserted_id : ObjectId
        The unique identifier of the inserted document.
    """

    return mongo_collection.insert_one(kwargs).inserted_id
