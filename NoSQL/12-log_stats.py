#!/usr/bin/env python3
"""
This Python script connects to a MongoDB database and provides statistics
about Nginx logs stored in the 'nginx' collection of the 'logs' database.

The script performs the following tasks:
1. Connects to the MongoDB instance running on localhost at port 27017.
2. Accesses the 'nginx' collection in the 'logs' database.
3. Counts the total number of logs in the collection.
4. Counts the number of logs for each HTTP method (GET, POST, PUT, PATCH,
    DELETE).
5. Counts the number of status check logs (GET requests to the '/status' path).
6. Prints the statistics to the console.

Usage:
Run the script from the command line to see the statistics printed
to the console.

Example output:
0 logs
Methods:
    method GET: 0
    method POST: 0
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
0 status check
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

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("    method {}: {}".format(
            method, collection.count_documents({"method": method})))

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))
