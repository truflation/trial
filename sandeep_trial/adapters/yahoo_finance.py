import pandas as pd
import yfinance as yf

from datetime import datetime

from fastapi import HTTPException


class YahooFinance:
    def get_data(self) -> dict:
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
        data = close.to_dict(orient="records")

        return data
