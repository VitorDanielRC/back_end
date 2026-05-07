from pydantic import BaseModel, EmailStr
from datetime import datetime


# ---------------- PRODUTO ----------------

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    estoque: int = 0


class ProdutoResponse(ProdutoCreate):
    id: int

    class Config:
        from_attributes = True


# ---------------- ITEM ----------------

class ItemCreate(BaseModel):
    produto_id: int
    quantidade: int = 1


class ItemResponse(BaseModel):
    produto: ProdutoResponse
    quantidade: int

    class Config:
        from_attributes = True 
        
 