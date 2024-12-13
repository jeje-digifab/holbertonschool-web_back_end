#!/usr/bin/env python3
"""
Write a Python function that returns the list of school having
a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    :param mongo_collection: MongoDB collection object
    :param topic: The specific topic to search for
    :return: A cursor object that can be iterated over to access the
        matching documents
    """

    return mongo_collection.find({"topics": topic})
