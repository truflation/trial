import pandas as pd
import yfinance as yf
import uvicorn

from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from sandeep_trial.database import create_db_and_tables, delete_db_and_tables, engine
from sandeep_trial.model.feed import Feed


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield

    delete_db_and_tables()


app = FastAPI(lifespan=lifespan)


@app.get("/feed")
async def insert_feed():
    try:
        ticker = yf.Ticker("LITH-USD")
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong.")

    daily = ticker.history()
    close = daily.Close.reset_index()

    # Add created_at column
    close["created_at"] = pd.Timestamp(datetime.now())
    # Round the close data to 6 decimals
    close = close.round({"Close": 6})
    # Rename columns to suit with the db table columns
    close.rename(columns={"Date": "date_value", "Close": "value"}, inplace=True)
    # convert the pandas dataframe into a dictionary
    close_dict = close.to_dict(orient="records")

    with Session(engine) as session:
        try:
            session.execute(insert(Feed), close_dict)
            session.commit()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=500, detail="Integrity Error")


@app.get("/")
async def index():
    results = []
    with Session(engine) as session:
        results = session.execute(select(Feed)).scalars().all()

    # @TODO Bring templating engine to display the results
    if not len(results):
        return "No data found. Go to 127.0.01/feed url first to fetch the data."
    
    return results


def start():
    uvicorn.run("sandeep_trial.index:app", host="127.0.0.1", port=8000, reload=True)
