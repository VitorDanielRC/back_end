from bson import ObjectId
from database import tarefas_collection

def create_tarefa(tarefa_dict):
    return tarefas_collection.insert_one(tarefa_dict)

def get_all_tarefas():
    return list(tarefas_collection.find())

def get_tarefa_by_id(tarefa_id):
    return tarefas_collection.find_one({"_id": ObjectId(tarefa_id)})

def update_tarefa(tarefa_id, tarefa_dict):
    return tarefas_collection.update_one(
        {"_id": ObjectId(tarefa_id)},
        {"$set": tarefa_dict}
    )

def delete_tarefa(tarefa_id):
    return tarefas_collection.delete_one({"_id": ObjectId(tarefa_id)})