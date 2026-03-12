from pymongo import MongoClient

MONGO_URL = "mongodb://mongo:27018"

client = MongoClient(MONGO_URL)

db = client["aula_nosql"]
users_collections = db["users"]