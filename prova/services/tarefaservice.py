from repositories.tarefa_repository import (
    create_tarefa,
    get_all_tarefas,
    get_tarefa_by_id,
    update_tarefa,
    delete_tarefa
)

def format_tarefa(tarefa):
    tarefa["_id"] = str(tarefa["_id"])
    return tarefa

def create_tarefa_service(tarefa):
    result = create_tarefa(tarefa.model_dump())
    return {
        "message": "Tarefa criada com sucesso",
        "id": str(result.inserted_id)
    }

def get_all_tarefas_service():
    tarefas = get_all_tarefas()
    return [format_tarefa(tarefa) for tarefa in tarefas]

def get_tarefa_by_id_service(tarefa_id):
    try:
        tarefa = get_tarefa_by_id(tarefa_id)
    except:
        return {"error": "ID inválido"}

    if not tarefa:
        return {"error": "Tarefa não encontrada"}

    return format_tarefa(tarefa)

def update_tarefa_service(tarefa_id, tarefa):
    try:
        result = update_tarefa(tarefa_id, tarefa.model_dump())
    except:
        return {"error": "ID inválido"}

    if result.matched_count == 0:
        return {"error": "Tarefa não encontrada"}

    return {"message": "Tarefa atualizada com sucesso"}

def delete_tarefa_service(tarefa_id):
    try:
        result = delete_tarefa(tarefa_id)
    except:
        return {"error": "ID inválido"}

    if result.deleted_count == 0:
        return {"error": "Tarefa não encontrada"}

    return {"message": "Tarefa deletada com sucesso"}