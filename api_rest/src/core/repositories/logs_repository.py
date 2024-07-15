from typing import Dict, List, Tuple

from sqlalchemy import desc, func, select
from infrastructure.database.repositories.repository import SqlRepository
from infrastructure.database.entities.logs import Logs


class LogsRepositor(SqlRepository):
    model = Logs

    async def get_logs_paginated(self, limit: int, offset: int, service: str) -> Tuple[Logs, int]:
        async with self.session_factory() as session:
            if service:
                query = select(self.model).limit(limit).offset(offset).where(self.model.service == service)
                total_query = select(func.count("*")).select_from(self.model).where(self.model.service == service)
            else:
                query = select(self.model).limit(limit).offset(offset)
                total_query = select(func.count("*")).select_from(self.model)
    
            total = await session.execute(total_query)
                
            results = await session.execute(query.order_by(desc('datetime')))
            total = total.scalar()
            results = results.scalars().all()
            return results, total
