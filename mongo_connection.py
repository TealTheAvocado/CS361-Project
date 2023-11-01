from pymongo import MongoClient

def connect_to_mongodb():
    # Replace these connection details with your MongoDB cluster's information.
    MONGO_URI = "mongodb://florazhang:Flora2185885@cluster.mongodb.net/Cluster0"
    client = MongoClient(MONGO_URI)
    db = client.get_database()
    return db

def insert_data(collection, data):
    # Insert data into the specified collection
    collection.insert_one(data)

# Define more functions for CRUD operations, updates, and deletions as needed
