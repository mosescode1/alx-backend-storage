#!/usr/bin/env python3
"""Module for log stats"""


if __name__ == "__main__":
    """ Include mongob"""
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

    status_count = col.count_documents(
        {'method': 'GET', "path": "/status"}
    )
    print("{} status check".format(status_count))

    values = col.find({}, {'ip': 1, '_id': 0}).limit(10).sort({'ip': 1})
    print("IPs:")
    for val in values:
        print("\t{}".format(val.get("ip")))

    client.close()
