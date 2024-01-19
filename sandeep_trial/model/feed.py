from sqlmodel import SQLModel, Field
from decimal import Decimal
from datetime import datetime


class Feed(SQLModel, table=True):
    __tablename__ = "feed"
    id: int = Field(primary_key=True)
    date_value: datetime = Field(unique=True)
    value: Decimal = Field(max_digits=7, decimal_places=6)
    created_at: datetime = Field(default_factory=datetime.utcnow)