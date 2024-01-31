from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from datetime import date
from database import get_db
from sqlalchemy.orm import Session
import crud


app = FastAPI()


@app.get("/")
def read_root():
    html_content = """
        <html>
            <head>
                <title>Lithium/USD price query app</title>
            </head>
            <body>
                <h2>Application to check Lithium USD Price</h2>
                
                <h3>Available API</h3>
                - /docs                       : Swagger UI for test </br>
                - /prices                     : get every prices from DB </br>
                - /prices/latest              : get latest price from DB </br>
                - /prices/from/{target_date}  : get data list since {target_date} </br>
                - /prices/{target_date}       : get data of {target_date}
                </p>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/prices/latest")
def get_latest_data(db: Session = Depends(get_db)):
    return crud.get_latest_price(db=db)


@app.get("/prices")
def get_every_data(db: Session = Depends(get_db)):
    return crud.get_prices(db=db)


@app.get("/prices/from/{target_date}")
def get_data_from_target_date(target_date: date, db: Session = Depends(get_db)):
    return crud.get_price_from_date(target_date=target_date, db=db)


@app.get("/prices/{target_date}")
def get_data_on_target_date(target_date: date, db: Session = Depends(get_db)):
    price = crud.get_price_by_date(db=db, target_date=target_date)
    if price is None:
        raise HTTPException(status_code=404, detail="Price not found")
    return price
