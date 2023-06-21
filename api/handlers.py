from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas import UserCreate, ShowUser, DeleteUserResponse, UpdateUserResponse
from db.service import UserService
from db.session import get_db
from typing import Union

user_router = APIRouter()
async def _create_new_user(body: UserCreate, db) -> ShowUser:
    async with db as session:
        async with session.begin():
            user_serv = UserService(session)
            user = await user_serv.create_user(
                name=body.name,
                hashed_password=body.password
            )
            return ShowUser(
                user_id=user.user_id,
                name=user.name,
                is_active=user.is_active
            )

async def _delete_user(user_id, db) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_serv = UserService(session)
            deleted_user_id = await user_serv.delete_user(user_id)
            return deleted_user_id

@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate, db:AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_new_user(body, db)
@user_router.delete("/", response_model=DeleteUserResponse)
async def delete_user(user_id: UUID, db:AsyncSession = Depends(get_db)) -> DeleteUserResponse:
    deleted_user_id = await _delete_user(user_id, db)
    if deleted_user_id is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found.")
    return DeleteUserResponse(deleted_user_id=deleted_user_id)