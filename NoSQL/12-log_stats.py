#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs
stored in MongoDB
"""


from pymongo import MongoClient

if __name__ == "__main__":
    """
    Main entry point of the script.

    This block of code is executed when the script is run directly.
    It performs the following tasks:
    1. Connects to the MongoDB instance.
    2. Accesses the 'nginx' collection in the 'logs' database.
    3. Counts and prints the total number of logs.
    4. Counts and prints the number of logs for each HTTP method.
    5. Counts and prints the number of status check logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("    method {}: {}".format(
            method, collection.count_documents({"method": method})))

    print("{} status check".format(collection.count_documents(
        {"method": "GET", "path": "/status"})))
