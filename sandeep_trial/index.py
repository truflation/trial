import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from sandeep_trial.adapters.yahoo_finance import YahooFinance
from sandeep_trial.database import create_db_and_tables, delete_db_and_tables, engine
from sandeep_trial.models.feed import Feed


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield

    delete_db_and_tables()


app = FastAPI(lifespan=lifespan)


@app.get("/feed")
async def insert_feed():
    yf = YahooFinance()
    data = yf.get_data()

    with Session(engine) as session:
        try:
            session.execute(insert(Feed), data)
            session.commit()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=500, detail="Integrity Error")

    return "Data feed run successfully"

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
