from sqlalchemy import select, update

from infrastructure.database.entities.base import Base
from infrastructure.database.repositories.irepository import IRepository


class SqlRepository(IRepository):
    model = Base

    async def get_all(self):
        async with self.session_factory() as session:
            result = await session.execute(select(self.model))
            return result.scalars().all()

    async def filter_by(self, params):
        async with self.session_factory() as session:
            result = await session.execute(select(self.model).filter_by(**params))
            return result.scalars().first()

    async def filter_all_by(self, params):
        async with self.session_factory() as session:
            result = await session.execute(select(self.model).filter_by(**params))
            return result.scalars()
