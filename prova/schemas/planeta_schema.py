from pydantic import BaseModel

class Planeta(BaseModel):
    nome: str
    galaxia: str
    diametro_km: float
    habitado: bool