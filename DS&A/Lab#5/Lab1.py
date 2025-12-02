from pymongo import MongoClient

# connect to mongodb server
client = MongoClient("mongodb://localhost:27017/")

print(client)

# connect to database
db = client["restaurant_db"]

# connect to collection
collection = db["restaurant"]

# test query
for doc in collection.find().limit(2):
    print(doc)
