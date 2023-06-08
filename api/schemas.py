import uuid
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr

class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        orm_mode = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    is_active: bool


class UserCreate(BaseModel):
    name: str
    password: str