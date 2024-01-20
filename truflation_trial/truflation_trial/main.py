# from fastapi import (
#     APIRouter,
#     BackgroundTasks,
#     Depends,
#     FastAPI,
# )
# from fastapi.middleware.cors import CORSMiddleware
# import sqlalchemy
# from sqlalchemy.orm import Session
import yfinance as yf
import pandas as pd
from datetime import datetime
# from typing import List

from database import Base, engine, get_db, SessionLocal
from schemas import HistorySchema
# from models import History

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

Base.metadata.create_all(bind=engine)

if __name__ == '__main__': 
    add_Feed()