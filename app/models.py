from sqlalchemy import Column, Integer, DECIMAL, Date, TIMESTAMP
from sqlalchemy.sql import func
from database import Base


class ClosePrice(Base):
    __tablename__ = "ClosePrice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_value = Column(Date, nullable=False)
    value = Column(DECIMAL(10, 0), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
