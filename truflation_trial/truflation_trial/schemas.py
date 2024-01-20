from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship
from database import Base


class HistorySchema(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    date_value = Column(Date)
    value = Column(Numeric(10, 6))
    created_at = Column(Date)