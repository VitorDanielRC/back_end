from fastapi import APIRouter
from schemas.planeta_schema import Planeta
from services.planeta_service import *

router = APIRouter()

@router.get("/planetas")
def list_planetas():
    return get_all_planetas_service()

@router.post("/planetas")
def create_planeta(planeta: Planeta):
    return create_planeta_service(planeta)

@router.get("/planetas/{planeta_id}")
def get_planeta(planeta_id: str):
    return get_planeta_by_id_service(planeta_id)

@router.put("/planetas/{planeta_id}")
def update_planeta(planeta_id: str, planeta: Planeta):
    return update_planeta_service(planeta_id, planeta)

@router.delete("/planetas/{planeta_id}")
def delete_planeta(planeta_id: str):
    return delete_planeta_service(planeta_id)