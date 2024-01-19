import yfinance as yf
import uvicorn
from datetime import datetime
import pandas as pd
from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from contextlib import asynccontextmanager
from sandeep_trial.database import create_db_and_tables, delete_db_and_tables, engine
from sandeep_trial.model.feed import Feed


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield

    delete_db_and_tables()

app = FastAPI(lifespan=lifespan)


@app.put("/feed")
async def insert_feed():
    ticker = yf.Ticker("LITH-USD")
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
        '''
        @TODO Add try-except to catch unique constraint error and
        other general errors
        '''
        session.execute(
            insert(Feed),
            close_dict
        )
        session.commit()
    
@app.get("/")
async def index():
    results = []
    with Session(engine) as session:
        results = session.execute(select(Feed)).scalars().all()

    # @TODO Bring templating engine to display the results
    return results

def start():
    uvicorn.run("sandeep_trial.index:app", host="127.0.0.1", port=8000, reload=True)
