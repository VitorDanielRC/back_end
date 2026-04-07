from fastapi import APIRouter
from schemas.tarefa_schema import Tarefa
from services.tarefa_service import (
    create_tarefa_service,
    get_all_tarefas_service,
    get_tarefa_by_id_service,
    update_tarefa_service,
    delete_tarefa_service
)

router = APIRouter()

@router.get("/")
def listar_tarefas():
    return get_all_tarefas_service()

@router.post("/")
def criar_tarefa(tarefa: Tarefa):
    return create_tarefa_service(tarefa)

@router.get("/{tarefa_id}")
def buscar_tarefa(tarefa_id: str):
    return get_tarefa_by_id_service(tarefa_id)

@router.put("/{tarefa_id}")
def atualizar_tarefa(tarefa_id: str, tarefa: Tarefa):
    return update_tarefa_service(tarefa_id, tarefa)

@router.delete("/{tarefa_id}")
def deletar_tarefa(tarefa_id: str):
    return delete_tarefa_service(tarefa_id)