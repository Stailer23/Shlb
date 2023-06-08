from typing import Union
from uuid import UUID

from sqlalchemy import and_
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import User

class UserService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self,
                    name: str,
                    hashed_password: str
                    ) -> User:
                    new_user = User(
                    name = name,
                    hashed_password = hashed_password
                    )
                    self.db_session.add(new_user)
                    await self.db_session.flush()
                    return new_user
