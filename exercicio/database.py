from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27018"

client = MongoClient(MONGO_URL)

db = client["banco"]

veiculos_collection = db["veiculos"]