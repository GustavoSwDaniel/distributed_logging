from typing import Dict, List
from domain.use_cases.iget_logs_use_case import IGetLogsUseCase
from infrastructure.database.repositories.irepository import IRepository
from presentation.pagination import paginate

class GetLogsUseCase(IGetLogsUseCase):
    def __init__(self, logs_repository: IRepository) -> None:
        self.logs_repository = logs_repository
        

    async def execute(self, limit: int, offset: int, service: str) -> Dict:
        logs, total = await self.logs_repository.get_logs_paginated(limit=limit, offset=offset, service=service)
        logs_paginated = paginate(result=logs, offset=offset, total=total)
        return logs_paginated