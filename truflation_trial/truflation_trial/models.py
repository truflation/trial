# This file contains Pydantic models, which are used for defining the structure of data for API requests and responses.


from pydantic import BaseModel # For defining the structure of data for API requests and responses
from datetime import date

# from typing import Sequence, List


# class Symbol(BaseModel):
#     #id: int
#     #symbol: str
#     value: str
#     #name: str
#     label: str
#     #exchange: str

# class Info(BaseModel):
#     symbol: str
#     name: str

# class SymbolRequest(BaseModel):
#     symbol: str


class History(BaseModel):
    id : int
    created_at : date
    date_value : date
    value : float
    