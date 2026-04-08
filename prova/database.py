import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27018")
MONGO_DB = os.getenv("MONGO_DB", "P2BackEnd")

client = MongoClient(MONGO_URL)
db = client[MONGO_DB]

planeta_collection = db["planetas"]