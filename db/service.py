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
                    # query = select(User).where(User.name == name)
                    # res = await self.db_session.execute(query)
                    # print("moi query", res.fetchone())
                    self.db_session.add(new_user)
                    await self.db_session.flush()
                    return new_user

    async def delete_user(self, user_id: UUID) -> Union[UUID, None]:
        query = update(User).where(and_(User.user_id == user_id, User.is_active == True)).\
            values(is_active=False).\
            returning(User.user_id)
        res = await self.db_session.execute(query)
        deleted_user_id_row = res.fetchone()
        if deleted_user_id_row is not None:
            return deleted_user_id_row[0]

