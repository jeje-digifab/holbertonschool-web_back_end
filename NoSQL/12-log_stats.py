#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs
stored in MongoDB
"""


from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx


print("{} logs".format(collection.count_documents({})))

print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print("\tmethod {}: {}".format(method, count))


print("{} status check".format(collection.count_documents(
    {"method": "GET", "path": "/status"})))
