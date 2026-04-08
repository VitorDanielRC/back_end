from repositories.planeta_repository import *

def format_planeta(planeta):
    planeta["_id"] = str(planeta["_id"])
    return planeta

def create_planeta_service(planeta):
    result = create_planeta(planeta.model_dump())
    return {"message": "Planeta criado", "id": str(result.inserted_id)}

def get_all_planetas_service():
    planetas = get_all_planetas()
    return [format_planeta(planeta) for planeta in planetas]

def get_planeta_by_id_service(planeta_id):
    try:
        planeta = get_planeta_by_id(planeta_id)
    except:
        return {"error": "ID inválido"}
    if not planeta:
        return {"error": "Planeta não encontrado"}
    return format_planeta(planeta)

def update_planeta_service(planeta_id, planeta):
    try:
        result = update_planeta(planeta_id, planeta.model_dump())
    except:
        return {"error": "ID inválido"}
    if result.matched_count == 0:
        return {"error": "Planeta não encontrado"}
    return {"message": "Planeta atualizado"}

def delete_planeta_service(planeta_id):
    try:
        result = delete_planeta(planeta_id)
    except:
        return {"error": "ID inválido"}
    if result.deleted_count == 0:
        return {"error": "Planeta não encontrado"}
    return {"message": "Planeta removido"}