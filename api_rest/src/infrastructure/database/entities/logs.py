from sqlalchemy import Column, DateTime, String, DateTime
from infrastructure.database.entities.base import Base

class Logs(Base):
    __tablename__ = 'logs'

    id = Column(String, primary_key=True)
    message = Column(String)
    type = Column(String)
    service = Column(String)
    datetime = Column(DateTime)