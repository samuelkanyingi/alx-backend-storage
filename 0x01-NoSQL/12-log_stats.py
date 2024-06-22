#!/usr/bin/env python3
from pymongo import MongoClient

def log_stats():
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)
    db = client.logs
    collection = db.nginx
    
    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # GET /status check
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
