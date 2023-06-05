from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas import UserCreate, ShowUser
from db.service import UserService
from db.session import get_db

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

@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate, db:AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_new_user(body, db)