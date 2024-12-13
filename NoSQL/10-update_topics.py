#!/usr/bin/env python3
"""
Write a Python function that changes all topics of a school document based
on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates documents in a MongoDB collection and retrieves the updated
    documents sorted by name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection to operate on.
        name (str): The value of the 'name' field used to filter documents.
        topics (list): The list of topics to set in the 'topics' field.

    Returns:
        list: A list of updated documents sorted by the 'name' field.

    Example:
        mongo_collection = db["my_collection"]
        updated_docs = update_and_retrieve_sorted(mongo_collection, "Alice",
            ["Python", "MongoDB"])
        for doc in updated_docs:
            print(doc)

    Note:
        - The function updates all documents matching the
            filter `{ 'name': name }` by setting their
          'topics' field to the provided `topics` list.
        - After the update, the function retrieves and returns the updated
            documents sorted by the 'name' field.
    """

    collection_sorted = []

    mongo_collection.update_many(
        {'name': name},  # Filtre
        {'$set': {'topics': topics}}  # Mise à jour
    )

    updated_documents = mongo_collection.find({'name': name}).sort("name", 1)

    for doc in updated_documents:
        collection_sorted.append(doc)

    return collection_sorted
