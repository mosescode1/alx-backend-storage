#!/usr/bin/env python3
"""Module for log stats"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')

# db = client["logs"]
# col = db["nginx"]
db = client.logs
col = db.nginx

str = "{} logs".format(col.count_documents({}))
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print(str)
print("Methods:")

for val in method:
    count = col.count_documents({'method': val})
    print("\tmethod {}: {}".format(val, count))

status_count = col.count_documents({'method': 'GET', "path": "/status"})
print("{} status check".format(status_count))
