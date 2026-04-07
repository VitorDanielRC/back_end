from fastapi import FastAPI
from routers.tarefa_router import router as tarefa_router

app = FastAPI(
    title="CRUD de Tarefas",
    description="API CRUD com FastAPI + MongoDB + Docker",
    version="1.0.0"
)

app.include_router(tarefa_router, prefix="/tarefas", tags=["Tarefas"])

@app.get("/")
def home():
    return {"message": "FastAPI + MongoDB + Docker funcionando"}