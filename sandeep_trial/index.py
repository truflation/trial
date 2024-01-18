import yfinance as yf
from datetime import datetime
import pandas as pd


def main():
    ticker = yf.Ticker("LITH-USD")
    daily = ticker.history()
    close = daily.Close.reset_index()
    close["created_at"] = pd.Timestamp(datetime.today())
    close_dict = close.to_dict(orient="records")
    print(close_dict)

if __name__ == "__main__":
    main()