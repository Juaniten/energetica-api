from fastapi import APIRouter
from server.models.schemas import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "User not found"}},
)


@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


@router.post("/")
async def create_user(user: User):
    return user


@router.put("/{user_id}")
async def update_user(user: User):
    return user


@router.delete("/{user_id}")
async def delete_user(user: User):
    return user
