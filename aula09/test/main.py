from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tarefas_db = {}
proximo_id = 1


class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False


@app.get("/tarefas")
def listar_tarefas():
    return list(tarefas_db.values())


@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    global proximo_id

    nova = {
        "id": proximo_id,
        "titulo": tarefa.titulo,
        "concluida": tarefa.concluida
    }

    tarefas_db[proximo_id] = nova
    proximo_id += 1

    return nova


@app.get("/tarefas/{tarefa_id}")
def obter_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas_db:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return tarefas_db[tarefa_id]