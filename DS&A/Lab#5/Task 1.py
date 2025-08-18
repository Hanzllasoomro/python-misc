from pymongo import MongoClient

# connect to mongodb server
client = MongoClient("mongodb://localhost:27017/")

# connect to database
db = client["restaurant_db"]

# connect to collection
collection = db["restaurant"]

for doc in collection.find({}, {"restaurant_id": 1001, "name": 1, "borough": 1, "cuisine": 1}):
    print(doc)
