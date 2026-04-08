from fastapi import FastAPI
from routers.planeta_router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"Message": "Sistema de cadastro de planetas com MongoDB e FastAPI"}
