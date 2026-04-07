from pymongo import MongoClient

MONGO_URL = "mongodb://mongodb:27017"

client = MongoClient(MONGO_URL)
db = client["crud_fastapi"]
tarefas_collection = db["tarefas"]