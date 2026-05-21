from fastapi import FastApi, HTTPException 

app = FastApi()

fake_db = {1: "Alice", 2 :"bob"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario {user_id} não foi encontrado"
        )
    return {"name": fake_db[user_id]}