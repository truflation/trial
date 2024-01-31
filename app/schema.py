from typing import List
from pydantic import BaseModel
from datetime import datetime, date
from decimal import Decimal


class ClosePriceBase(BaseModel):
    id: int
    date_value: date
    value: Decimal
    created_at: datetime

    class Config:
        orm_mode = True


class ListClosePriceResponse(BaseModel):
    status: str
    results: int
    notes: List[ClosePriceBase]