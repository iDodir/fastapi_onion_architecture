from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import users_service
from src.schemas.users import UserSchemaAdd
from src.services.users import UsersService

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
async def add_user(
        user: UserSchemaAdd,
        users_service: Annotated[UsersService, Depends(users_service)],
):
    user_id = await users_service.add_user(user)
    return {"user_id": user_id}


@router.get("/")
async def get_users(
        users_service: Annotated[UsersService, Depends(users_service)],
):
    users = await users_service.get_users()
    return users
