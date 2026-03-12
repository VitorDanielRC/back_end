from fastapi import APIRouter
from database import users_collections
from schemas import user

router = APIRouter()

@router.get("/users")
def list_users():
    users = []

    for user in users_collections.find():
        user["_id"] = str(user["_id"])
        user.append(users)

    return users

@router.post("/users")
def list_users():
    users = []

    for user in users_collections.find():
        user["_id"] = str(user["_id"])
        user.append(users)

    return users

#post - CREATE USER
#GET - USER BY ID