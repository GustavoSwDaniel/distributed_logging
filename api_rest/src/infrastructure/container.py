from dependency_injector import containers, providers
from infrastructure.database.database import PostgresDatabase
from config import Config
from core.use_case.get_logs_use_case import GetLogsUseCase
from core.repositories.logs_repository import LogsRepositor

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    postgres_db = providers.Singleton(PostgresDatabase, database_url=Config.DATABASE_URL)

    logs_repository = providers.Factory(LogsRepositor, session_factory=postgres_db.provided.session)

    get_logs_use_case = providers.Factory(GetLogsUseCase, logs_repository=logs_repository)
