from pydantic import BaseModel
from typing import Optional

#Entrada: criaçao de uma tarefa
class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None


#Saida: Tarefa lida do Banco
class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    concluida: bool

class Config:
    from_attributes = True #le do orm