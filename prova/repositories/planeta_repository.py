from database import planeta_collection
from bson import ObjectId

def create_planeta(planeta_dict):
    return planeta_collection.insert_one(planeta_dict)

def get_all_planetas():
    return list(planeta_collection.find())

def get_planeta_by_id(planeta_id):
    return planeta_collection.find_one({"_id": ObjectId(planeta_id)})

def update_planeta(planeta_id, planeta_dict):
    return planeta_collection.update_one(
        {"_id": ObjectId(planeta_id)},
        {"$set": planeta_dict}
    )

def delete_planeta(planeta_id):
    return planeta_collection.delete_one(
        {"_id": ObjectId(planeta_id)}
    )