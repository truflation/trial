import uvicorn
from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy
from sqlalchemy.orm import Session
import yfinance as yf
import pandas as pd
from datetime import datetime

# from typing import List

from database import Base, engine, get_db, SessionLocal
from schemas import HistorySchema
from models import History

def add_Feed():
    db = SessionLocal()
    ticker = yf.Ticker("LITH-USD")
    h = ticker.history()
    df = h.Close.reset_index()
    df["created_at"] = pd.Timestamp(datetime.now())
    df = df.round({"Close": 6})
    df.rename(columns={"Date": "date_value", "Close": "value"}, inplace=True)
    df_records = df.to_dict(orient="records")
    for record in df_records:
        record["date_value"] = pd.Timestamp(record["date_value"])
        record["created_at"] = pd.Timestamp(record["created_at"])
        record["value"] = round(float(record["value"]), 6)
        # Create an instance of HistorySchema for each record
        history_schema = HistorySchema(**record)

        # Add the instance to the database session
        db.add(history_schema)

    # Commit changes to the database
    db.commit()
    db.close()

app = FastAPI()
router = APIRouter()
Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@router.get("/feed", status_code=200, response_model=list[History])
async def fetch_symbol():
    """
    Lithium Feed
    """
    db = SessionLocal()
    historyFeed = db.query(HistorySchema).all()
    res = [{"id": h.id, "date_value": h.date_value , "value":h.value , "created_at":h.created_at} for h in historyFeed]
    
    return res

def start():
    uvicorn.run("truflation_trial.main:app", host="127.0.0.1", port=8000, reload=True)

app.include_router(router)

# if __name__ == '__main__': 
#     add_Feed()
#     fetch_symbol()