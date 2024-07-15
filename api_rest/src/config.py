import os

class Config:
    DATABASE_URL = os.getenv('A-POSTGRES_DATABASE_URL', 'postgresql+asyncpg://admin:admin@127.0.0.1:5432/postgres')
