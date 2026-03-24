from pydantic import BaseModel

class Veiculos(BaseModel):
    tipo: str
    modelo: str
    quantidade: int