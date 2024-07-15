from typing import List
from pydantic import BaseModel
from datetime import datetime
from typing import List

class LagsSchema(BaseModel):
    message: str
    type: str
    datetime: datetime
    service: str

    class Config:
        orm_mode = True


class LagsSchemaPaginateSchema(BaseModel):
    total: int
    offset: int
    count: int
    data: List[LagsSchema]