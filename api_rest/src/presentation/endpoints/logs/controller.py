from fastapi import APIRouter, Depends, FastAPI, Request
from dependency_injector.wiring import inject, Provide
from infrastructure.container import Container
from domain.use_cases.iget_logs_use_case import IGetLogsUseCase
from presentation.schemas.logs import LagsSchemaPaginateSchema

router = APIRouter(tags=['Logs'])

@router.get("/logs", response_model=LagsSchemaPaginateSchema)
@inject
async def get_logs(request: Request, limit: int = 12, offset: int = 0, service: str = None, 
                   get_logs_use_case: IGetLogsUseCase = Depends(Provide(Container.get_logs_use_case))):
    logs = await get_logs_use_case.execute(limit=limit, offset=offset, service=service)
    return logs


def configure(app: FastAPI):
    app.include_router(router)