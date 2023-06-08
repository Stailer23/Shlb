from fastapi import FastAPI, Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from api.handlers import user_router
from db.service import UserService
from api.schemas import UserCreate, ShowUser
from db.session import get_db

app = FastAPI(title="qeqwe")


main_api_router = APIRouter()
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)